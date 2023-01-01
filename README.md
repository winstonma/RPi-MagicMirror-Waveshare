# Magicmirror on Waveshare eink device

## How it works
The python script uses [selenium](https://github.com/SeleniumHQ/selenium), to take a screenshot of the local running MagicMirror site (localhost:8080) and display the screenshot on the eInk screen.  

## Requirements
- Raspberry Pi with Raspbian
- [Waveshare display](https://www.waveshare.com/epaper)
- running [MagicMirror](https://github.com/MichMich/MagicMirror) (serveronly)
- it seams that MagicMirror² **must have been installed the "normal" way** - no imagefile, no installation script, otherwise this script will cause very strange unreproducable errors

## Important
As said before: It seams that MagicMirror² **must have been installed the "normal" way** - no imagefile, no installation script, otherwise this script will cause very strange unreproducable errors

## Configuration
All configuration in done in the ``config.cfg`` file and is as well mandatory as self explanatory.
The only thing which might become difficult is finding the right name for your Waveshare-Display. So have a look at the [official library of Waveshare](https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd) and you will find your epaper-screen!
Please note that Waveshare has recommendations about the refresh rate:

> When using the e-Paper display, it is recommended that the refresh interval be at least 180s, and refresh at least once every 24 hours. If the e-Paper is not used for a long time, you should use the program to clear the screen before storing it. (Refer to the datasheet for specific storage environment requirements.) [(Source)](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT_Manual#Precautions)

## Resources
- [3d printable frame](https://www.thingiverse.com/thing:3382910)

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
cd RPi-MagicMirror-Waveshare
# Install python dependencies (inside the `rpi-magicmirror-eink` folder)
sudo pip install -r requirements.txt
# Start the script with PM2 and run it in the background
pm2 start main.py --name "eink-update"
pm2 save
```

## Optional styling
As the normal css will not look good you can use this specific css in your ``~/MagicMirror/css/custom.css``

<details>
  <summary>CSS for E-Paper-Displays</summary>
  
```css
/* Magic Mirror Custom CSS Sample
 *
 * Change color and fonts here.
 *
 * Beware that properties cannot be unitless, so for example write '--gap-body: 0px;' instead of just '--gap-body: 0;'
 *
 * MIT Licensed.
 */

/* Uncomment and adjust accordingly if you want to import another font from the google-fonts-api: */
/* @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;400;700&display=swap'); */

:root {
  --color-text: black;
  --color-text-dimmed: #666;
  --color-text-bright: black;
  --color-background: white;

  --font-primary: "Roboto Condensed";
  --font-secondary: "Roboto";
  
  --font-size: 24px;
  --font-size-small: 0.75rem;

  --gap-body-top: 0px;
  --gap-body-right: 0px;
  --gap-body-bottom: 0px;
  --gap-body-left: 0px;
  
  --gap-modules: 5px;
}

header {
  display: none!important;
}

.light {
  font-weight: 400;
}

.medium {
  font-size: 1.25rem;
}

.small {
  font-size: 1.1rem;
}
```
</details>

## Troubleshooting
### My screen flickers and then stays black
Wait! I guess this has to do with the page loading. While the page hasn't loaded, a screenshot is taken which due to the initial CSS of MagicMirror² purely black. After some minutes the picture should reload and show what you want to see.
### After reboot the MagicMirror doesn't show
Does ``pm2 list`` takes some seconds to load and shows an empty table? Has happened to me too! Carefully [go through the installation of the autostart](https://docs.magicmirror.builders/configuration/autostart.html#using-pm2) again! **Pay close attention to the shell output! At some point it gives you a command line you have to copy, paste, execute.** Do so and probably the problem is solved. Don't forget to ``pm2 save``!
### I cannot see my CSS-Changes
Go to mobile view in your "normal" Browser such as Firefox (Ctrl+Shift+M) and configure a custom screen (for instance 800x480 for the large Waveshare display), do all your CSS stuff, reload the browser window each time you want to check the changes. When you are satisfied on your "normal" screen simulating your e-paper display ``sudo reboot`` your Rasperry Pi to take effect of the changes on the EPD (electornic paper display)!

## Ressources
- The project uses the Original Library written by Waveshare. It can be downloaded [here](https://www.waveshare.com/wiki/Main_Page#OLEDs_.2F_LCDs).
