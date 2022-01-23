# Magicmirror on Waveshare eink device

## How it works
The python script uses [selenium](https://github.com/SeleniumHQ/selenium), to take a screenshot of the local running MagicMirror site (localhost:8080) and display the screenshot on the eInk screen.  

You can change the MagicMirror port in the
 `config.cfg` file.

## Requirements
- Raspberry Pi with Raspbian
- [Waveshare display](https://www.waveshare.net/list.html?cat=85) (This is a chinese link)
- running [MagicMirror](https://github.com/MichMich/MagicMirror) (serveronly)

## Resources
- [3d printable frame](https://www.thingiverse.com/thing:3382910)
- [Installations-Tutorial (deutsch)](https://maker-tutorials.com/7-5-eink-epaper-bilderrahmen-magicmirror-display-raspberry-pi-zero-w/)
- [MagicMirror Module List](https://github.com/MichMich/MagicMirror/wiki/3rd-Party-Modules)

## Install dependencies

```bash
# Update packages and install Git, Chrome Browser
sudo apt-get update && sudo apt-get install -y git chromium-browser chromium-chromedriver
# Install PM2 (process manager for Node.js)
sudo npm install -g pm2
// Starting PM2 on Boot
pm2 startup
// pm2 start node serveronly
// pm2 save
```

## Setup

```bash
# Clone/copy the project files to your system
git clone https://github.com/winstonma/RPi-MagicMirror-Waveshare.git
# Move to the project folder
cd rpi-magicmirror-eink
# Install python dependencies (inside the `rpi-magicmirror-eink` folder)
sudo pip install -r requirements.txt
# Start the script with PM2 and run it in the background
pm2 start index.js --name "eink-update"
pm2 save
```

## Todo
- [X] 3d print case
- [ ] white background/black font mode (invert image with [jimp](https://github.com/oliver-moran/jimp) (image.invert();))

## Ressources
- The project uses the Original Library written by Waveshare. It can be downloaded [here](https://www.waveshare.com/wiki/Main_Page#OLEDs_.2F_LCDs).
