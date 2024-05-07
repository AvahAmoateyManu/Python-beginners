##print("boop".count("o")) # a is 2 because there are 2 o's in boop
##print("title".find("t")) # b is 0 because the first t is at index 0
##print("StR1nG".isalnum())
### c is True because the string is only letters and numbers
##print( "Hello World!".isalpha())
### d is False because there is a space and !
##print("1234".isdigit())
### e is True because our string is all numbers
##print("HAYDEN".isupper())
### f is True because all the letters are uppercase
##print( "hayden123".islower())
### g is True because all the letters are lowercase
##print("banana".replace('a', 'u'))
### h is "bununu" because all a's are replaced with u's
##print(" jo jo".title()) # j is "Jo Jo"
##a=input('write your name ')
##print(a[0].upper()+a[1::1])
##print(a.title()
##print('row row row'.replace('r','m'),'your boat')
##a=(input('What is your favorite number'))
##while a.isdigit() == False:
##    print('Invalid input')
##    a=(input('What is your favorite number'))
####print(type(a))
####else:
######    a=int(a)
######print(type(a))
##a=(input('enter a number you want to multiply '))
##b=(input('enter another number you want to multiply '))
##while a.isdigit()== False and b.isdigit()== False:
##    print('Invalid digits')
##    a=(input('enter a number you want to multiply '))
##    b=(input('enter another number you want to multiply '))
##else:
##        a=int(a)
##        b=int(b)
##        print('The product of both numbers is',a*b)
##
##price=float(input('What is the price of your item '))
##amount=float(input('How much money is the customer paying you '))
##change=amount-price
##print('the amount of change given will be','$',change)
        
##price=(input('What is the price of your item '))
##amount=(input('How much money is the customer paying you '))
##while price.count('.')>1 and amount.count('.')>1:
##    print('Invalid price')
##else:
##    
##change=amount-price

##price=(input('What is the price of your item in decimal form '))
##dot_count=price.count('.')
##dot_index=price.find('.') 
##wholepart=price[:dot_index]
##decipart=price[dot_index+1:] 
##
##
##while dot_count !=1 or decipart.isdigit()==False or wholepart.isdigit()==False:
##    print('invalid number')
##    price=(input('What is the price of your item '))
##    dot_count=price.count('.')
##    dot_index=price.find('.') 
##    wholepart=price[:dot_index]
##    decipart=price[dot_index+1:] 
##else:
##  price=float(price)
##
##amount=(input('How much money is the customer paying you in decimal form '))
##dot_count=amount.count('.')
##dot_index=amount.find('.')
##wholepart=amount[:dot_index]
##decipart=amount[dot_index+1:]
##while dot_count !=1 or decipart.isdigit()==False or wholepart.isdigit()==False:
##    print('invalid number')
##    amount=(input('What is the amount customer is paying you'))
##    dot_count=amount.count('.')
##    dot_index=amount.find('.')
##    wholepart=amount[:dot_index]
##    decipart=amount[dot_index+1:]
##else:
##    amount=float(amount)
##if price==amount:
##    print('you do not owe any cash')
##elif price>amount:
##    print('you are short of ', price-amount,'$')
##else:
##    print('you need to return', amount-price,'$')
##
####
##w=input('write a string:  ')
##capitalcounter=0
##for letter in w:
##    if letter.isupper():
##        capitalcounter+=1
##print('you have',capitalcounter,'capital letters in your string')
##
##a=input('Enter a password: ')
##if a.isupper()== False or a.isalpha()==True:
##    print('A stronger password would be',a[0].upper()+a[1::],'or',end=' ')
##    a=a.replace('a','@')
##    a=a.replace('s','$')
##    a=a.replace('l','|')
##    print(a)
##  
