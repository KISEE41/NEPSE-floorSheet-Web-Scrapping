"""
Configure the different selenium driver as per wish.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


def initialize_driver(user_agent: str) -> webdriver:
    """
    Function to initialize the driver.

    Parameters:
    -----------
    user_agent (str):  user agent of the chrome browser

    Return:
    ----------
    driver: selenium chrome driver
    """

    # Options available and to be used
    option_arguments = [
        # "--headless=new",
        "--window-size=1920,1080",
        f"user-agent={user_agent}",
    ]

    # Initializing the options that are available in chrome
    options = Options()

    # Adding the arguments
    for argument in option_arguments:
        options.add_argument(argument)

    # Initializing the service
    service = Service(ChromeDriverManager().install())

    # Initializing the chrome driver, and return it
    # Here, chrome driver manager is used to manage the driver automatically
    # For more info about webdriver-manager: https://github.com/SergeyPirogov/webdriver_manager
    return webdriver.Chrome(service=service, options=options)


def find_elements(
    driver: webdriver,
    xpath: str,
    check_for: str = None,
    wait_for: int = 5,
    multiple_element: bool = False,
) -> WebElement:
    """
    Constructor class to initialize the driver.
    For now, it only supports chrome driver.

    Parameters:
    -----------
    driver (webdriver):  webdriver to be used
    xpath (str): path of the element in the DOM
    check_for (str): check for the clickability or presense of element
                (options available are 'clickable' and 'presence')
    wait_for (int): wait for the element to be visible
    multiple_element (bool): whether to return multiple element of not

    Return:
    ----------
    WebElement: web element that is selected
    """

    # Check for the presence of the element on the DOM/Element
    if check_for == "presenece":
        return WebDriverWait(driver, wait_for).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    # Check whether the element is clickable
    elif check_for == "clickable":
        return WebDriverWait(driver, wait_for).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    # Otherwise find the element on the DOM/Element
    return (
        driver.find_elements(By.XPATH, xpath)
        if multiple_element
        else driver.find_element(By.XPATH, xpath)
    )
