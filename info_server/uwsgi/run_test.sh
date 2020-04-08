#!/bin/sh
cd `dirname $0`

:>uwsgi_test.log
uwsgi --ini info_test.ini
