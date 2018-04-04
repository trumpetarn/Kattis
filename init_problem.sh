#!/bin/bash
# This script is to large parts copied from https://github.com/chixulub/kattis/blob/master/kattis.sh


function testing {
	if false; then
		if [ $# -lt 1 ]; then
			echo "Error: Init problem needs 1 argument"
			return -1
		fi

		problem=$1

		mkdir $problem
		pushd $problem
		wget https://open.kattis.com/problems/$problem/file/statement/samples.zip

		if [ $? -ne 0 ]; then
			echo "Error: \"$problem\" does not seem to be a valid kattis problem."
			popd
			rm -rf $problem
			return -1
		else
			cp ../.templates/TEMPLATE.py $problem.py
			#cp ../.kattis/TEMPLATE.cpp $problem.cpp
			#cp ../.kattis/TEMPLATE.c $problem.c

			unzip -d samples samples.zip
			rm -f samples.zip
			popd
			/opt/sublime_text/sublime_text $problem/$problem.py
		fi
	else
		echo "Hej"
	fi
}