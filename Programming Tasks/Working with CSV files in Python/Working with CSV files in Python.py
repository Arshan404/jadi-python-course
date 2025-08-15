import csv

input_file = r"D:\py projects\jadi python course\jadi-python-course\Programming Tasks\Working with CSV files in Python\1741502118270796.csv"
output_file = r"D:\py projects\jadi python course\jadi-python-course\Programming Tasks\Working with CSV files in Python\processed_products.csv"

# Detect possible delimiter (Tab or Comma)
with open(input_file, 'r', encoding='utf-8') as f:
    first_line = f.readline()
    if '\t' in first_line:
        delimiter = '\t'
    else:
        delimiter = ','

# Read data from CSV
products = []
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=delimiter)
    for row in reader:
        # Strip extra spaces from keys and values
        row = {k.strip(): v.strip() for k, v in row.items()}
        price = float(row['Price'])
        quantity = int(row['Quantity'])
        total = price * quantity
        row['Total Price'] = total
        products.append(row)

# Write processed data to new CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['Product Name', 'Price', 'Quantity', 'Total Price']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()  # Write column headers
    for product in products:
        writer.writerow({
            'Product Name': product['Product Name'],
            'Price': product['Price'],
            'Quantity': product['Quantity'],
            'Total Price': product['Total Price']
        })

print(f"Processed data saved to {output_file}")


    