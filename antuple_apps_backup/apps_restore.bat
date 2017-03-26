@echo off
adb root

REM contacts/call logs
echo Restoring Contacts/Call Logs...
adb push data/data/com.android.providers.contacts/databases /data/data/com.android.providers.contacts/

REM messanger
echo Restoring Telephony...
adb push data/user_de/0/com.android.providers.telephony/databases /data/user_de/0/com.android.providers.telephony/

echo Restoring Messanger...
adb push data/data/com.google.android.apps.messaging/databases /data/data/com.google.android.apps.messaging/

echo Done!
pause
