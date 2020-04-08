#!/bin/sh
cd `dirname $0`


expdir="$HOME/bin"
_ip='163.1.6.10'
_user='doc'
#_pass='haohaobaomi123'
expect -f $expdir/scp_get.exp "$_ip" "$_user" "$_pass" "$1" "$HOME/rjxf/rjxf_tmp"
