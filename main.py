import os as os

# Catalog of items (Name, Description and Price)
catalog = [
  # 1
  {
    "item": "Lovely Loveseat", 
    "description": "Lovely Loveseat.\n Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.", 
    "price": 254
  },
  # 2
  {
    "item": "Stylish Settee",
    "description": "Stylish Settee.\n Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.",
    "price": 180.5
  },
  # 3
  {
    "item": "Luxurious Lamp",
    "description": "Luxurious Lamp.\n Glass and iron. 36 inches tall. Brown with cream shade.",
    "price": 52.15
  }
]

# Business sales tax
sales_tax = .088 
# Customer var
customer_total = 0
customer_cart = []

# Loop to handle customer purchases
done = False
while not done:
  os.system("cls")
  print("Catalog:")
  for item in range(len(catalog)):
    print(f'{item + 1}' + ': ' + catalog[item]["description"])
  if customer_cart:
    print("\n Current cart:")
    for i in customer_cart:
        print("- " + i)
  choice = input("\nChoose the item you want to buy with the respective number (or type anything else to exit the buying page): ")
  if choice.isnumeric() and 0 < int(choice) <= len(catalog):
    choice = int(choice)
    customer_cart.append(catalog[choice-1]["item"])
    customer_total += catalog[choice-1]["price"]
  else:
    break

# Adding the tax value to total value
customer_tax = customer_total * sales_tax
customer_total += customer_tax

# Receipt
os.system("cls")
print("Customer Cart:")
for i in customer_cart:
  print("- " + i)
print("\nCustomer Total:")
print("$" + str(round(customer_total, 2)))



