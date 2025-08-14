#! /bin/bash

# 模拟登录Linux
echo -n "login:"
read name
echo -n "password:"
read passwd
if [ $name = 'd111kc' -a $passwd = '123456' ]
then echo "welcome back, $name"
else echo "your username or password is wrong"
fi