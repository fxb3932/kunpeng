#!/bin/sh

file_pwd=$1

cd $1
echo "该版本目录下未找到安装说明！" > readme.txt
cp 安装说明 readme.txt
