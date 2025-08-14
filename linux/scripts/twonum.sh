#! /bin/bash

# 比较两个数的大小

echo "input two num(use enter):"
read a
read b
if [ $a -eq $b ]
then echo "$a = $b"
elif [ $a -gt $b ]
then echo "$a > $b"
else echo "$a < $b"
fi
