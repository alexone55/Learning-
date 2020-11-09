import time
import logging
import csv
from datetime import datetime
from os import path
from Dima.text.quote_tracker.chrome_driver_options import get_chrome_driver


file = 'quotes.csv'
logging.basicConfig(filename="log.txt", format="{asctime} {levelname:<8} {message}", style="{", level=logging.INFO, )


def scrap(quote_name, file, driver, period):
    driver.get(f'https://finance.yahoo.com/quote/{quote_name}')
    headers = ('quote_name', 'quote_data', 'scrap_time')
    data = get_data_from_url(quote_name, driver)
    write_to_csv(file, headers, data)
    counter = 0
    try:
        while counter < 3:
            time.sleep(period)
            new_data = get_data_from_url(quote_name, driver)
            if new_data != data:
                write_to_csv(file, headers, new_data)
                logging.info(f'Difference:, {-round((data[1] - new_data[1]), 2)}, "Data/Time:", {data[2]}')
            data = new_data
            counter += 1
    finally:
        driver.close()


def get_data_from_url(quote_name, driver):
    quote_web_element = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')
    quote_data = round(float(quote_web_element.text), 2)
    scrap_time = datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
    data = (quote_name, quote_data, scrap_time)
    return data


def write_to_csv(file_name, headers, data):
    if not path.isfile(file_name):
        with open(file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def input_tracker_parameters():
    quote_name = input('Enter your Quota: ')
    if not isinstance(quote_name, str):
        raise TypeError('Your message isn`t string type: ')
    period = int(input('Enter scraping period in seconds: '))
    return quote_name, period


def main():
    # quote_name, period = input_tracker_parameters()
    quote_name = 'AAPL'
    period = 3
    driver = get_chrome_driver()
    scrap(quote_name, file, driver, period)


if __name__ == '__main__':
    main()