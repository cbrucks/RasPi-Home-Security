#! /bin/bash

function c_header() {
	COLOR='\033[01;36m'	# bold cyan
	RESET='\033[00;00m'	# normal white
	MESSAGE=${@:-"${RESET}Error: No message passed"}
	echo "###########################################################"
        echo -e "${COLOR}${MESSAGE}${RESET}"
	echo "###########################################################"
}
function c_text() {
	COLOR='\033[01;36m'	# bold cyan
	RESET='\033[00;00m'	# normal white
	MESSAGE=${@:-"${RESET}Error: No message passed"}
        echo -e "+--${COLOR}${MESSAGE}${RESET}"
}

if [ "$(id -u)" != "0" ]; then 
  echo "This script has to be run with root priveledges. Rerun it using sudo."
  exit
fi

c_header ${0##*/}

cd $(dirname $0)

if [ -d init ]; then
  files=$( ls -1 init | grep -G ".sh$" )
  for file in $files; do
    sudo ./init/$file
  done
fi

