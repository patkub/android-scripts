#!/bin/sh
adb root
echo Backing up databases...
adb pull /data/data/com.google.android.apps.authenticator2/databases
echo Done!
