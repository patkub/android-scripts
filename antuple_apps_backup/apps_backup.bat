@echo off
adb root

REM contacts/call logs
echo Backing up Contacts/Call Logs...
mkdir "data/data/com.android.providers.contacts"
adb pull /data/data/com.android.providers.contacts/databases data/data/com.android.providers.contacts
 
REM messanger
echo Backing up Telephony...
mkdir "data/user_de/0/com.android.providers.telephony/databases"
adb pull /data/user_de/0/com.android.providers.telephony/databases data/user_de/0/com.android.providers.telephony

echo Backing up Messanger...
mkdir "data/data/com.google.android.apps.messaging"
adb pull /data/data/com.google.android.apps.messaging/databases data/data/com.google.android.apps.messaging

echo Done!
pause
