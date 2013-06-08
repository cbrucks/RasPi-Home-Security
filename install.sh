#! /bin/bash

function c_text() {
	COLOR='\033[01;36m'	# bold yellow
	RESET='\033[00;00m'	# normal white
	MESSAGE=${@:-"${RESET}Error: No message passed"}
	echo -e "${COLOR}${MESSAGE}${RESET}"
}


c_text "Installing/Updating Packages"

# update the package manager and 
apt-get update

# install required packages
#   alsa-utils --> sound utilities
#   mpg321     --> mp3 playback
#
sudo apt-get install -y alsa-utils mpg321


c_text "Installing Custom Banner"

# Backup current Banners
mv /etc/issue /etc/issue.backup
mv /etc/issue.net /etc/issue.net.backup

# Install Custom Banner and activate it in the config file
cp files/banner /etc/issue.net
cp files/banner /etc/issue
sed -ir "s/#*Banner .*/Banner \/etc\/issue.net/g" /etc/ssh/sshd_config

# TODO Disable some of the post login banners

# Restart the ssh server
service ssh restart

# TODO Set HDMI as default video source

# 
