@echo off
adb root

REM authenticator
echo Backing up Authenticator...
mkdir "data/data/com.google.android.apps.authenticator2/databases"
adb pull /data/data/com.google.android.apps.authenticator2/databases data/data/com.google.android.apps.authenticator2

REM call logs
echo Backing up Call Log...
mkdir "data/data/com.android.providers.contacts/databases"
adb pull /data/data/com.android.providers.contacts/databases/calllog.db data/data/com.android.providers.contacts/databases
adb pull /data/data/com.android.providers.contacts/databases/calllog.db-journal data/data/com.android.providers.contacts/databases

REM messanger
echo Backing up Telephony/Messanger...
mkdir "data/user_de/0/com.android.providers.telephony/databases"
adb pull /data/user_de/0/com.android.providers.telephony/databases data/user_de/0/com.android.providers.telephony
mkdir "data/data/com.google.android.apps.messaging"
adb pull /data/data/com.google.android.apps.messaging/databases data/data/com.google.android.apps.messaging

echo Done!
pause
