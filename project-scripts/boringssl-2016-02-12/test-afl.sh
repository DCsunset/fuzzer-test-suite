#!/bin/bash
. $(dirname $0)/../../fuzzer-test-suite/common.sh

set -x
rm -rf $CORPUS
mkdir $CORPUS

# Master
[ -e $EXECUTABLE_NAME_BASE ] && $AFL_SRC/afl-fuzz -m 800 -i seeds -o $CORPUS -M fuzzer1 ./$EXECUTABLE_NAME_BASE &> fuzzer1.log &
for i in $(seq 2 $JOBS); do
	# secondary
	[ -e $EXECUTABLE_NAME_BASE ] && $AFL_SRC/afl-fuzz -m 800 -i seeds -o $CORPUS -S fuzzer$i ./$EXECUTABLE_NAME_BASE &> fuzzer$i.log &
done
