#!/bin/sh
adb pull /system/hosts old_hosts
adb push /system/ hosts
