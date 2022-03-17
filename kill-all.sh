#!/bin/bash
. $(dirname $0)/config.sh

for i in "${AVAIL_PROJ[@]}"; do
	echo Killing $i
	pkill -9 $i
done
