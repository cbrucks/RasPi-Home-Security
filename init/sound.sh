#!/bin/bash

function c_header() {
        COLOR='\033[01;36m'     # bold cyan
        RESET='\033[00;00m'     # normal white
        MESSAGE=${@:-"${RESET}Error: No message passed"}
        echo -e "+${COLOR}${MESSAGE}${RESET}"
}
function c_text() {
        COLOR='\033[00;00m'     # bold cyan
        RESET='\033[00;00m'     # normal white
        MESSAGE=${@:-"${RESET}Error: No message passed"}
        echo -e "+--${COLOR}${MESSAGE}${RESET}"
}

if [ "$(id -u)" != "0" ]; then
  echo "This script has to be run with root priveledges. Rerun it using sudo."
  exit
fi

c_header ${0##*/}

cd $(dirname $0)

c_text "Setup 3.5mm output settings"

sudo modprobe snd-bcm2835

amixer cset numid=3 1

sed -i "s/pcm.front cards.pcm.front/pcm.front cards.pcm.default/g" /usr/share/alsa/alsa.conf

c_text "Restart the ALSA utilities"

/etc/init.d/alsa-utils restart
