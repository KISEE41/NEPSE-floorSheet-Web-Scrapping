"""
This file is used to get the argument from the user via terminal.
"""

import argparse


def argument_parser() -> str:
    """
    parse the argument sent via terminal.

    Parameters:
    -----------
    None

    Return:
    ----------
    str: return the stock name, that is provided via terminal. (If not provided returns the default value)
    """
    # Initializing the  ArgumentParser
    parser = argparse.ArgumentParser(
        description="Get the name of the stock from the user via terminal"
    )

    # Adding the stock_name argument (note: the argument provided is optional)
    # If not provided from the terminal, replace by the default value
    parser.add_argument(
        "--stock_name",
        type=str,
        default="Himalayan Reinsurance Limited / HRL",
        help="Name of the stock",
    )

    # Parse the arguments
    args = parser.parse_args()

    # returning the arguments
    return args
