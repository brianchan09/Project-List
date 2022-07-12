#!/bin/bash
if [[ ! -f $1 ]]; then
	echo "Error!! The password list $1 NOT exist."
	echo "Please check and enter a correct path."
	echo "`date +\"%a %b %d %T %Z %Y\"` Missing Password List $1" >> err.log
	exit
fi
if [[ ! -d $2 ]]; then
	echo "Error!! Directory $2 NOT exist."
	echo "Please check and enter a correct directory path."
	echo "`date +\"%a %b %d %T %Z %Y\"` Directory $2 NOT exist" >> err.log
	exit
fi
unlock(){ #$1 password $2 filename $3 output $4 path for store unlocked file
	_pass=0
	common_pwd=`cat $1 | sed "s/.*,//g" | tail -n +2`
	for i in $common_pwd; do
		for (( j = 0; j < 36; j++ )); do
			pwd=`bash shift_encrypt.sh $i $j`
			unzip -qqtP $pwd $2 > /dev/null 2>&1
			if [[ $? -eq 0 ]]; then
				unzip -jqqP $pwd -d $4 $2
				_pass=1
			fi
			if [[ _pass -eq 1 ]]; then
				echo "Password Found for $2 ! Password is $pwd ( WORD is $i and KEY is $j )"
				echo "$2,WORD:$i;KEY:$j;PWD:$pwd" >> $3
				((count++))
				return 0
			fi
		done
	done
	echo "Password not find for $2"
	echo "$2,Not found" >> $3
	((count_fail++))
	return 0
}
# main
count=0
count_fail=0
echo "File,Password" > $3
filename="$(ls $2)"
for i in $filename; do
	if [[ "${i: -4}" == ".zip" ]]; then
		path=$2/$i
		unlock $1 $path $3 $2
	fi
done
total=$(($count+$count_fail))
echo "Result : $count out of $total file found password."
