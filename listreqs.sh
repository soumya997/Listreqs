#!/usr/bin/env bash

if [ -n "$1" ];
then
	file=$1
else
	read -p "Enter the requirements file name : " file
	if [ -z "$file" ];
	then
		touch requirements.txt
		pip list > requirements.txt
		file="requirements.txt"
	fi

fi

sed -i '1,2d' $file
sed -i 's/ \{2,\}/ /g' $file
sed -i 's/\ /==/g' $file
