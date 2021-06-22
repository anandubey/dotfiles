#!/bin/bash

if [[ "$(bspc query -M | wc -l)" -eq "2" ]]; then
    bspc monitor $(bspc query -M --names | awk '/^HDMI*/ {print}') -d 1 2 3 4 5
    bspc monitor $(bspc query -M --names | awk '/^eDP*/ {print}') -d 6 7 8 9 0
else
    bspc monitor -d 1 2 3 4 5 6 7 8 9 0
fi
