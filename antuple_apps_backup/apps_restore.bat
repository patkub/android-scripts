@echo off
adb root

REM authenticator
echo Restoring authenticator...
adb push data/data/com.google.android.apps.authenticator2/databases /data/data/com.google.android.apps.authenticator2/

REM call logs
echo Restoring Call Log...
adb push data/data/com.android.providers.contacts/databases/calllog.db /data/data/com.android.providers.contacts/databases/
adb push data/data/com.android.providers.contacts/databases/calllog.db-journal /data/data/com.android.providers.contacts/databases/

REM messanger
echo Restoring Telephony/Messanger...
adb push data/user_de/0/com.android.providers.telephony/databases /data/user_de/0/com.android.providers.telephony/
adb push data/data/com.google.android.apps.messaging/databases /data/data/com.google.android.apps.messaging/

echo Done!
pause
