import time

from argparser import argument_parser

from driver import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Site that is to be scrapped
url = "https://www.nepalstock.com.np/"

# By default 20 records are fetched per page
num_of_records_per_page = 20

if __name__ == "__main__":
    driver = initialize_driver(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    )

    driver.get(url)

    try:
        # Wait for the dropdown button to be clickable
        navbar_dropdown = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "navbarDropdown"))
        )

        # Click the dropdown button
        navbar_dropdown.click()

        # Find the dropdown item with the href "/floor-sheet"
        floor_sheet_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.dropdown-item[href='/floor-sheet']")
            )
        )

        # Click the dropdown item if found
        floor_sheet_link.click()

        # Wait for the reset button to be clickable
        reset_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "box__filter--reset"))
        )

        # Click the reset button
        reset_button.click()
    except:
        print("Error")
    finally:
        # Close the WebDriver
        driver.quit()
