#!/sbin/sh
#
# Enable freeform windows
#

cd /system/etc/permissions
sed -e "s/live_wallpaper/freeform_window_management/" android.software.live_wallpaper.xml >freeform.xml
exit 0
