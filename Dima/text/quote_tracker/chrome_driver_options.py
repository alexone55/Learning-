import chromedriver_autoinstaller
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    chromedriver_autoinstaller.install('./')
    print('Checking chromedriver update...')
    time.sleep(3)
    driver = set_chrome_drive_parameter_from_file()
    return driver


def set_chrome_drive_parameter_from_file():
    try:
        options = Options()
        with open('properties.txt') as config_file:
            for line in config_file:
                if '--' in line:
                    options.add_argument(line)
            driver = webdriver.Chrome(executable_path='./86/chromedriver.exe', options=options)
        return driver
    finally:
        config_file.close()


def main():
    get_chrome_driver()


if __name__ == '__main__':
    main()
