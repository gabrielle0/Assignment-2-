amount_money = input ("Amount of money you have:")
amount_money = int (amount_money)
apple_price = input ("Price of an apple:")
apple_price = int (apple_price)
max_no_apple = amount_money // apple_price 
remaining_money = amount_money % apple_price
print (f"You can buy {max_no_apple} apples and your change is {remaining_money} pesos.")