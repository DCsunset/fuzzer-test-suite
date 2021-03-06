#!/bin/bash
# Copyright 2017 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
set -e

. $(dirname $0)/config.sh
cd fuzzer-test-suite

. $(dirname $0)/common.sh

if [ "$#" -eq 0 ]; then
	echo "Usage: ./test-project.sh <name>..."
	exit 1
fi

#[[ -e "$PARENT_DIR" ]] && echo "Rename folder $PARENT_DIR to avoid deletion" && exit 1
mkdir -p $PARENT_DIR

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
		export ORIGINAL_SCRIPT_DIR="${ABS_SCRIPT_DIR}/${file_name}"
		(cd $PARENT_DIR && ${ABS_SCRIPT_DIR}/build-and-test.sh "${file_name}" > from-${file_name}.out 2>&1  &) # && sleep 10
	done
done

