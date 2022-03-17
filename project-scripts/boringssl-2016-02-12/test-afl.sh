#!/bin/bash
# Copyright 2016 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
. $(dirname $0)/../../fuzzer-test-suite/common.sh

# Note: this target contains unbalanced malloc/free (malloc is called
# in one invocation, free is called in another invocation).
# and so libFuzzer's -detect_leaks should be disabled for better speed.
export ASAN_OPTIONS=detect_leaks=0:quarantine_size_mb=50

set -x
rm -rf $CORPUS fuzz-*.log
mkdir $CORPUS
[ -e $EXECUTABLE_NAME_BASE ] && $AFL_SRC/afl-fuzz -i seeds -o $CORPUS ./$EXECUTABLE_NAME_BASE -N$JOBS
