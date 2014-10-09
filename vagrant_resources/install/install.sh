#!/bin/bash
echo "==========================================="
echo "Provisioning virtual machine..."
echo "==========================================="

# Install essential packages from Apt
echo "Updating apt-get..."
#apt-get update -y

# python-setuptools
echo "=============================="
echo "Installing python-setuptools"
echo "=============================="
apt-get install python-setuptools -y

#apache
if ! command -v apache2; then
    echo "=============================="
    echo "Installing Apache2"
    echo "=============================="
    sudo apt-get install apache2 -y
fi

#git
if ! command -v git; then
    echo "=============================="
    echo "Installing Git"
    echo "=============================="
    sudo apt-get install git -y
fi

#sqlite3
if ! command -v sqlite3; then
    echo "=============================="
    echo "Installing sqlite3"
    echo "=============================="
    sudo apt-get install sqlite3 -y
fi


#mysql
if ! command -v mysql; then
    echo "=============================="
    echo "Setting up MySQL..."
    echo "=============================="
    apt-get install debconf-utils -y
    debconf-set-selections <<< "mysql-server mysql-server/root_password password root"
    debconf-set-selections <<< "mysql-server mysql-server/root_password_again password root"

    apt-get install python-dev -y
    apt-get install libmysqlclient-dev -y
    apt-get install mysql-client-core-5.5 -y
    apt-get install mysql-server mysql-client -y
    
fi

# pip
if ! command -v pip; then
    echo "=============================="
    echo "Installing pip..."
    echo "=============================="
    easy_install -U pip
fi

#virtualenv
if [[ ! -f /usr/local/bin/virtualenv ]]; then
    echo "==========================================="
    echo "Installing virtualenv virtualwrapper..."
    echo "==========================================="
    pip install virtualenv virtualenvwrapper stevedore virtualenv-clone
fi


