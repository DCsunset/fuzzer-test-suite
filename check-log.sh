#!/bin/bash
set -e

. $(dirname $0)/config.sh
cd fuzzer-test-suite

if [ "$#" -eq 0 ]; then
	echo "Usage: ./check-log.sh <name>"
	exit 1
fi

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

	BENCHMARKS="${PARENT_DIR}/from-${name}*/"
	for f in $BENCHMARKS
	do
		file_name="$(basename $f)"
		echo "Checking log $file_name"
		tail -f $file_name 
	done
done
