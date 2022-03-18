#!/bin/bash
set -e

./patch-fuzzer-test-suite.sh
./patch-libfuzzer.sh
cd AFL && make && cd ..
