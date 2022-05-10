
shopt -s autocd #Allows you to cd into directory merely by typing the directory name.

GREEN="\e[1;92m"
CYAN="\e[1;36m"
NC='\033[0m'

export PS1="${CYAN}[\w]${GREEN} $ ${NC} "
. "/home/bae/.local/share/cargo/env"
