#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools


class ConanSqlite3(ConanFile):
    name = "sqlite3"
    version = "3.28.0"
    description = "Self-contained, serverless, in-process SQL database engine."
    url = "http://github.com/bincrafters/conan-sqlite3"
    homepage = "https://www.sqlite.org"
    author = "Bincrafters <bincrafters@gmail.com>"
    topics = ("conan", "sqlite", "database", "sql", "serverless")
    license = "Public Domain"
    generators = "cmake"
    settings = "os", "compiler", "arch", "build_type"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "FindSQLite3.cmake"]
    options = {"shared": [True, False],
               "fPIC": [True, False],
               "threadsafe": [0, 1, 2],
               "enable_column_metadata": [True, False],
               "enable_explain_comments": [True, False],
               "enable_fts3": [True, False],
               "enable_fts4": [True, False],
               "enable_fts5": [True, False],
               "enable_json1": [True, False],
               "enable_rtree": [True, False],
               "omit_load_extension": [True, False]
               }
    default_options = {"shared": False,
                       "fPIC": True,
                       "threadsafe": 1,
                       "enable_column_metadata": False,
                       "enable_explain_comments": False,
                       "enable_fts3": False,
                       "enable_fts4": False,
                       "enable_fts5": False,
                       "enable_json1": False,
                       "enable_rtree": False,
                       "omit_load_extension": False
                       }
    _source_subfolder = "source_subfolder"

    def source(self):
        sha256 = "d02fc4e95cfef672b45052e221617a050b7f2e20103661cda88387349a9b1327"
        download_url = "{}/2019".format(self.homepage)
        major, minor, patch = self.version.split(".")
        archive_name = "sqlite-amalgamation-" + major + minor.rjust(2, "0") + patch.rjust(2, "0") + "00"
        tools.get("{}/{}.zip".format(download_url, archive_name), sha256=sha256)
        os.rename(archive_name, self._source_subfolder)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["THREADSAFE"] = self.options.threadsafe
        cmake.definitions["ENABLE_COLUMN_METADATA"] = self.options.enable_column_metadata
        cmake.definitions["ENABLE_EXPLAIN_COMMENTS"] = self.options.enable_explain_comments
        cmake.definitions["ENABLE_FTS3"] = self.options.enable_fts3
        cmake.definitions["ENABLE_FTS4"] = self.options.enable_fts4
        cmake.definitions["ENABLE_FTS5"] = self.options.enable_fts5
        cmake.definitions["ENABLE_JSON1"] = self.options.enable_json1
        cmake.definitions["ENABLE_RTREE"] = self.options.enable_rtree
        cmake.definitions["OMIT_LOAD_EXTENSION"] = self.options.omit_load_extension
        cmake.definitions["HAVE_FDATASYNC"] = True
        cmake.definitions["HAVE_GMTIME_R"] = True
        cmake.definitions["HAVE_LOCALTIME_R"] = True
        cmake.definitions["HAVE_POSIX_FALLOCATE"] = True
        cmake.definitions["HAVE_STRERROR_R"] = True
        cmake.definitions["HAVE_USLEEP"] = True
        if self.settings.os == "Windows":
            cmake.definitions["HAVE_LOCALTIME_R"] = False
            cmake.definitions["HAVE_POSIX_FALLOCATE"] = False
        if tools.is_apple_os(self.settings.os):
            cmake.definitions["HAVE_POSIX_FALLOCATE"] = False
        if self.settings.os == "Android":
            cmake.definitions["HAVE_POSIX_FALLOCATE"] = False
        if self.options.shared:
            cmake.definitions["BUILD_SHARED_LIBS"] = True
        if self.options.fPIC:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = True
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        header = tools.load(os.path.join(self._source_subfolder, "sqlite3.h"))
        license_content = header[3:header.find("***", 1)]
        tools.save("LICENSE", license_content)

        self.copy("LICENSE", dst="licenses")
        self.copy("FindSQLite3.cmake")

        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Linux":
            if self.options.threadsafe:
                self.cpp_info.libs.append("pthread")
            if self.options.omit_load_extension == "False":
                self.cpp_info.libs.append("dl")
