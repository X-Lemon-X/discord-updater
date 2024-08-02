#!/bin/bash
directory=$(dirname "$(readlink -f "$0")")
cd $directory
sudo python3 discord-updater.py