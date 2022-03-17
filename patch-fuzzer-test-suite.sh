#!/bin/sh
set -e

sed -i '/PLEASE USE THIS SCRIPT FROM ANOTHER DIR/s/^/#/g' fuzzer-test-suite/common.sh
sed -i '/TEST=/s/.*/TEST=\$SCRIPT_DIR\/..\/project-scripts\/\$1\/test-\$FUZZING_ENGINE\.sh/g' fuzzer-test-suite/build-and-test.sh
