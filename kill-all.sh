#!/bin/bash
set -e

. $(dirname $0)/config.sh

for i in "${AVAIL_PROJ[@]}"; do
	pkill $i
done
