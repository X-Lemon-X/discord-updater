#!/bin/bash

# if [[ $EUID -ne 0 ]]; then
#   echo "This script must be run as root. Use sudo"
#   echo "Exiting..."
#   exit 1
# fi
directory=$(dirname "$(readlink -f "$0")")
cd $directory
sudo python3 discord-updater.py

set -e
outfile=$(mktemp)
trap 'rm -f "$outfile"' EXIT
echo "Downloading vencord Installer..."
set -- "XDG_CONFIG_HOME=$XDG_CONFIG_HOME"
curl -sS https://github.com/Vendicated/VencordInstaller/releases/latest/download/VencordInstallerCli-Linux \
  --output "$outfile" \
  --location 
chmod +x "$outfile"
sudo env "$@" "$outfile" -install -location /usr/share/discord