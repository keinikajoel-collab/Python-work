menu = {
    "Rolex" : 3000,
    "Chips" : 5000,
    "Soda" : 2000,
    "Chicken" : 15000,
    "Tea" : 1500
}
## initialize and empty list
order = []

order.append("Rolex")
order.append("Soda")
order.append("Chicken")

print("Order:", order)

total = 0
for item in order:
    total = total+menu[item]

print("Total bill", total, "UGX")