#!/bin/bash
xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output eDP-1-1 --off --output DP-1-1 --off &
function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

picom --experimental-backends &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nvidia-settings --assign CurrentMetaMode="HDMI-0: nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On, TripleBuffer = on, AllowIndirectGLXProtocol = off }, eDP-1-1: nvidia-auto-select +1920+0 { ForceFullCompositionPipeline = On, TripleBuffer = on, AllowIndirectGLXProtocol = off }" &

feh --bg-fill $HOME/Pictures/walls/artix-gruvbox.png &
#starting utility applications at boot time
run nm-applet &
run pamac-tray &
#run xfce4-power-manager &
#blueman-applet &
run flameshot &
#picom --config $HOME/.config/picom/picom.conf &
run dunst &
#run optimus-manager-qt &
run copyq &
run redshift-gtk -l 48.666239:9.569250 -t 5600:5000 &
#conky -c ~/.config/conky/.conkyrc &
#/usr/lib/kdeconnectd &
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
