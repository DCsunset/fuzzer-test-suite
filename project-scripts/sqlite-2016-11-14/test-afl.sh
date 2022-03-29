#!/bin/bash
. $(dirname $0)/../../fuzzer-test-suite/common.sh

if [ "FUZZING_ENGINE" == "coverage" ]; then
	exit 0
fi

set -x
rm -rf $CORPUS
mkdir $CORPUS

# create an initial seed
mkdir seeds
echo 1 > seeds/seed

# Master
[ -e $EXECUTABLE_NAME_BASE ] && $AFL_SRC/afl-fuzz -m 800 -i seeds -x $ORIGINAL_SCRIPT_DIR/sql.dict -o $CORPUS -M fuzzer1 ./$EXECUTABLE_NAME_BASE @@ &> fuzzer1.log &
for i in $(seq 2 $JOBS); do
	# secondary
	[ -e $EXECUTABLE_NAME_BASE ] && $AFL_SRC/afl-fuzz -m 800 -i seeds -x $ORIGINAL_SCRIPT_DIR/sql.dict -o $CORPUS -S fuzzer$i ./$EXECUTABLE_NAME_BASE @@ &> fuzzer$i.log &
done
