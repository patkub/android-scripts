#!/bin/sh
echo Flashing AdBlock...
adb pull /system/hosts old_hosts
adb push /system/ hosts
