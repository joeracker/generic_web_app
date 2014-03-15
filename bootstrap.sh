#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
sudo pip install Flask