import time
import csv
from datetime import datetime
from os import path
from Dima.text.quote_tracker.chrome_driver_options import get_chrome_driver


def scrap(quote_name, driver, period):
    try:
        driver.get('https://finance.yahoo.com/quote/{0}'.format(quote_name))
        file = 'quotes.csv'
        headers = ('quote_name', 'quote_data', 'scrap_time')
        data = get_data_from_url(quote_name, driver)
        write_to_csv(file, headers, data)
        while True:
            time.sleep(period)
            new_data = get_data_from_url(quote_name, driver)
            if new_data != data:
                write_to_csv(file, headers, data)
                print('Difference:', -round((data[1] - new_data[1]), 2), 'Data/Time:', data[2])
            data = new_data
        driver.close()
    except ConnectionError:
        raise ConnectionError('Check your internet connection')


def get_data_from_url(quote_name, driver):
    try:
        quote_web_element = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')
        quote_data = round(float(quote_web_element.text), 2)
        scrap_time = datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
        data = (quote_name, quote_data, scrap_time)
        return data
    except ConnectionError:
        raise ConnectionError('Check your internet connection')


def write_to_csv(filename, headers, data):
    if not path.isfile(filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def main():
    # query_name = input('Enter your Quota: ')
    # period = int(input('Enter scraping period in seconds: '))
    driver = get_chrome_driver()
    quote_name = 'AAPL'
    period = int(3)
    scrap(quote_name, driver, period)


if __name__ == '__main__':
    main()
