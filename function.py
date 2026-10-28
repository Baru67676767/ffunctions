#part1 : define a function with no arguments to greet the customer
def greet_customer():
    print("welcome to the lemonade stand!")
    print("fresh lemonade, made just for you.")

#part2 : Call the greet_customer function
greet_customer()

#part3: ask for the price per cup and the number of cups sold
price_per_cup = float(input("enter the price per cup in dollars:"))
cups_sold = int(input ("enter the number of cups sold"))

#part 4: Define a function that takes arguments and returns the total cost
def calculate_total(price,cups):
    total = price * cups
    return total

#part 5 : call calculate_total and store the values it returns
total_cost = calculate_total(price_per_cup, cups_sold)

#part6 : use a built_in fucntion to round the total, then print it
rounded_total = round(total_cost, 2)
print("total cost:", rounded_total)

#part7: ask how much  money the customer paid
amount_paid = float(input("enter the amount paid by customer"))

#part 8: Define a function that takes arguments and returns the change due
def calculate_change(paid,total):
    change = paid - total
    return change

# Part 9: Call the calculate_change function and store the value in change
change = calculate_change(total_cost, amount_paid)

# Part 10: Define the thank_you_message function that contains a side/print_message_based_on_cash_flow
def thank_you_message(cups):
    if cups> 50:
        return "Wow, big order! Thanks so much for your support."
    else:
        return "Thanks for stopping by the stand!"

# Part 11: Call the thank_you_message and store the value in thank_you_message_print_message_based_on_cash_flow
thank_you_message_print_message_based_on_cash_flow = thank_you_message(cups_sold)

# Part 12: Print all the final values/data/outputs
print(total_cost)
print("----------------- LEMONADE STAND RECEIPTS -----------------")
print("Total number of items bought:", cups_sold)
print("Total cost:", total_cost)
print("Change to give customer:", change)