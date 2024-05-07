##secret = ['O', 'l', ' ', 'e'] # we are assembling a secret
##secret.insert(1, 'n') # message!
##secret.insert(3, 'y')
##secret.insert(5, 'g') # write the list down on paper
##secret.extend(['n', 'i', 'u']) # and track the changes
##secret.append('s') # to find out what the list
##secret.append('e') # becomes
##secret.append('s')
##for letter in " can read":
##    secret.append(letter)
##piece = " 012012t,,,h987i+++s823!" # when you are done,
### copy and run the code
##num = len(secret) # to see if you were right!
##for character in piece:
##    if character.isalpha() or character == " ":
##        secret.insert(num, character)
##num += 1
##print(secret) # this will print a list of characters
##string = "".join(secret)
##print(string)
### use this syntax to import the whole library
##import random
### use this syntax if you only need one or two things
##from math import floor
##print(random.choice(['a', 'b', 'c'])) # using a module function
##
##import math
##print(math.floor(2.5)) # 2.5 rounded down is 2!
##print(math.ceil(2.5)) # 2.5 rounded up is 3!
##print(math.fabs(2.5)) # gives us 2.5
##print(math.fabs(-2.5)) # ALSO gives us 2.5
##print(math.isclose(25,30,rel_tol = 10))
### 25 and 30 are less than 10 apart so this is True
##print(math.isclose(3,4,rel_tol = 0.05))
### 3 and 4 are more than 0.05 apart so this is False
##print(math.pow(2,3)) # 2 to the power of 3 is 8
##print(math.sqrt(16)) # square root of 16 is 4
##print(math.floor(math.pi)) # pi (3.14159...) rounded down is 3
##print(3 > math.inf) # False! 3 is not bigger than i
##import random as r # now i can type r instead of the module name
##col = [2,3,7,8,34,6,78,0,11,6]
##print(r.choice(col))
##print(r.randrange(1,10,2)) # some random odd number from 1-10
##print(r.randrange(10)) # some random number from 0 - 10
##print(r.sample(col, 3)) # 3 random UNIQUE items from col
##print(r.choices(col, k=9)) # 9 random items from col (may repeat)
##
##import math as m
##import random as r
##floar=[3.75,4.5,0.8,7.4]
##print('round UP',r.choice(floar),'to the nearest number')
####b=r.choice(floar)
####while True:
####    a=input('Write your answer here:  ')
####    if a!=b:
####        print('wrong answer, try again')
##
####from datetime import datetime as dt
####print(dt.now())
####print(dt.now().weekday())
####print(dt.now().date())
####print(dt.now().time())
##import turtle
##shelly = turtle.Turtle() # shelly is our turtle object
##shelly.forward(100) # use the same syntax as list or string methods
##shelly.left(90)
##shelly.forward(100)
##shelly.left(90)
##shelly.forward(100)
######shelly.left(90)
######shelly.forward(100)
import random as r

######import math as m
######i=int(input('enter integer'))
##########print(m.pow(i,2))
######
####employees=['Emily','Josette','Arisha','Scarlett','Ryan','Nate','Hailey','Brock','Rex','Adam','Charlie','Stephanie','Benjamin','Sadie','Robbie']
####groupsize=int(input('how many employees do you need'))
####print(r.sample(employees,k=groupsize))
####import math as m
####a=float(input('what is the diameter of your circle'))
####print((m.pi*a),'is your circumference')
####      
import turtle
####a=turtle.Turtle()
##(a).color('blue')
##for i in range(5):
##    a.forward(100)
##    a.left(144)

##from datetime import datetime as dt
##weekdays=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
####day= dt.now().weekday()
####print(weekdays[day])
##
##sheldon=turtle.Turtle()
##steps=r.randrange(70)
##degrees=r.randrange(350)
##colours=["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink", "magenta"]
##while True:
##    colour=r.choice(colours)
##    print(colour)
##    sheldon.color(colour)
##    sheldon.forward(steps)
##    sheldon.left(degrees)
####colours=["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink", "magenta"]
####shape=int(input('how many sides does ur shape have '))
##degree=360/shape
##steps=int(input('how many steps '))
##colour=input('what colour is your shape ')
##if colour!=colours:
##          colour=r.choice(colours)
##sheldon.color(colour)
##for a in range(shape):
##    sheldon.forward(steps)
##    sheldon.left(degree)
