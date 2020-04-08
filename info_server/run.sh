#!/bin/sh
cd `dirname $0`

python manage.py runserver 0.0.0.0:19096
#python manage.py runserver 0.0.0.0:19090

exit

#建项目
django-admin startproject mysite

python manage.py startapp myApp

#生成迁移文件
python manage.py makemigrations polls

#查看迁移命令会执行哪些SQL语句
python manage.py sqlmigrate polls 0001

#执行迁移
python manage.py migrate

#创建管理员账号
python manage.py createsuperuser

python manage.py collectstatic