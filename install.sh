#!/bin/bash
# vim: 

function cinfo() {
	COLOR='\033[01;33m'	# bold yellow
	RESET='\033[00;00m'	# normal white
	MESSAGE=${@:-"${RESET}Error: No message passed"}
	echo -e "${COLOR}${MESSAGE}${RESET}"
}

cinfo "Updating Packages"
apt-get update -qq; apt-get upgrade -yqq;

cinfo "Installing Custom Banner"
# Backup current Banners
mv /etc/issue /etc/issue.backup
mv /etc/issue.net /etc/issue.net.backup
# Install Custom Banner and activate it in the config file
cp files/banner /etc/issue.net
cp files/banner /etc/issue
sed -ir "s/#Banner .*/Banner \/etc\/issue.net/g" /etc/ssh/sshd_config
# TODO:Disable some of the post login banners
# Restart the ssh server
service ssh restart
