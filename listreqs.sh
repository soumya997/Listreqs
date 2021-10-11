#!/usr/bin/env bash

if [ -n "$1" ];
then
	file=$1
else
	read -p "Enter the requirements file name : " file
	if [ -z "$file" ];
	then
		file="requirements.txt"
	fi

fi

touch $file
pip list > $file

sed -i '1,2d' $file
sed -i 's/ \{1,\}/ /g' $file
sed -i 's/\ /==/g' $file
