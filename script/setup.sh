#!/bin/bash -e
# --
# Add -ex for Debugging
#
# Script to install opencv-python package (version==3)
# and tell user location of harr cascade files to be put into python script
#
# This script needs to be run as root.
# --

echo -e "\033[0;34mThis script shall install opencv-python and its dependencies for the facial-rejection program.\033[0m" 

sleep 3

if [ "$EUID" -ne 0 ]
  then echo -e "\033[0;31m Please run as root \033[0m"
  echo "Exiting"
  exit 1
fi

pyVersion="$(python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"

echo -e "\033[0;34mPython Version: $pyVersion\033[0m" 

apt-get update || echo -e "\033[0;31m Please reboot your system and try again \033[0m"

apt-get install opencv-python opencv-contrib-python numpy scipy -y || (echo -e "\033[0;31m Error Installing , Please Try Again\033[0m")

facePath="$(dpkg -L opencv-python  | grep haarcascade_frontalface_default)"

smilePath="$(dpkg -L opencv-python  | grep haarcascade_smile)"

echo -e "\033[0;31mPlease copy the location for facePath and smilePath and paste them in their respective location inside simple_facial_rejection.py\033[0m" 

echo -e "\033[0;34mYour facePath is: $facePath\033[0m" 

echo -e "\033[0;34mYour smilePath is: $smilePath\033[0m" 


