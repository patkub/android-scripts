#!/sbin/sh
#
# Pure Nexus Custom Settings
#

echo Applying custom Pure Nexus settings...

# Quicksettings
settings put system qs_layout_columns 3
settings put system qs_rows_landscape 2
settings put system qs_rows_portrait 3
settings put system qs_tile_title_visibility 1
settings put system quick_settings_vibrate 1
settings put secure lockscreen_qs_disabled 0
settings put secure qs_easy_toggle 1
settings put secure qs_show_brightness 1

# Double tap to sleep
settings put system double_tap_sleep_anywhere 1
settings put system double_tap_sleep_gesture 1
settings put system double_tap_sleep_navbar 1

# Kill back button
settings put secure kill_app_longpress_back 1
settings put system long_press_kill_delay 1000

# Powermenu
settings put global power_menu_actions "power|reboot|screenshot|screenrecord|silent"

# Lockscreen torch
settings put system keyguard_toggle_torch 1

# Media cover art
settings put system lockscreen_media_metadata 1

# Scramble layout
settings put system lockscreen_scramble_pin_layout 0

# Lockscreen pin ripple
settings put system lockscreen_pin_ripple 1

# Battery
settings put secure status_bar_battery_style 2
settings put secure status_bar_battery_style_tile 1
settings put secure status_bar_show_battery_percent 1

# Network traffic
settings put system network_traffic_autohide_threshold 10
settings put system network_traffic_state 3

# Notification count
settings put system status_bar_notif_count 0

# Statusbar
settings put system status_bar_brightness_control 1
settings put system status_bar_show_carrier 0
settings put system statusbar_clock_am_pm_style 2
settings put system statusbar_clock_date_display 2
settings put system statusbar_clock_date_format "MMM dd"

# Bluetooth battery status
settings put system bluetooth_show_battery 0

# PowerMenu secure lockscreen
settings put system lockscreen_enable_power_menu 1

# Volume rocker
settings put system volbtn_music_controls 1
settings put system volume_key_cursor_control 2
settings put system volume_keys_control_media_stream 0
settings put system volume_wake_screen 1
settings put system swap_volume_buttons 1

# Clear-all recents
settings put system show_clear_all_recents 1
settings put system three_finger_gesture 1
settings put system toast_icon 1

# Vibrate
settings put system vibrate_on_callwaiting 1
settings put system vibrate_on_connect 1
settings put system vibrate_on_disconnect 1
settings put system vibrate_when_ringing 0

# Custom header
settings put system status_bar_custom_header 1
settings put system status_bar_custom_header_image org.omnirom.omnistyle/poly_sunset
settings put system status_bar_custom_header_provider static
settings put system status_bar_custom_header_shadow 80
settings put system status_bar_daylight_header_pack org.omnirom.omnistyle/org.omnirom.omnistyle.poly

echo Done!

