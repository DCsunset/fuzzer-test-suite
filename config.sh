AVAIL_PROJ=(boringssl c-ares freetype2 guetzli harfbuzz json lcms libarchive libjpeg libpng libssh libxml2 llvm-libcxxabi openssl-1.0.1f openssl-1.1.0c pcre2 proj4 re2 sqlite vorbis woff2)

BASEDIR=$(readlink -f $(dirname $0))
PARENT_DIR="$BASEDIR/RUN_EXPERIMENT"

export FUZZING_ENGINE="afl"
export AFL_SRC=$BASEDIR/AFL

