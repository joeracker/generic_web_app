#!/usr/bin/env bash

# Use vagrant provision --provision-with shell to quickly rerun this script for the vagrant vm
# From http://docs.vagrantup.com/v2/cli/provision.html

# to get the latest updates
sudo apt-get update

# Python Requirements
sudo apt-get install -y python-pip python-dev build-essential
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
sudo pip install -r /vagrant_data/requirements.txt

# Setup mysql
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password password'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password password'
sudo apt-get install -y mysql-server mysql-client
mysql -u root -ppassword << EOF
 CREATE DATABASE IF NOT EXISTS generic;
 GRANT ALL PRIVILEGES  ON generic.* 
  TO 'generic'@'%' IDENTIFIED BY 'password' 
  WITH GRANT OPTION;
 FLUSH PRIVILEGES;
EOF
sudo apt-get install libmysqlclient-dev