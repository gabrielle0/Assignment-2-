amount_Money = input ("Amount of money you have:")
amount_Money = int (amount_Money)
apple_Price = input ("Price of an apple:")
apple_Price = int (apple_Price)
max_No_Apple = amount_Money // apple_Price 
remaining_Money = amount_Money % apple_Price
print (f"You can buy {max_No_Apple} apples and your change is {remaining_Money} pesos.")
