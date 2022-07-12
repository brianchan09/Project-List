#!/bin/bash
pwd_gen(){
	pin=`cat /dev/urandom | tr -dc '0-9' | fold -w $1 | head -n 1`
	echo $pin
}
pwd_gen $1
