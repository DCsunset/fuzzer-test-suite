#!/bin/sh
set -e

sudo apt install -y gcc clang libpng-dev libarchive-dev inotify-tools
cd ../afl-utils && sudo python3 setup.py install

echo core | sudo tee /proc/sys/kernel/core_pattern
cd /sys/devices/system/cpu
echo performance | sudo tee cpu*/cpufreq/scaling_governor
