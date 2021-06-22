#!/bin/bash


$HOME/.config/bspwm/scripts/screen_layout.sh &
$HOME/.config/polybar/launch.sh &

feh --bg-fill /usr/share/backgrounds/Aurora_Dragon.png &
pgrep -x sxhkd > /dev/null || sxhkd &


picom --experimental-backends &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xrdb merge ~/.Xresources &
