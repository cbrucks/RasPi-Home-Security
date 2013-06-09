#! /bin/bash

function c_header() {
	COLOR='\033[01;36m'	# bold cyan
	RESET='\033[00;00m'	# normal white
	MESSAGE=${@:-"${RESET}Error: No message passed"}
        echo -e "+${COLOR}${MESSAGE}${RESET}"
}
function c_text() {
	COLOR='\033[00;00m'	# bold cyan
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

c_text "Install custom banner"

# Backup current Banners
if [ ! -f /etc/issue.sav ]; then
  sudo mv /etc/issue /etc/issue.sav
fi
if [ ! -f /etc/issue.net.sav ]; then
  sudo mv /etc/issue.net /etc/issue.net.sav
fi

# Install Custom Banner and activate it in the config file
sudo cp ../files/banner /etc/issue.net  # ssh terminal connection
sudo cp ../files/banner /etc/issue      # local terminal connection
sudo sed -ir "s/#*Banner .*/Banner \/etc\/issue.net/g" /etc/ssh/sshd_config

c_text "Disable welcome messages"

# Disable unwanted welcome messages
entries="/etc/pam.d/login;session    optional   pam_lastlog.so,\
         /etc/pam.d/login;session    optional   pam_motd.so  motd=/run/motd.dynamic,\
         /etc/pam.d/login;session    optional   pam_motd.so,\
         /etc/pam.d/login;session    optional   pam_mail.so standard,\
         /etc/pam.d/sshd;session    optional     pam_motd.so  motd=/run/motd.dynamic noupdate,\
         /etc/pam.d/sshd;session    optional     pam_motd.so,\
         /etc/pam.d/sshd;session    optional     pam_mail.so standard noenv"

(IFS=,
for entry in $entries; do
  file=`echo "$entry" | sed "s/^ *//g" | sed "s/ *$//g" | cut -d ";" -f1`
  text=`echo "$entry" | sed "s/^ *//g" | sed "s/ *$//g" | cut -d ";" -f2`
  
  sed -ir "s@^$text@#$text@g" $file
done)

# TODO Disable some of the post login banners

# Restart the ssh server
sudo service ssh restart
