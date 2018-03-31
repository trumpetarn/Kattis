#!/bin/bash

if [ $# -lt 1 ]; then
	echo "Error: run_tests needs 1 argument"
	return -1
fi

problem=$1

pushd $problem

for n in samples/*.in; do
	echo "Running sample $n ..."
	cat $n | ./$problem.py > samples/`basename $n .in`.out
	diff samples/`basename $n .in`.out samples/`basename $n .in`.ans
	if [ $? -eq 0 ]; then
		echo "All tests passed!"
	else
		echo "Something seems wrong!"
	fi
done
echo "Done."