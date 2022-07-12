#!/bin/bash
pin=`bash pwd_gen.sh $1`
password=`bash shift_encrypt.sh $pin $2`
zip -rjP $password $3.zip $3
if [[ $? -eq 0 ]]; then
	rm $3
fi
echo "PIN:$pin;KEY:$2;PWD:$password" > $4
