#!/bin/sh
cd `dirname $0`
export LANG=C

:>uwsgi.log
#name=$(pwd | awk -F'/' '{print $(NF-1)}')
name="info_server"
uwsgi -d uwsgi.log ${name}.ini

exit
uwsgi -d test.log info_test.ini
uwsgi -d test_yh.log info_yh.ini
