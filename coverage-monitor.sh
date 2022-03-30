#!/bin/bash

# $1: directories to watch
# $2: executable

# pre-execute all seeds
for dir in $1; do
	$2 $dir/*
done

inotifywait -e close_write,moved_to -r -m $1 |
while read -r directory events filename; do
	# run coverage
	seed="$directory$filename"
	echo File change: $seed
	$2 $seed
done
