###function is a chunk of code that accomplishes a task
##
##big=max(4,3,2,1)
##print(big)
##print(max(4,6,7,8))
##
##def print_helpinfo():
##    print("Welcome to Brick Breaker 3000")
##    print("--------CONTROLS-------")
##    print("\tUse arrow keys to move!")
####    print("\tUse space to shoot!")
####print_helpinfo()
##
####
##def add():
##    a= float(input('enter #'))
##    b=float(input('enter #'))
##    c=a+b
##    print('sum is equal to',c)
####add()
##
##def sub(a,b):
##    c=a-b
##    print(c)
####sub(50,5)
####x=float(input('number?'))
####y=float(input("number?"))
####c=sub(x,y)
##
##def multi(a,b):
##    c=a*b
##    return c
##
############################################################print('the answer is',multi(4,5))
############################################################a=float(input('enter num'))
############################################################b=float(input('enter num'))
############################################################c=multi(a,b)
############################################################print('answer is', c)
############################################################
############################################################def div():
############################################################    a=float(input('enter num'))
############################################################    b=float(input('enter num'))
############################################################    c=a/b
############################################################    return c
############################################################print(div())
############################################################
############################################################def print_player_data(username, highscore, attempts):
############################################################    print("PLAYER NAME: ", username)
############################################################    print("has a highscore of: ", highscore)
############################################################    print("after a total of attempts", "attempts")
############################################################    print_player_data("2Cool4School", 125, 10)
############################################################    print_player_data("JUnKR@T", 25)
##########################################################def brick_points(type):
##########################################################    if type == "common":
##########################################################        points = 10
##########################################################    elif type == "rare":
##########################################################        points = 50
##########################################################    elif type == "legendary":
##########################################################        points = 100
##########################################################    return points # points is what is returned
##########################################################score = 0
########################################################### hit a common brick, that's 10 points - add this value to score
##########################################################score = score + brick_points("common")
##########################################################print(score)


##
##def print_triangle():# since its task is to print a triangle
##    a=int(input('enter num'))
##    for i in range(a): # it does not need any input, or give output
##        print("@" * i)
##print_triangle()

##def ask_silly_question(): # the body of the function does not have
##    input("Press any key to continue: ") # to just print something
##for a in range(2):
##    ask_silly_question()

##import random
##def guess_my_number(): # bodies can be as complicated as you need
##    my_number = random.randrange(1,10)
##    guess = int(input("Guess a number between 1 and 10! "))
##    if guess == my_number:
##        print("You guessed it right!")
##    else:
##        print("Wrong! My number was", my_number)
##
##while True:
##    guess_my_number()
##    ch=input('enter y to try again')
##    if ch!='y':
##        break

### TYPE 2 EXAMPLES
##def double(): # our parameter is x, which can be anything
##    a=float(input()) # we do NOT write a number as our parameter
##    c=a*2
##    return c
##print(double())# we write the number when we CALL it, as the argument

##def print_stars(number_of_stars): # use descriptive parameter names
##    number_of_stars= int(number_of_stars)
##    print("*" * number_of_stars)
##print_stars(60)
# what would happen if I wrote: print_stars("ten") ?

##def print_ticket_price(type, discount):
##if type == "child":
##print("Child tickets cost $3.99")
##elif type == "senior":
##print("Senior tickets cost $5.49")
##elif discount: # we expect discount to always be True or False
##print("Adult ticket with Family Discount is $6.25")
##else:
##print("Adult ticket, no discount, costs $7.25")
####print_ticket_price("senior", False)
####print_ticket_price("adult", True)
#### what happens when you call this function with 1 argument?
####
#### TYPE 3 EXAMPLES
####def get_sum(x, y):
####    x=float(x)
####    y=float(y)
####    return x + y
####print(get_sum(3.5,.2))
##
##def is_adult(age):
##    if age > 17:
##        return True
##    else:
##        return False
#### this function has multiple return statements, but you can see that
#### no matter what argument is passed in for 'age', it always returns
#### just one value. There is no way the code can reach both returns!
##
##a = is_adult(89) # what is stored in variable a?
##if is_adult(10): # if is adult(10) evaluates to True, it will print
##    print("10 year olds are adults") # will this be printed?
##    
##user_age = int(input("How old are you?" ))
##if is_adult(user_age): # it only prints if they enter 18 or higher
##    print("You are an adult.")
##is_adult(99) # where is the return value goin

import turtle
rain=turtle.Turtle()
rain.speed('fastest')
def draw_rectangle():
    for i in range(2):
        rain.forward(30)
        rain.left(90)
        rain.forward(75)
        rain.left(90)
##draw_rectangle()

def draw_colour_triangle(c):
    rain.color(c)
    for i in range (3):
        rain.forward(50)
        rain.left(120)
##draw_colour_triangle('blue')

import random
def get_random_colour():
    colours=['blue','red','yellow','green','pink','purple','orange',]
    clr=random.choice(colours)
    return clr

while True:
    draw_colour_triangle(get_random_colour())
    rain.left(5)
    draw_rectangle()
