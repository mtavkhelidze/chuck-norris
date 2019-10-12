cmake_minimum_required(VERSION 3.15)

project(chuck-norris)

set(CMAKE_CXX_STANDARD 17)

set(CN_SOURCES src/chuck-norris.cpp include/chuck-norris.hpp)

include_directories(include)

add_library(chuck-norris ${CN_SOURCES})

add_executable(chuck-says src/main.cpp)
target_link_libraries(chuck-says chuck-norris)
