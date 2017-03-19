#!/sbin/sh
#
# Pure Nexus Custom Settings
#

#
# Lockscreen
#

# Lockscreen clock
settings put system show_lockscreen_clock 1

# Lockscreen font: Roboto Light (default)
settings put system lock_clock_fonts 4

# Lockscreen date
settings put system show_lockscreen_date 1

# Lockscreen alarm text
settings put system show_lockscreen_alarm 1

# Lockscreen torch
settings put system keyguard_toggle_torch 1

# Media cover art
settings put system lockscreen_media_metadata 1

# Scramble pin layout
settings put system lockscreen_scramble_pin_layout 0

# Lockscreen pin ripple
settings put system lockscreen_pin_ripple 1


#
# Notification drawer
#

# Quick pulldown
settings put system status_bar_quick_qs_pulldown 1

# Smart pulldown
settings put system qs_smart_pulldown 0

# Force expanded notification
settings put system force_expanded_notifications 0


#
# Quick Settings
#

# Advance Quick Settings easy toggle
settings put secure qs_easy_toggle 1

# Brightness slider
settings put secure qs_show_brightness 1

# Vibrate on touch
settings put system quick_settings_vibrate 1

# Disable quick settings
settings put secure lockscreen_qs_disabled 0

# Quick settings titles
settings put system qs_tile_title_visibility 1

# Quick settings number of tiles in column
settings put system qs_layout_columns 3

# Quick settings number of rows (portrait)
settings put system qs_rows_portrait 3

# Quick settings number of rows (landscape)
settings put system qs_rows_landscape 2

# Custom header
settings put system status_bar_custom_header 1
settings put system status_bar_custom_header_image org.omnirom.omnistyle/poly_sunset
settings put system status_bar_custom_header_provider static
settings put system status_bar_custom_header_shadow 80
settings put system status_bar_daylight_header_pack org.omnirom.omnistyle/org.omnirom.omnistyle.poly


#
# Recent apps
#

# Immersive Recents (Default)
settings put system immersive_recents 0

# Clear all FAB
settings put system show_clear_all_recents 1

# Clear all FAB location (bottom right)
settings put system recents_clear_all_location 3


#
# Statusbar
#

# Battery settings

# Battery style (circle)
settings put secure status_bar_battery_style 2

# Show battery percentage (inside the icon)
settings put secure status_bar_show_battery_percent 1

# Battery tile style
settings put secure status_bar_battery_style_tile 1

# Battery bar location (hidden)
settings put system battery_bar_location 0


# Carrier label (disabled)
settings put system status_bar_show_carrier 0

# Custom carrier label (currently not set)
settings put system custom_carrier_label ""

# Show clock and date
settings put system status_bar_clock 1

# Show seconds
settings put system status_bar_clock_seconds 0

# Alignment (right clock)
settings put system statusbar_clock_style 0

# AM/PM
settings put system statusbar_clock_am_pm_style 2

# Date (normal)
settings put system statusbar_clock_date_display 2

# Date style (normal)
settings put system statusbar_clock_date_format "MMM dd"

# Date position (left of time)
settings put system statusbar_clock_date_position 0

# Date format
settings put system statusbar_clock_date_format "EEE"


# Network traffic state
settings put system network_traffic_state 65536003

# Hide arrows
settings put system network_traffic_hidearrow 0

# Auto hide
settings put system network_traffic_autohide 0

# Inactivity threshold
settings put system network_traffic_autohide_threshold 10


# Brightness control
settings put system status_bar_brightness_control 1

# Show notification count
settings put system status_bar_notif_count 0

# Show Bluetooth battery status
settings put system bluetooth_show_battery 0


#
# Navigation bar
#

# Enable navigation bar options
settings put system navigation_bar_show 1

# Pixel navbar animation
settings put system pixel_nav_animation 1

# Kill back button
settings put secure kill_app_longpress_back 1
settings put system long_press_kill_delay 1000

# Navbar height
settings put system navigation_bar_height 48

# Navbar width
settings put system navigation_bar_width 48


#
# PowerMenu
#

# Show power menu on secure lockscreen
settings put system lockscreen_enable_power_menu 1

# Power menu items
settings put global power_menu_actions "power|reboot|screenshot|screenrecord|silent"


#
# Volume rocker
#

# Volume keys control media volume
settings put system volume_keys_control_media_stream 0

# Volume button wake
settings put system volume_wake_screen 1

# Music control
settings put system volbtn_music_controls 1

# Volume button swap
settings put system swap_volume_buttons 1

# Volume key cursor control (right/left)
settings put system volume_key_cursor_control 2

# Volume down for do not disturb
settings put secure sysui_volume_down_silent 1

# Volume up in do not disturb
settings put secure sysui_volume_up_silent 1

# Do not disturb switch
settings put secure sysui_show_full_zen 1

# Volume steps: Alarm
settings put system volume_steps_alarm 7

# Volume steps: DTMF
settings put system volume_steps_dtmf 15

# Volume steps: Media
settings put system volume_steps_music 15

# Volume steps: Notification
settings put system volume_steps_notification 7

# Volume steps: Ringer
settings put system volume_steps_ring 7

# Volume steps: System
settings put system volume_steps_system 7

# Volume steps: Voice Call
settings put system volume_steps_voice_call 6


#
# Display
#

# Three finger screenshot
settings put system three_finger_gesture 1

# Allow lights
settings put system allow_lights 1

# Notification light
settings put system notification_light_pulse 1
settings put system notification_light_pulse_default_color 65535
settings put system notification_light_pulse_default_led_off 0
settings put system notification_light_pulse_default_led_on 1
settings put system notification_light_screen_on_enable 0

# Battery light
settings put system battery_light_enabled 1
settings put system battery_light_full_color 65280
settings put system battery_light_low_color 16711680
settings put system battery_light_medium_color 255
settings put system battery_light_pulse 1
settings put system battery_light_really_full_color 65280

# Double tap camera vibration
settings put system double_tap_vibrate 1


#
# Miscellaneous
#

# Toast icon
settings put system toast_icon 1

# Vibrate
settings put system vibrate_on_callwaiting 1
settings put system vibrate_on_connect 1
settings put system vibrate_on_disconnect 1


# Double tap to sleep
settings put system double_tap_sleep_anywhere 1
settings put system double_tap_sleep_gesture 1
settings put system double_tap_sleep_navbar 1

exit 0

