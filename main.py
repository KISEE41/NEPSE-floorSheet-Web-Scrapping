import time
import pandas as pd

from selenium.webdriver.remote.webelement import WebElement

from driver import initialize_driver, find_elements

from argparser import argument_parser


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


def process_table_per_page(elements: WebElement) -> None:
    # Iterate through each row
    for row in elements:
        # Insert data into the DataFrame
        df.loc[len(df)] = row.text.split()


if __name__ == "__main__":
    # Initializing the argument parser
    args = argument_parser()

    # Initializing the driver
    driver = initialize_driver(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    )

    # Accessing the url
    driver.get(url)

    try:
        # Accessing the dropdown menu for 'Market'
        floorsheet_link = find_elements(
            driver=driver, xpath="//footer//a[@href='/floorsheet']"
        )
        # Clicking the link
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

        # Find all the rows within the tbody
        time.sleep(10)
        rows = find_elements(
            driver=driver,
            xpath="//table[@id='myTable']/tbody/tr",
            multiple_element=True,
        )

        # process_table_per_page(rows)

    finally:
        driver.quit()
        pass

    df.to_csv("data.csv", index=False)
    driver.quit()
