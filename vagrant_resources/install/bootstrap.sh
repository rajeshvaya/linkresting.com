#!/bin/bash
su vagrant 

echo "================================="
echo "Setting up .bash_profile"
echo "================================="
# copy the terminal settings from host
cp -rf /home/vagrant/host_resources/install/.bash_profile /home/vagrant/
source /home/vagrant/.bash_profile


#### PROJECT SETTINGS ####
ENV_NAME="default"


echo "================================="
echo "Creating virtual environments"
echo "================================="

#create the virtual env
mkvirtualenv $ENV_NAME;
workon $ENV_NAME;

echo "============================================="
echo "Install default apps as per requirements.txt"
echo "============================================="
# pip install apps
cd /home/vagrant/www/;
pip install -r requirements.txt