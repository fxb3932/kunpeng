#!/bin/sh
cd `dirname $0`

python manage.py runserver 0.0.0.0:19096
#python manage.py runserver 0.0.0.0:19090

exit

#����Ŀ
django-admin startproject mysite

python manage.py startapp myApp

#����Ǩ���ļ�
python manage.py makemigrations polls

#�鿴Ǩ�������ִ����ЩSQL���
python manage.py sqlmigrate polls 0001

#ִ��Ǩ��
python manage.py migrate

#��������Ա�˺�
python manage.py createsuperuser

python manage.py collectstatic

