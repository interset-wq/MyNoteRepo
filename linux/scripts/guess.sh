#! /bin/bash

# 猜数字游戏
# 随机生成一个1-100之间的数字
# 让用户输入一个数字
# 比较两个数字的大小
# 如果用户输入的数字大于随机生成的数字，提示用户输入的数字大了
# 如果用户输入的数字小于随机生成的数字，提示用户输入的数字小了
# 如果用户输入的数字等于随机生成的数字，提示用户猜对了
# 并输出用户猜的次数

num=$((RANDOM%100+1))
count=0
while true
do
    echo "input a num(1-100):"
    read guess
    let count++
    if [ $guess -eq $num ]
    then echo "you guess right, the num is $num"
        echo "you guess $count times"
        break
    elif [ $guess -gt $num ]
    then echo "your guess is bigger than the num"
    else echo "your guess is smaller than the num"
    fi
done
