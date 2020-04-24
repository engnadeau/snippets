#!/usr/bin/env bash

set -x

sudo apt update
sudo apt full-upgrade -y
sudo apt dist-upgrade -y
sudo apt autoremove -y
sudo apt autoclean -y

sudo snap refresh
