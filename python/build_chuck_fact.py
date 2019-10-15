#!/usr/bin/env python3

from cffi import FFI
import json
import path

ffi_builder = FFI()

libs = ["../.build/lib/libchuck-norris.a"]
includes = ["../include"]

conan_info = json.loads(path.Path("../.build/conanbuildinfo.json").text())
for dep in conan_info["dependencies"]:
    for lib_name in dep["libs"]:
        lib_file = "lib{}.a".format(lib_name)
        for lib_path in dep["lib_paths"]:
            candidate = path.Path(lib_path).joinpath(lib_file)
            if candidate.exists():
                libs.append(candidate)
            else:
                libs.append(lib_name)

    for include_path in dep["include_paths"]:
        includes.append(include_path)

print(libs)
print(includes)

ffi_builder.set_source(
    "_chuck_fact",
    """
    #include <chuck-fact.h>
    """,
    extra_objects=libs,
    include_dirs=includes,
    libraries=["stdc++"],
)

ffi_builder.cdef(
    """
    typedef struct chuck_fact chuck_fact_t;
    chuck_fact_t* chuck_fact_init(void);
    const char* chuck_fact_get(chuck_fact_t*);
    void chuck_fact_destroy(chuck_fact_t*);
    """
)
