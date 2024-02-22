"""
Configure the different selenium driver as per wish.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def initialize_driver(user_agent: str) -> webdriver:
    """
    Constructor class to initialize the driver.
    For now, it only supports chrome driver.

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
