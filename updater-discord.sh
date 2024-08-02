#!/bin/bash

if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root. Use sudo"
  echo "Exiting..."
  exit 1
fi
directory=$(dirname "$(readlink -f "$0")")
cd $directory
python3 discord-updater.py