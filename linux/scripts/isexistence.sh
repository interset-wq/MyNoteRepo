#! /bin/bash

# 判断文件是否存在
echo "input a file name:"
read file
if [ -e $file ]
then echo "$file is exist"
else echo "$file is not exist"
fi