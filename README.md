## Depenedencies

* `clang`
* `libpng`
* `libarchive-dev`

## Usage

First clone this repo by the following commands:

```sh
git clone --recurse-submodules https://github.com/DCsunset/fuzzer-test-suite.git
./patch-fuzzer-test-suite.sh
./patch-libfuzzer.sh
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

