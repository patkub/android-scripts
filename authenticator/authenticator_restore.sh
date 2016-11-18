#!/bin/sh
adb root
echo Restoring databases...
adb push databases/databases /data/data/com.google.android.apps.authenticator2/databases/
echo Restoring databases journal...
adb push databases/databases-journal /data/data/com.google.android.apps.authenticator2/databases/
echo Done!
