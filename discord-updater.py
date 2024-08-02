#!/usr/bin/python3
import re
import subprocess
import traceback
from pathlib import Path
import os

import requests

def compare_version(install_candidate, installed_version) -> bool:
  for i in range(len(installed_version)):
    if install_candidate[i] > installed_version[i]:
      return True
    elif install_candidate[i] < installed_version[i]:
      return False

def main():
  r = requests.head('https://discord.com/api/download?platform=linux&format=deb')
  dl_url = r.headers['location']
  filename = dl_url.split('?')[0].split('/')[-1]
  m = re.search(r'(\d+\.\d+\.\d+)', filename)
  version = m.group(1)
  # Use apt to check the installed version of Discord
  try:
    output = subprocess.check_output(['apt-cache', 'policy', 'discord']).decode('utf-8')
    installed_version = re.search(r'Installed:\s*(\S+)', output).group(1)
    installed_version = [int(x) for x in installed_version.split('.')]
    install_candidate = [int(x) for x in version.split('.')]
    if not compare_version(install_candidate, installed_version):
      print("Current installed version is up to date.")
      return 0
    else:
      print(f"Current installed version ({installed_version}) is lower than the latest version ({version}).")
  except Exception as e:
    print("Failed to retrieve installed version of Discord.")
    return 1
    
  discord_file = Path(__file__).with_name(f'discord-{version}.deb') 
  print(f'Downloading: {dl_url}')
  with requests.get(dl_url, stream=True) as r:
    with discord_file.open('wb') as fp:
      for chunk in r.iter_content(chunk_size=65536):
        fp.write(chunk)
  try:
    command = f"sudo dpkg -i {discord_file}"
    print(f"Installing Discord {version}...")
    print(f"Running command: {command}")
    subprocess.Popen(command,shell=True).wait()
  except subprocess.CalledProcessError:
    print("Failed to install Discord.")
    return 1
  
  print("Discord has been successfully updated.")
  discord_file.unlink()
  print("Removed .deb file.")
  if os.path.exists(discord_file):
    os.remove(discord_file)
  print("Done.")
  return 0

if __name__ == '__main__':
  exit_code = main()
  exit(exit_code)