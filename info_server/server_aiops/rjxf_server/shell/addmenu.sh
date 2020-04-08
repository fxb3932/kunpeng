#!/bin/sh
cd `dirname $0`
menuUpdateFile=/yycx/menuadd/menu.txt
menuBakFile=/yycx/menuadd/menu.txt.`date +%Y%m%d`
if [ ! -f $menuBakFile ];then
  cp $menuUpdateFile $menuBakFile
  [ $? -eq 0 ] && suc="成功" || suc='失败'
  echo "menu.txt 备份$suc"
else
  echo "[$menuBakFile]已存在，无需备份"
fi

count_1=$(ls -trl $menuUpdateFile | awk '{print $5}')
cp menu.txt $menuUpdateFile
count_2=$(ls -trl $menuUpdateFile | awk '{print $5}')
[ $? -eq 0 ] && suc="成功" || suc='失败'
echo "menu.txt 更新$suc, 文件大小 [$count_1] --> [$count_2]"

cd /yycx/menuadd
sh menuadd.sh topywk menu.txt
[ $? -eq 0 ] && suc="已调用执行" || suc='调用执行异常'
echo "menuadd.sh $suc"
