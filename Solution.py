#Task1 By Omar Jabari
def sales(sales_amounts):
    total_sales = sum(sales_amounts) 
    average_sales = total_sales / len(sales_amounts)
    return total_sales , average_sales


weekly_sales = [500,125,300,600,420,890,100]

total_sales,average_sales = sales(weekly_sales)
print("Total Sales is " , total_sales )
print("Average Sales is ", average_sales)

# Task2 By Omar Jabari
#Discount_total function
def discount_total(basket , prices_of_items):
    total_cost = 0
    for product , quantity in basket.items() :
        if product in prices_of_items:
            total_cost += prices_of_items[product] * quantity
        else:
            print("not found")
     #To find the total discount we find the total cost multiply with 90%
    total_of_discount = total_cost * 0.9
    return total_of_discount

#Product prices list
product_prices = {
 'mouse' : 50 ,
 'keyboard': 80,
 'monitor' : 200
}
#Product quantity list
basket_items = {
    'mouse' : 4 ,
    'keyboard' : 3 ,
    'monitor': 2
}
#Final answer for the task
total_of_discount = discount_total(basket_items,product_prices)
print(f"The Total of the discount is: ${total_of_discount:}")


#Task 3  & Task 4 By Omar Jabari

#Define the class with the methods
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
#Method to show the details
    def show_details(self):
        print("Name of the product :" , self.name)
        print(f"Price of the product : , ${self.price}" )
        print("Quantity of the product :",self.quantity)
# for task 4 if the quantity is the self.quantity
    def total_cost_of_a_certian_quantity(self):
        total_cost = self.price * self.quantity
        return total_cost
#for task 4 If the quantity is external and we want to calculate it
    def total_cost_of_a_external_quantity(self,external_quantity):
         total_cost = self.price * external_quantity
         return total_cost

#Creating the instance of the class
p1 = Product('Mouse Razer' , 50 ,4)
#Print the details
p1.show_details()
#print for quantity is the self.quantity
total_cost_for_quantity = p1.total_cost_of_a_certian_quantity()
print(f"Total cost for quantity  units: ${total_cost_for_quantity}")
#print for quantity is external
external_quantity_to_calculate =  6
total_cost_for_external_quantity = p1.total_cost_of_a_external_quantity(external_quantity_to_calculate)
print(f"Total cost for {external_quantity_to_calculate} units: ${total_cost_for_external_quantity}")

#Task 5 By Omar Jabari

# first I created an Excel file called sales_data and put it in Python Scripts
# for importing a csv module like Excel we need to import csv
#------------------------------------------------------------------------------------
#imports csv and os to handle the files and the needed of the task
import csv
import os

output_directory = 'Scratches'
input_file_path = 'sale_data.csv'
output_file_path = os.path.join(output_directory, 'results.csv')

# Ensure the directory exists, create it if necessary
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# i'am gonna create the file sales_data using with open
# the array productes  is the data and inputs for the sale_data file
productes = [
    {"product_name": "mouse", "quantity": 4, "price": 50},
    {"product_name": "keyboard", "quantity": 3, "price": 80},
    {"product_name": "monitor", "quantity": 2, "price": 200}
]


def write_to_csv(file_path, data):
    with open(file_path, mode='w', newline='') as csvfile:
        #Extract the field names (column headers)
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty and write the header if needed
        if csvfile.tell() == 0:
            writer.writeheader()
        #Iterate through the list of dictionaries rows  in the data
        for row in data:
            writer.writerow(row)

# Write new data to the CSV file
write_to_csv(input_file_path, productes)

     #Method to find the total_revenue and average price
def calculate_total_revenue_and_average_price(file_path):
    total_revenue = 0
    total_items = 0

    with open(input_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # Use get method to handle missing keys
            quantity = float(row.get('quantity', 0))
            price = float(row.get('price', 0))

            total_revenue += quantity * price
            total_items += quantity

    if total_items == 0:
        average_price_per_item = 0
    else:
        average_price_per_item = total_revenue / total_items

    return total_revenue, average_price_per_item
    #Save result
def save_results_to_csv(output_file_path, total_revenue, average_price_per_item):
    with open(output_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write header
        writer.writerow(['Total Revenue value', 'Average Price value'])

        # Write total revenue
        writer.writerow(['Total Revenue', f'${total_revenue:}'])

        # Write average price per item
        writer.writerow(['Average Price per Item', f'${average_price_per_item:}'])

# Calculate total revenue and average price per item
total_revenue, average_price_per_item = calculate_total_revenue_and_average_price(input_file_path)

# Save results to a new CSV file results.csv ( the code created it if it's not exist and in our case it's not exist so the code will create it
save_results_to_csv(output_file_path, total_revenue, average_price_per_item)

   # Print a message to show that the Results have been saved into the results.csv
print(f'Results have been saved to {output_file_path}')


