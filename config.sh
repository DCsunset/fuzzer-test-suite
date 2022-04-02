AVAIL_PROJ=(boringssl c-ares freetype2 guetzli harfbuzz json lcms libarchive libjpeg libpng libssh libxml2 llvm-libcxxabi openssl-1.0.1f openssl-1.1.0c pcre2 proj4 re2 sqlite vorbis woff2)

BASEDIR=$(readlink -f $(dirname $0))
PARENT_DIR="$BASEDIR/RUN_EXPERIMENT"

export FUZZING_ENGINE="afl"
export AFL_SRC=$BASEDIR/AFL

# disable ASAN for afl
export FUZZ_FLAGS="-O2 -fno-omit-frame-pointer -gline-tables-only -fsanitize-coverage=trace-pc-guard,trace-cmp,trace-gep,trace-div"
# using gcov
export GCOV_FLAGS="-O0 --coverage"
export GCOV_LDFLAGS="--coverage"
