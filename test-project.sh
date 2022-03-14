#!/bin/bash
# Copyright 2017 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
set -e

BASEDIR=$(readlink -f $(dirname $0))
cd fuzzer-test-suite

export FUZZING_ENGINE="afl"
. $(dirname $0)/common.sh

AVAIL_PROJ=(boringssl c-ares freetype2 guetzli)

if [ "$#" -eq 0 ]; then
	echo "Usage: ./test-project.sh <name>"
	exit 1
fi

PARENT_DIR="$BASEDIR/RUN_EXPERIMENT"
#[[ -e "$PARENT_DIR" ]] && echo "Rename folder $PARENT_DIR to avoid deletion" && exit 1
rm -rf $PARENT_DIR
mkdir $PARENT_DIR
echo "Created top directory $PARENT_DIR"

ABS_SCRIPT_DIR=$(readlink -f $SCRIPT_DIR)

for name in $@; do
	found=0
	for i in "${AVAIL_PROJ[@]}"; do
		if [ "$i" == "$name" ]; then
			found=1
			break
		fi
	done
	if [ "$found" -eq 0 ]; then
		echo "Project $name not available"
		exit 1
	fi

	BENCHMARKS="${ABS_SCRIPT_DIR}/${name}*/"
	for f in $BENCHMARKS
	do
		file_name="$(basename $f)"
		[[ ! -d $f ]] && continue # echo "${file_name} isn't a directory" && continue
		[[ ! -e ${f}build.sh ]] && continue # echo "${file_name} has no build script" && continue
		echo "Running build_and_test $file_name"
		(cd $PARENT_DIR && ${ABS_SCRIPT_DIR}/build-and-test.sh "${file_name}" > from-${file_name}.out 2>&1  &) # && sleep 10
	done
done

