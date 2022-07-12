#!/bin/bash
# Student Name : XXXXX XXXXX XXXXXX 
# Student ID : XXXXXXXX
# Class : CCIT 4052 CL0X 
# Last Update : 2020-XX-XX XX:XX
# ------------------
# Complete the script below 
# you may add .py files and .sh files, make sure you submit them as well 

cve_list=$1
html_output=$2

echo -n "" > $2 
# html contents generation
# add scripts here .... 

for item in `cat $1`
do
    vul_num=`echo $item | cut -d, -f1`
    cvss_vector=`echo $item | cut -d, -f2`
    
    # Integrate with python lib to get CVSS score and rating
    # add scripts here .... 
    # 

    # Output information HTML format
    # add scripts here .... 
    # 

done

# html contents generation
# add scripts here .... 

echo "CVSS scores and ratings outputed to HTML files $2"

