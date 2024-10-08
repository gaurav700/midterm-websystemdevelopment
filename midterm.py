import json
import argparse
from collections import defaultdict

# reading the json file named example_orders.json that is passed via command line argument
def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# creating the customer.json file
def create_customers_file(orders):
    customers = {order['phone']: order['name'] for order in orders}
    
    with open('customers.json', 'w') as file:
        json.dump(customers, file, indent=4)

#creating the items.json file
def create_items_file(orders):
    items = defaultdict(lambda: {'price': 0, 'orders': 0})
    
    for order in orders:
        for item in order['items']:
            name, price = item['name'], item['price']
            items[name]['price'] = price
            items[name]['orders'] += 1
    
    with open('items.json', 'w') as file:
        json.dump(items, file, indent=4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str)
    args = parser.parse_args()
    orders = read_orders(args.file_name)
    create_customers_file(orders)
    create_items_file(orders)

if __name__ == "__main__":
    main()
