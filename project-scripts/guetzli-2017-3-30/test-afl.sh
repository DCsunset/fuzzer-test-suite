#!/bin/bash
. $(dirname $0)/../../fuzzer-test-suite/common.sh

set -x
rm -rf $CORPUS
mkdir $CORPUS

EXECUTABLE_NAME_COVERAGE=$(basename $SCRIPT_DIR)-coverage

seed_dirs="$CORPUS/fuzzer1/queue"
# Master
[ -e $EXECUTABLE_NAME_BASE ] && $AFL_SRC/afl-fuzz -m 800 -i $SCRIPT_DIR/seeds -x $SCRIPT_DIR/jpeg.dict -o $CORPUS -M fuzzer1 ./$EXECUTABLE_NAME_BASE @@ &> fuzzer1.log &
for i in $(seq 2 $JOBS); do
	# secondary
	seed_dirs="$seed_dirs $CORPUS/fuzzer$i/queue"
	[ -e $EXECUTABLE_NAME_BASE ] && $AFL_SRC/afl-fuzz -m 800 -i $SCRIPT_DIR/seeds -x $SCRIPT_DIR/jpeg.dict -o $CORPUS -S fuzzer$i ./$EXECUTABLE_NAME_BASE @@ &> fuzzer$i.log &
done

sleep 10
# Monitor and execute seeds to get coverage
$(dirname $0)/../../coverage-monitor.sh "$seed_dirs" ./$EXECUTABLE_NAME_COVERAGE &> coverage-monitor.log &
