## Description

This directory stores the scrapped data in csv format.
Csv file of each day will be available here.

# Data Schema

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
