#!/bin/bash
x=`./pwd_gen.sh 5`
passcode=HKU$x
password=`echo -n $passcode | sha256sum | head -c 64`
file=$1
zip --password $password $file.zip $file
