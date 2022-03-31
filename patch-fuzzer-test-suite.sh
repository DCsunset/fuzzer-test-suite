#!/bin/sh
set -e

sed -i '/PLEASE USE THIS SCRIPT FROM ANOTHER DIR/s/^/#/g' fuzzer-test-suite/common.sh
sed -i '/TEST=/s/.*/TEST=\$SCRIPT_DIR\/..\/project-scripts\/\$1\/test-\$FUZZING_ENGINE\.sh/g' fuzzer-test-suite/build-and-test.sh
sed -i '/^cd \$RUNDIR/s/$/\nFUZZING_ENGINE=coverage CFLAGS="$GCOV_FLAGS" CXXFLAGS="$GCOV_FLAGS" CC=gcc CXX=g++ $BUILD/g' fuzzer-test-suite/build-and-test.sh
