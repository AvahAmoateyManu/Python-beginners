##############################################name = input("What is your name?")
##############################################letter = input("What is your favourite letter?")
##############################################letter_count = 0
##############################################vowel_count = 0
##############################################for char in name:
##############################################    if char == letter:
################################################# this is short for letter_count = letter_count + 1
##############################################        letter_count += 1
##############################################    if char in "aeiouAEIOU":
##############################################        vowel_count += 1
##############################################print("You have", letter_count,\
##############################################"instances of your favourite letter", letter,"in your name!")
##############################################print("You have", vowel_count, "vowels in your name.")
##############################################print("The total length of your name is", len(name = "Rumplestiltskin"
##name = "Rumplestiltskin"
##guess = "John"
##while guess != name: # stuck in this loop you guess correctly
##    print("I challenge you to guess my name!")
##    
##    guess = input("Enter your guess: ")
##print("Wow! You got it!")
##### The only way this print is reached is if you get it right!
##### if you always guess wrong, this loop could go forever
##age = 0
##while age < 100: # we will only leave the loop when age >= 100
## age += 1
##print(age)
##num = 0
##while num != 2:
##    num += 2
##
##game_completed = True
##while not game_completed: # this is a proper boolean condition
##    print("Keep playing!")
##dollars = 35
##while dollars < 20:
##    print("Insufficient funds.")
##x = 100
##while x != 300:
##    x = x - 5
##guess = "x"
##secret_letter = "b"
##
##name = "Rumplestiltskin"
##guess = "wrong guess"
##while guess != name:
##    guess = input("Enter a guess for my name: ")
##    if guess == "I give up!":
####        break
##
##while True:
##    print('iuytr')
##
##1<2
##while False:
##    print('smaller than 2')
##
##sw='purple'
##print('hint: It is a colour')
##g=input('guess a word: ')
##while g!= sw:
##    if g=='I dont know':
##        print('The correct word was purple')
##        break
##    print('Guess again')
##    g=input('guess a word: ')
##if g==sw:
##    print('You got the word')
##
##s=int(input('Enter a number '))
##while s%2==1:
##    s=int(input('Enter a number '))

##for a in range (2,8):
##    print(a)
##a=2
##while a<=8:
##    print(a)
##    a=a+1
#whileloop is easier because you can repeat the code.

##guess = int(input("Guess the number of marbles in the jar: "))
##number_of_marbles = 249
##while guess != number_of_marbles:
##    print("Incorrect guess! Try again!")
##    guess = int(input("Guess the number of marbles in the jar: "))
##if number_of_marbles==guess:
##   print('You got the answer!')
####

##a=input('Give me a number')
##while len(a)!=10 or a.isdigit()==False:
##    print('try again')
##    a=input('Give me a number')
##############################
##############################s='!@$%^&*.'
##############################counter=0
##############################a= True
##############################while a== True and counter<5:
##############################    p=input('Make your password: ')
##############################    for letter in p:
##############################        if letter in s:
##############################            print('you have a strong password')
##############################            a=False
##############################            break
##############################    counter+=1
##############################if counter==5:
##############################    print('You lost your attempts, come back later')
################################a= False
##for a in range(0,100,3):
##    print (a)
##num=0
##while num<101:
##    print(num)
##    num+=3
##while False:
##    print('ahhhhhhhhhhhhhhhaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssssshh')
    
####guess = int(input("Guess the number between 1-9: "))
####num = 7
####while guess!=num:
####    if guess>num:
####        print('enter a number smaller')
####    elif guess<num:
####        print('enter a bigger number')
####    print("Try again!")
####    guess = int(input("Guess the number between 1-9 : "))
####if num==guess:
####   print('You got the answer')

##word= 'regina'
##guess=0
##correcti=''
##print('Hint: This is a capital of a canadian province')
##while guess<6: 
##    g=input('guess the word ')
##    for letter in word:
##        if letter in g or letter in correcti:
##            correcti+=letter
##            print(letter ,end=' ')
##        else:
##            print('_',end=' ')
##    guess+=1
##    print('\nyour total chances equals',6-guess)
##



##while True:
##    print('Enter 1 for square\nenter 2 for triangle\nenter 3 for circle\nenter 4 to exit')
##    choice=int(input(' Do you want area for a square, a triangle or a circle? '))
##    if choice==1:
##        w=float(input('Enter your width '))
##        l=float(input('Enter your length '))
##        print('area of your square is',w*l)
##    elif choice==2:
##        h=float(input('Enter your height '))
##        b=float(input('Enter your base length '))
##        print('area of your triangle is',b*h/2)
##    elif choice ==3:
##        ch=input('Enter r if you know radius, enter d if you know diameter ')
##        if ch=='r':
##            r=float(input('Enter your radius '))
##            print('area of your circle is',r*r*3.14)
##        if ch=='d':
##            d=float(input('Enter your diameter '))
##            r=d/2
##            print('area of your circle is',r*r*3.14)
##    elif choice==4:
##        print('Thank you for using our services')
##        break
