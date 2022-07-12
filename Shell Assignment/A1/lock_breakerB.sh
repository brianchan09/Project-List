#!/bin/bash
_pass=0
common_pwd=`cat $1 | sed "s/.*,//g" | tail -n +2`
name=$2
path=`echo $2 | sed "s/${name##*\/}//g"`
for i in $common_pwd; do
	for (( j = 0; j < 36; j++ )); do
		pwd=`bash shift_encrypt.sh $i $j`
		unzip -qqtP $pwd $2 > /dev/null 2>&1
		if [[ $? -eq 0 ]]; then
			unzip -jqqP $pwd -d $path $2
			_pass=1
		fi
		if [[ _pass -eq 1 ]]; then
			echo "Password Found! Zip Password is $pwd ( WORD is $i and KEY is $j )"
			echo "WORD:$i,KEY:$j,PWD:$pwd" > $3
			exit
		fi
	done
done
echo "Password not find."
