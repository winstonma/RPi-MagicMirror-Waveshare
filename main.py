#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import epaper

from configparser import ConfigParser
import logging
from PIL import Image
from io import BytesIO
from time import time, sleep

#logging.basicConfig(level=logging.DEBUG)

try:
    # Read config file
    config = ConfigParser()
    config.read('config.cfg')
    refreshRate = config.getint('Display', 'refesh_rate')
    model = config.get('Display', 'model')

    epd = epaper.epaper(model).EPD()
    epd.init()
    epd.Clear()

    service = Service('/usr/bin/chromedriver')

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(epd.width, epd.height)

    start_url = config.get('MagicMirror', 'address')
    driver.get(start_url)

    while True:
        # Display the screenshot
        sleep(refreshRate - time() % refreshRate)
        img = Image.open(BytesIO(driver.get_screenshot_as_png()))
        epd.display(epd.getbuffer(img))

    print('Success')

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    driver.close()
    driver.quit()
    epd7in5_V2.epdconfig.module_exit()
    exit()
