#creat a function called chocolate
def chocolate(money,price):
    """Input the total money and the price of chocolate
       Return the number of bars the user can buy and the change that will be left
    """
    bar=money//price#the number of bars 
    change=money%price#the change that will be left
    return bar,change
#input the money and price as you want to set
money_str=input("The total money the user has:")
money=int(money_str)#transfer the string into integar
price_str=input("The price of one chocolate bar:")
price=int(price_str)
a,b=chocolate(money,price)#call the function
print(f"The number of bars is {a}, the change is {b}")#print the results
