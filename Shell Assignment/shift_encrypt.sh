#!/bin/bash
shift_encrypt(){
	encode=`printf $1 | od -A n -t d1`
	tmp=""
	maxtime=$(($2 % 36))
	for i in $encode; do
		k=$i
		for (( j = 1; j <= $maxtime; j++ )); do
			k=$(($k+1))
			if [[ k -eq 123 ]]; then
				k=48
			elif [[ k -eq 58 ]]; then
				k=97
			fi
		done
		tmp="$tmp $k"
	done
	decode=""
	for i in $tmp; do
		code=`awk -v char=$i 'BEGIN { printf "%c\n", char;exit } '`
		decode="$decode$code"
	done
	echo $decode
}
shift_encrypt $1 $2