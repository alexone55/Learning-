import chromedriver_autoinstaller
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


logging.basicConfig(format="{asctime} {levelname:<8} {message}", filename="log.txt",
                    filemode='a', style="{", level=logging.DEBUG)


def get_chrome_driver():
    chromedriver_autoinstaller.install('./')
    logging.info("Checking chromedriver update..")
    time.sleep(3)
    driver = set_chrome_drive_parameter_from_file()
    return driver


def set_chrome_drive_parameter_from_file():
    options = Options()
    with open('properties.txt') as config_file:
        for line in config_file:
            if '--' in line:
                options.add_argument(line)
        driver = webdriver.Chrome(executable_path='./86/chromedriver.exe', options=options)
    return driver


if __name__ == '__main__':
    get_chrome_driver()
