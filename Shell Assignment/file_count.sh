#!/bin/bash
file_count(){
	find $1 -maxdepth 1 -type f | wc -l
}
file_count $1