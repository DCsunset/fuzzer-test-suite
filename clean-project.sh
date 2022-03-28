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
		echo "Deleting $f"
		rm -rf $f
	done
done

