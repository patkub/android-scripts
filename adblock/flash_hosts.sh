#!/bin/sh
echo Flashing AdBlock...
adb pull /system/etc/hosts old_hosts
adb push hosts /system/etc
