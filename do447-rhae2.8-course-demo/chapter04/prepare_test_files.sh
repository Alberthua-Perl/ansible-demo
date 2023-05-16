#!/bin/bash

for i in {a..c}; do
	for NUM in {1..3}; do 
		touch files/app_${i}_tmp_file${NUM}.txt
	done
done
