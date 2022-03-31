sed -i '/^\$CXX/s/.*/$CXX $CXXFLAGS sqlite3.o ossfuzz.o $LIB_FUZZING_ENGINE -ldl -pthread \\/g' fuzzer-test-suite/sqlite-2016-11-14/build.sh
