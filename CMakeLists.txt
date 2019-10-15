cmake_minimum_required(VERSION 3.15)

project(chuck-fact)

set(CMAKE_CXX_STANDARD 17)

set(CN_SOURCES
    src/chuck-fact.cpp
    src/cwrapper.cpp
    src/facts.hpp
    include/chuck-fact.hpp
    include/chuck-fact.h
    )

include_directories(include)
set(BUILD_SHARED_LIBS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(chuck-norris ${CN_SOURCES})
target_link_libraries(chuck-norris CONAN_PKG::sqlite3)

add_executable(chuck-fact src/main.cpp)
target_link_libraries(chuck-fact chuck-norris)
set_target_properties(chuck-fact PROPERTIES LINK_FLAGS "-Wl,-rpath,.build/lib")

add_executable(chuck-fact-c src/main.c)
target_link_libraries(chuck-fact-c chuck-norris)
set_target_properties(chuck-fact-c PROPERTIES LINK_FLAGS "-Wl,-rpath,.build/lib")
