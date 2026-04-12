# Kiara Williams
# 4/12/2026
# P1HW2
# Create a program to calculate and display travel expenses

print("This program calculates and displays travel expenses") 

a = budget_input = int(input("Enter budget: $ "))
destination = input("Enter your travel destination: ")
b = fuel_input = int(input("How much do you think you will spend on gas: $"))
c = hotel_input = int(input("Approximately, how much will you need for accommodation/hotel?: $"))
d = food_input = int(input("Last, how much do you need for food: $"))


print("--------Travel Expenses--------")
print()

print("Location:", destination)
print("initial budget: ", budget_input)
print()

print("Fuel: ", fuel_input)
print("Accomodation: ", hotel_input)
print("Food: ", food_input)
print()

print("Remaining Balance: ", a - b - c - d)










