## Depenedencies

* `gcc`
* `clang`
* `libpng-dev`
* `nasm`
* `libarchive-dev`
* `inotify-tools`
* `subversion`
* `libgcrypt20-dev`
* `autoconf-archive`

For data analysis, install [afl-utils](https://gitlab.com/rc0r/afl-utils.git).

## Usage

First clone this repo by the following commands:

```sh
git clone --recurse-submodules https://github.com/DCsunset/fuzzer-test-suite.git
./init.sh
```

For AFL, configure the kernel parameters:

```sh
echo core | sudo tee /proc/sys/kernel/core_pattern
cd /sys/devices/system/cpu
echo performance | sudo tee cpu*/cpufreq/scaling_governor
```

To run one or more projects:

```sh
./test-project.sh <name(s)>
```

The available projects are listed in the variable `AVAIL_PROJ` in file `./config.sh`.

To check log of a projects

```sh
./check-log.sh <name(s)>
# with some flags to command tail
TAIL_FLAGS=-f ./check-log.sh <name>
```

To stop the running projects:

```sh
./kill-all.sh
```

