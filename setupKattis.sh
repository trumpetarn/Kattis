#!/bin/bash
# This script is to large parts copied from https://github.com/chixulub/kattis/blob/master/kattis.sh

function set_language {
	if [ $# -lt 1 ]; then
		echo "Error: set_language needs 1 argument"
		return -1
	fi

	case $1 in
	"py")
		lang="py"
	;;
	"python")
		lang="py"
	;;	
	"c++")
		lang="cpp"
		;;
	"cpp")
		lang="cpp"
	;;
	"c")
		lang="c"
	;;
	*)
		echo "Error: $1 is not a supported language"
		if [[ $lang == "" ]]; then
			echo "No language set"	
		else
			echo "Keeping $lang"
		fi
		return -1
	esac
	echo "New language in $lang"
}

function init_problem {
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
		subl $problem/$problem.py
	fi

	currentProblem=$problem
}

function run_tests {
	echo "Running tests for $currentProblem"
	problem=$currentProblem

	pushd $problem
	retCode=0
	for n in samples/*.in; do
		echo "Running sample $n ..."
		cat $n | ./$problem.py > samples/`basename $n .in`.out
		diff samples/`basename $n .in`.out samples/`basename $n .in`.ans
		if [ $? -eq 0 ]; then
			echo "All tests passed!"
		else
			echo "Something seems wrong!"
			retCode=$((retCode+1))
		fi
	done
	popd
	if [ $retCode -eq 0 ]; then
		printf "\n***** PASSED *****\n\n"
	else
		printf "\n***** Failed ($retCode) *****\n\n"
	fi
	return $retCode
}

function change_problem {
	if [ $# -lt 1 ]; then
		echo "Error: Init problem needs 1 argument"
		return -1
	fi
	echo "Active problem was $currentProblem"
	currentProblem=$1
	echo "New active problem is $currentProblem"
}

function active_kattis {
	if [ -z ${currentProblem+x} ]; then 
		echo "ERROR: Current problem is unset"
	else 
		echo "Current Problem is $currentProblem"
	fi
}

function debug {
	pattern="$currentProblem/samples/*.in"
	files=( $pattern )
	python2 $currentProblem/$currentProblem.py < ${files[0]}
}

function submit_problem {
	echo "Submitting problem $currentProblem after testing"
	run_tests
	if [ $? -eq 0 ]; then
		python submit.py -p $currentProblem $currentProblem/$currentProblem.py -l "Python 2"
	else
		echo "Aborting submit due to failed tests"
	fi
}