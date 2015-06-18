#!/bin/bash

apt-get update
apt-get -y dist-upgrade
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm get-pip.py
apt-get install -y python3-dev
pip install flask

apt-get install ipython python-ipdb
