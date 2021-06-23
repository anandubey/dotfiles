#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

nvidia-settings --assign CurrentMetaMode="HDMI-0: nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On, TripleBuffer = on, AllowIndirectGLXProtocol = off }, eDP-1-1: nvidia-auto-select +1920+0 { ForceFullCompositionPipeline = On, TripleBuffer = on, AllowIndirectGLXProtocol = off }" &

feh --bg-fill $HOME/Pictures/wallpapers/ghost.jpg &
#starting utility applications at boot time
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
run nm-applet &
run pamac-tray &
numlockx on &
#run xfce4-power-manager &
#blueman-applet &
#flameshot &
#picom --config $HOME/.config/picom/picom.conf &
picom &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &

#starting user applications at boot time
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
