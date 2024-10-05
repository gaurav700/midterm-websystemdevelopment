import json, argparse

# reading the json file
def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


# main function getting the file as arguments
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str)
    args = parser.parse_args()

    orders = read_orders(args.file_name)
    

if __name__ == "__main__":
    main()
