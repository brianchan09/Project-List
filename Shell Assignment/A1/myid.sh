#!/bin/bash
myid(){
	if [ "$1" = "id" ]
	then
		echo "20117292"
	elif [ "$1" = "name" ]
		then 
			echo "Chan Chun Ho"
	fi
}
myid $1