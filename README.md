# Dosa Restaurant Order Processing System

## Overview
The Dosa Restaurant Order Processing System is a Python script designed to help manage and organize order data for a Dosa restaurant. The script reads order information from a JSON file, processes it, and generates two new JSON files: `customers.json` and `items.json`. This organization helps the restaurant owner track customer details and item sales more effectively.

## Features
- Reads a JSON file containing individual orders.
- Generates a `customers.json` file mapping customer phone numbers to names.
- Generates an `items.json` file that tracks item prices and the number of times each item has been ordered.
- Phone numbers are formatted as `xxx-xxx-xxxx` for consistency.


## File Descriptions

- **midterm.py**: 
  - This is the main Python script responsible for reading the orders from the input JSON file, processing the data, and creating the output JSON files. The script handles tasks such as extracting customer information and item details from the orders.

- **example_orders.json**: 
  - This file contains sample order data in JSON format. It serves as an example for how the input data should be structured.

- **customers.json**: 
  - This output file stores the details of customers extracted from the processed orders. The data includes information such as customer names, contact details, and order history.

- **items.json**: 
  - This output file contains information about the items ordered by customers. It includes details such as item names, quantities, and pricing.

- **README.md**: 
  - This documentation file provides an overview of the project, including instructions on how to run the Python script and details about the project structure.

## Requirements
- Python 3.x
- No external libraries are required (standard library only).

## Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/gaurav700/midterm-websystemdevelopment.git
   cd midterm-websystemdevelopment
   ```
2. **Run the script**:
```
py midterm.py example_orders.json
```

## Output Files
After running the script, you will find two new files in the project directory:
- **customers.json:** Contains a mapping of phone numbers to customer names.
- **items.json:** Contains a mapping of item names to their prices and the number of times they have been ordered.
   

