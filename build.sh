#!/bin/bash

executable="chuck-fact"
build_dir=".build"

mkdir $build_dir 2>/dev/null

(
  cd $build_dir || exit
  if [[ ! -s "conanbuildinfo.cmake" ]]; then
    conan install ../ --build
  fi
  cmake -GNinja ../
  ninja
  cp bin/$executable ../
)
