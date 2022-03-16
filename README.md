## Requirements

* `clang`

## Usage

First clone this repo by the following commands:

```sh
git clone --recurse-submodules https://github.com/DCsunset/fuzzer-test-suite.git
./patch-fuzzer-test-suite.sh
```

To run one or more projects:

```sh
./test-project.sh <name(s)>
```

The available projects are listed in the variable `AVAIL_PROJ` in file `./config.sh`.

To stop the running projects:

```sh
./kill-all.sh
```

