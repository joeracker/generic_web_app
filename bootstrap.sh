#!/usr/bin/env bash

apt-get update
apt-get install -y python-pip python-dev build-essential
pip install --upgrade pip 
pip install --upgrade virtualenv 

pip install Flask