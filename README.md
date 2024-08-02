# Discord Updater

This repository contains the source code for the handy script to update Discord automatically. 
No longer anoying pops up to update your discord manually.

## Description
Discord Updater is a tool that automatically updates your Discord when new version is available.
Using deb package.

## Installation
To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/X-Lemon-X/discord-updater.git`
2. Copy path to a file udpater-discord.sh
3. Open terminal and run 
```bash
sudo crontab -e
```
4. Add the following line to the end of the file
```bash
@reboot /path/to/this/repo/updater-discord.sh
```
5. Save and exit the file
6. Now discord will be updated automatically on every reboot

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
