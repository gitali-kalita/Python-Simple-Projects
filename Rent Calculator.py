## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# Number of person living in flat

## Output
# Total amount you've to pay is

rent= int(input("Enter youre flat rent = "))
food= int(input("Enter the amount of food ordered = "))
electricity= int(input("Enter the total of electricity bill = "))
charge_per_unit= int(input("Enter the chaege per unit = "))
persons= int(input("Enter the number of persons living in flat =  "))

total_bill= electricity * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)

