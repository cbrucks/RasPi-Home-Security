#!/bin/bash
# vim: 


apt-get update; apt-get upgrade -yqq;

# Install Custom Banner and activate it in the config file
cp files/issue.net /etc/issue
sed -ir "s/#Banner .*/Banner \/etc\/issue.net/g" /etc/ssh/sshd_config
