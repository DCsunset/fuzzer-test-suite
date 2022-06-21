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

## License

AGPL-3.0 License.

Full notice:

    Copyright (C) 2022 DCsunset, lyuyues, xuyeliu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
