#!/bin/sh
echo Concatenating hosts...
python hosts_concat.py sources.txt
echo Flashing AdBlock...
adb root
adb pull /system/etc/hosts old_hosts
adb push hosts /system/etc
