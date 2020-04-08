#!/bin/sh
cd `dirname $0`
export LANG=C

:>uwsgi.log
uwsgi --reload uwsgi.pid
