gcc central.c -o central
gcc external.c -o external
./external 100 1 &
./external 22 2 &
./external 50 3 &
./external 40 4 &
./central 60 &
