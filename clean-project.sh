#!/bin/bash

. $(dirname $0)/config.sh

if [ "$#" -eq 0 ]; then
	echo "Usage: ./clean-project.sh <name>..."
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

	BENCHMARKS="${PARENT_DIR}/RUNDIR-${name}*/"
	for f in $BENCHMARKS
	do
		file_name="$(basename $f)"
		echo "Deleting $file_name from-${file_name#RUNDIR-}.out"
		rm -rf $f rm -rf ${PARENT_DIR}/from-${file_name#RUNDIR-}.out
	done
done

