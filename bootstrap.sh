#!/usr/bin/env bash

# to get the latest updates
sudo apt-get update

# Python Requirements
sudo apt-get install -y python-pip python-dev build-essential
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
sudo pip install Flask

# Setup mysql
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password password'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password password'
sudo apt-get install -y mysql-server mysql-client
mysql -u root -ppassword -e "CREATE USER 'generic'@'localhost' IDENTIFIED BY 'password';GRANT ALL PRIVILEGES ON * . * TO 'generic'@'localhost';FLUSH PRIVILEGES;"

