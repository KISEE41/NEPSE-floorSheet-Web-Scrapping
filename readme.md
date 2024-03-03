# Web Scraping Task Documentation

This documentation outlines the process of web scraping data from the website [ShareSansar](https://www.sharesansar.com/floorsheet), saving the extracted data in CSV format, and logging the execution. The documentation provides a detailed explanation of the steps involved, the tools and libraries used, and instructions for executing the scraping task.

## Table of Contents

- [Introduction](#introduction)
- [Tools Used](#tools-used)
- [Process Overview](#process-overview)
- [Step-by-Step Guide](#step-by-step-guide)
  - [1. Setting Up Environment](#1-setting-up-environment)
  - [2. Installing Requirements](#2-installing-requirements)
  - [3. Executing the Script](#3-executing-the-script)
- [Data Schema](#data-schema)
- [Github Action Workflow](#github-action-workflow)
- [Future Enhancement](#future-enhancement)
- [Conclusion](#conclusion)

## Introduction

Web scraping is the process of extracting data from websites. In this task, the data are scraped from the [ShareSansar floorsheet](https://www.sharesansar.com/floorsheet) website. The floorsheet provides information about the stock market transactions in Nepal.

## Tools Used

- **Programming Language:** Python
- **Web Scraping Library:** Selenium
- **Logging Module:** Python's built-in logging module

## Process Overview

1. **Setting Up Environment**: Create a virtual environment to manage dependencies.
2. **Installing Requirements**: Install necessary Python packages using a requirements file.
3. **Executing the Script**: Run the Python script to scrape data from ShareSansar and save it to a CSV file.

## Step-by-Step Guide

### 1. Setting Up Environment

- Create a virtual environment using the following command:
  ```
  python -m venv venv
  ```

### 2. Installing Requirements

- Activate the virtual environment:
  - On Windows:
    ```
    venv\Scripts\activate
    ```
  - On macOS and Linux:
    ```
    source venv/bin/activate
    ```
- Install the required packages using the provided requirements file:
  ```
  pip install -r requirements.txt
  ```

### 3. Executing the Script

- Run the Python script `main.py` to scrape data from ShareSansar:
  ```
  python main.py
  ```
- To specify the stock to fetch, use the `--stock_name` argument:
  ```
  python main.py --stock_name <stock_name>
  ```
  _(Note: The script provides the functionality of extracting data of specific stock, for that we can use the argparser optional parameter to provide the name of stock, if not provided default value of **HRL** is taken as stock_name)_
- For more information and help, use the `-h` or `--help` option:
  ```
  python main.py -h
  ```

## Data Schema

Running the script scrape the data from website, arrange it in dataframe, and store it in csv format inside a folder called **datas**.

| Field           | Data Type   | Description                                                    |
| --------------- | ----------- | -------------------------------------------------------------- |
| SN              | Integer     | Serial Number assigned to each transaction record.             |
| Symbol          | String      | Unique identifier representing the stock symbol.               |
| Transaction No. | String      | Unique identification number for each transaction.             |
| Buyer Broker    | Integer     | Identification code for the buyer's broker.                    |
| Seller Broker   | Integer     | Identification code for the seller's broker.                   |
| Share Quantity  | Float       | Number of shares involved in the transaction.                  |
| Rate(Rs)        | Float       | Rate per share in Nepalese Rupees (Rs).                        |
| Amount(Rs)      | String      | Total transaction amount in Nepalese Rupees (Rs).              |
| Traded Date     | Date/String | Date of the transaction. It could be in Date format or String. |

### Description:

- **SN (Serial Number):** A unique identifier assigned to each transaction record in sequential order.
- **Symbol:** The stock symbol represents a unique identifier for a particular stock listed in the stock market.
- **Transaction No.:** Each transaction is assigned a unique identification number for reference purposes.
- **Buyer Broker:** Identification code assigned to the broker representing the buyer in the transaction.
- **Seller Broker:** Identification code assigned to the broker representing the seller in the transaction.
- **Share Quantity:** The number of shares involved in the transaction, represented as a floating-point number.
- **Rate(Rs):** The rate per share in Nepalese Rupees (Rs) at which the transaction was conducted.
- **Amount(Rs):** The total transaction amount in Nepalese Rupees (Rs), calculated as the product of share quantity and rate per share.
- **Traded Date:** The date on which the transaction occurred. It could be in Date format or String, representing the date of the transaction.

This schema provides a structured representation of the data extracted from the ShareSansar floorsheet website, enabling easy understanding and analysis of stock market transactions in Nepal.

## Github Action Workflow

Using the github action workflow, the cron job is created that executes at UTC 1AM each day; so the csv file of each day is created and stored. For more information for the github action used here, click [here](./.github/workflows/readme.md).

## Future Enhancements

### 1. Dockerization

Dockerizing the web scraping application can offer several benefits such as:

- **Portability:** Docker containers can run on any platform, providing consistent behavior across different environments.
- **Isolation:** Docker containers encapsulate the application and its dependencies, ensuring that it runs independently of the underlying infrastructure.
- **Ease of Deployment:** Docker provides a straightforward mechanism for deploying applications, making it easier to manage and scale.

To dockerize the application:

- Create a Dockerfile specifying the application environment and dependencies.
- Build the Docker image.
- Run the Docker container with appropriate configurations.

### 2. ETL (Extract, Transform, Load) Pipeline

Implementing an ETL pipeline can help in managing and processing the scraped data efficiently. The pipeline would involve the following steps:

- **Extract:** Retrieve data from the CSV files generated by the scraping script.
- **Transform:** Clean, transform, and standardize the data format as necessary.
- **Load:** Load the transformed data into a centralized data store or database for analysis and visualization.

To implement the ETL pipeline:

- Use Python libraries like Pandas for data manipulation and transformation.
- Schedule the ETL pipeline to run periodically to process new data generated by the scraping script.

### 3. Data Visualization with Box Plots

Visualizing the data using box plots can provide insights into the distribution and variability of key metrics such as share quantity, rate, and transaction amounts.

To implement data visualization with box plots:

- Use Python libraries like Matplotlib or Seaborn to generate box plots.
- Aggregate the scraped data based on relevant dimensions (e.g., stock symbol, transaction date).
- Plot box plots for different dimensions to visualize trends and outliers in the data.
- Include labels and annotations to make the plots more informative and understandable.

These future enhancements can improve the scalability, manageability, and analytical capabilities of the web scraping application. By dockerizing the application, implementing an ETL pipeline, and incorporating data visualization techniques, users can gain deeper insights into the stock market transactions and make informed decisions based on the analyzed data.

## Conclusion

Web scraping is a powerful technique for extracting data from websites, and it can be used for various purposes such as data analysis, research, and automation. By following the steps outlined in this documentation, you can effectively set up your environment, install dependencies, and execute the scraping script to fetch data from the ShareSansar floorsheet website.
