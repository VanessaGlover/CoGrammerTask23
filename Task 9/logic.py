def bag(quantity):
    price_per_bag = 10
    total_cost = quantity * price_per_bag
    return total_cost

print("Welcome to the Bag Ordering System!")

quantity = int(input("How many bags do you want to order? "))
#logical error:  the discount should be applied if the quantity is more than 5
if quantity > 10: #the incorrect condition is applied 
        discount = 2
        total_cost = bag(quantity) - discount
else:
        total_cost = bag(quantity)

print(f"The total cost for the {quantity} bags is £{total_cost}")
