import time
import logging
import pandas as pd

from datetime import datetime

from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException,
)

from driver import initialize_driver, find_elements

from argparser import argument_parser


# Initializing the logging class for loggin purpose
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s : %(message)s",
    filename=f"./logs/logs_for_{datetime.today().date()}.log",
    filemode="a",
)

# User agent used in this script
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

# Site that is to be scrapped
url = "https://www.sharesansar.com/"

# By default 20 records are fetched per page
num_of_records_per_page = 50

# Storing the result in dataframe
df = pd.DataFrame(
    columns=[
        "SN",
        "Symbol",
        "Transaction No.",
        "Buyer Broker",
        "Seller Broker",
        "Share Quantity",
        "Rate(Rs)",
        "Amount(Rs)",
        "Traded Date",
    ]
)


def add_underscore_to_log_files():
    with open(f"./logs/logs_for_{datetime.today().date()}.log", "a") as log_file:
        log_file.write(
            "\n\n------------------------------------------------------------"
        )
        


def process_table_per_page(elements: WebElement) -> None:
    # Iterate through each row
    for row in elements:
        # Insert data into the DataFrame
        df.loc[len(df)] = row.text.split()


if __name__ == "__main__":
    # Initializing the argument parser
    args = argument_parser()

    # Adding underscore for easy readability
    add_underscore_to_log_files()
    logging.info(f"Log for the date: {datetime.now()}\n")

    # Initializing the driver
    driver = initialize_driver(user_agent=user_agent)
    print("Initializing Driver!!!")
    logging.info(f"Driver Initialized with user_agent: {user_agent}")

    # Accessing the url
    logging.debug(f"Requsting the site: {url}")
    driver.get(url)

    try:
        # Accessing the dropdown menu for 'Market'
        floorsheet_link = find_elements(
            driver=driver, xpath="//footer//a[@href='/floorsheet']"
        )
        # Clicking the link
        logging.debug("Clicking the floorsheet link")
        print("Floor Sheet site opened.")
        floorsheet_link.click()

        # Waiting for the page to load
        time.sleep(5)

        # For accessing the input field one element is to be clicked
        input_access = find_elements(
            driver=driver, xpath="//span[@class='selection']", check_for="clickable"
        )
        input_access.click()

        # Accessing the company input field
        input_field = find_elements(
            driver=driver,
            xpath="//input[@class='select2-search__field']",
            check_for="presence",
        )
        # Sending the keys
        input_field.send_keys(args.stock_name)

        # Clicking the Search button
        search_button = find_elements(
            driver=driver, xpath="//button[@id='btn_flsheet_submit']"
        )
        search_button.click()
        logging.debug(f"Company share: {args.stock_name} searched Successfull")

        # Waiting for the data to be loaded
        time.sleep(5)

        # Traking the pages that is processed
        current_page = 1

        # Loop until the pagination next button is disabled
        logging.info("Processing the table data with paginations")
        print("Processing Table...")
        while True:
            try:
                # print(f"processing page: {current_page}")
                # Find all the rows within the tbody
                rows = find_elements(
                    driver=driver,
                    xpath="//table[@id='myTable']/tbody/tr",
                    multiple_element=True,
                )

                # Processing the table data
                process_table_per_page(rows)

                # Find the pagination next button
                next_button = find_elements(
                    driver=driver,
                    xpath="//div[@id='myTable_paginate']//a[@id='myTable_next']",
                )

                # Check if the next button is enabled
                if "disabled" in next_button.get_attribute("class"):
                    # If the next button is disabled, break the loop
                    print("Page ended, last page read")
                    logging.info("Last page read")
                    break

                # Click the next button
                current_page += 1
                next_button.click()

                # Wait for the page to load after clicking the next button
                time.sleep(3)

            except (NoSuchElementException, StaleElementReferenceException) as err:
                # If no next button is found, break the loop
                print(
                    f"Page Ended with exception at page number {current_page}\n {err}"
                )
                logging.error(f"Error encountered at page: {current_page}: \n {err}")
                break

        logging.info("Extraction Successfull")
        print("Scrapping Successfull..hurray!!!")

    except WebDriverException as err:
        logging.critical(f"Script run failed with error:\n {err}")

    finally:
        logging.info("Closing the driver")
        print("Closing the driver")
        time.sleep(10)
        driver.quit()

    # Storing the result in csv file
    logging.info(
        f"Storing the data in csv file: floorsheet_{datetime.today().date()}.csv"
    )
    df.to_csv(f"datas/floorsheet_{datetime.today().date()}.csv", index=False)
    time.sleep(5)
    print("Data stored to CSV")

    # Quitting the driver
    logging.info("Closing the driver")
    driver.quit()
    time.sleep(10)

    # Logs are in append mode
    # So leaving space to differentiate data from day to day
    # Adding underscore for easy readability
    add_underscore_to_log_files()
