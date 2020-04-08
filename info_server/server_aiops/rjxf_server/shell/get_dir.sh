#!/bin/sh
cd `dirname $0`

dqdhFlag=$1

#cd $HOME/rjxf/rjxf_tmp
expdir="$HOME/bin"
_ip='163.1.6.10'
_user='doc'
_pass='XXX'
tmp=`expect -f $expdir/run_command.exp "$_ip" "$_user" "$_pass" "cd $dqdhFlag;ls -tl *.tar"`

echo "$tmp"|awk '{print $NF}'|grep '.tar'
