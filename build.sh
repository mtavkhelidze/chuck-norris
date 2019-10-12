#!/bin/bash

executable="chuck-says"
build_dir=".build"

mkdir $build_dir 2>/dev/null

(
  cd $build_dir || exit
  cmake -GNinja ../
  ninja
  cp $executable ../
)
