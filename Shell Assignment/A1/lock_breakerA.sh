#!/bin/bash
end=`cat /dev/urandom | tr -dc '9' | fold -w $1 | head -n 1`
answer=$1
_pass=0
name=`echo $2 | sed 's/.*\///g'`
path=`echo $2 | sed "s/${name}//g"`
for (( i = 0; i <= $end; i++ )); do
	k=`printf "%0${answer}d\n" $i`
	for (( j = 0; j < 36; j++ )); do
		pwd=`./shift_encrypt.sh $k $j`
		unzip -qqtP $pwd $2 > /dev/null 2>&1
		if [[ $? -eq 0 ]]; then
			unzip -jqqd $path -P $pwd $2
			_pass=1
		fi
		if [[ _pass -eq 1 ]]; then
			echo "Password Found! Zip Password is $pwd ( PIN is $k and KEY is $j )"
			echo "PIN:$k,KEY:$j,PWD:$pwd" > $3
			exit
		fi
	done
done
echo "Password not find."
