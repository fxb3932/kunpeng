#!/bin/sh
cd `dirname $0`
menuUpdateFile=/yycx/menuadd/menu.txt
menuBakFile=/yycx/menuadd/menu.txt.`date +%Y%m%d`
if [ ! -f $menuBakFile ];then
  cp $menuUpdateFile $menuBakFile
  [ $? -eq 0 ] && suc="�ɹ�" || suc='ʧ��'
  echo "menu.txt ����$suc"
else
  echo "[$menuBakFile]�Ѵ��ڣ����豸��"
fi

count_1=$(ls -trl $menuUpdateFile | awk '{print $5}')
cp menu.txt $menuUpdateFile
count_2=$(ls -trl $menuUpdateFile | awk '{print $5}')
[ $? -eq 0 ] && suc="�ɹ�" || suc='ʧ��'
echo "menu.txt ����$suc, �ļ���С [$count_1] --> [$count_2]"

cd /yycx/menuadd
sh menuadd.sh topywk menu.txt
[ $? -eq 0 ] && suc="�ѵ���ִ��" || suc='����ִ���쳣'
echo "menuadd.sh $suc"
