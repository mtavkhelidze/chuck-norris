cmake_minimum_required(VERSION 3.15)

project(chuck-fact)

set(CMAKE_CXX_STANDARD 17)

set(CN_SOURCES src/chuck-fact.cpp src/facts.hpp include/chuck-fact.hpp)

include_directories(include)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(chuck-norris ${CN_SOURCES})

add_executable(chuck-fact src/main.cpp)
target_link_libraries(chuck-fact chuck-norris CONAN_PKG::sqlite3)
