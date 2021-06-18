#             ______            __
#      ____  / ______  ______  / /_  ___  _____
#     / __ \/___ \/ / / / __ \/ __ \/ _ \/ ___/
#    / /_/ ____/ / /_/ / /_/ / / / /  __/ /
#   / .___/_____/\__, / .___/_/ /_/\___/_/
#  /_/          /____/_/


# Change zsh directory
export ZDOTDIR=$HOME/.config/zsh

# Set XDG dirs
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share

# Set default editor
export EDITOR="/bin/nvim"
# Nvidia cache directory
export __GL_SHADER_DISK_CACHE_PATH=$XDG_CACHE_HOME/nv
# Flutter
export PATH="$PATH:/usr/local/src/flutter/bin"
export PATH="$PATH:/home/p5ypher/.local/bin"
