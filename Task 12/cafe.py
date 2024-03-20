# Created a list called 'menu'
menu = ["english breakfast", "avocado toast", "granola bowl", "green smoothie", "banana pancake"]

# Created a dictionary called 'stock' with stock values for each item on the menu
stock = {'english breakfast':40,
         'avocado toast' :60,
         'granola bowl'  :50,
         'green smoothie':30,
         'banana pancake':80 
         }
# Created a dictionary called 'price' with the prices for each item on the menu
price = {'english breakfast' :3.5,
         'avocado toast' :5.5,
         'granola bowl'  :4.5,
         'green smoothie':2.5,
         'banana pancake':7.5
           }

# Calculating the total stock on the menu
total_stock = 0
 # Looping through the menu and calculating the item value 
for item in menu:
    stock_value = stock[item]
    price_value = price[item]
    item_value = stock_value * price_value

    total_stock += item_value
    # Prints the reslult
print(f'\n The total stock value is: £{total_stock}')