#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}


feh --bg-fill /usr/share/backgrounds/Aurora_Dragon.png &
#starting utility applications at boot time
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#run nm-applet &
#run pamac-tray &
numlockx on &
#blueman-applet &
#flameshot &
#picom --config $HOME/.config/picom/picom.conf &
picom --config .config/picom/picom-blur.conf --experimental-backends &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &

#starting user applications at boot time
#run volumeicon &
#run cbatticon &
#run discord &
#nitrogen --random --set-zoom-fill &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
