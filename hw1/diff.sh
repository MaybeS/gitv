#!/bin/bash

argc=$#
file_pattern=$1
grep_pattern=$2

root_path=$(git rev-parse --show-toplevel)
mygitv="python $root_path/hw1/gitv.py findgrep $file_pattern $grep_pattern" 
tsgitv="$root_path/gitv findgrep $file_pattern $grep_pattern"

if [ 2 -eq $argc ]; then
	echo "::: my gitv findgrep result for $grep_pattern in $file_pattern save to 'result_my'"
	$mygitv > result_my
	echo "::: taesoo gitv findgrep result for $grep_pattern in $file_pattern save to 'result_ts'"
	$tsgitv > result_ts
	echo "::: diff with my and taeesoo"
	diff my ts
	echo "::: done diff with my and taeesoo gitv findgrep"
else
	echo "must input argument [file_pattern] [grep_pattern]"
fi
