#!/bin/bash

# $1: directories to watch
# $2: executable

inotifywait -e close_write,moved_to -r -m $1 |
while read -r directory events filename; do
	# run coverage
	seed="$directory$filename"
	echo File change: $seed
	$2 $seed
done
