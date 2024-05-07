##for letter in 'Hello world':
##    print(letter)
##
##for i in range(10,0,-1):
##    print(i)
##
##for i in range(2,9):
##    print(i) # print each number from 2 to 9 one at a time
##for i in range(2,9):
##    print(i + 1) # what do you think this one will print?
##for num in range(5):
##    print("!") # we can print anything in the loop
### the loop above will print the exclamation mark (!) 5 times!
##    num = 0
##for i in range(10):
##    num = num + 10 # we can do more than just print too
##    print(num)
##
##for a in range(4,40,4):
##    print(a)

# what will the loop above print out? Try running it
##for character in "Horton Hears a Hoo":
##    if character != "H": # what will be printed out here?
##        print(character)
##for letter in "The Quick Brown Fox Jumps Over The Lazy Dog":
##    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
##        print(letter)
### the loop above goes through all letters in the sentence, and
### only prints them if they are capital letters!
##for i in range(0, 100, 3):
##    print(i)
### this loop will only print multiples of three!
##### This is because of our range call
##count = 0
##word=input('What is your name ')
##l=input('What is your favorite letter ')
##for letter in word:
##    if letter == l:
##        count = count + 1
##print('Number of time',l,'occurs',count)
### this will increase the variable only when letter is a
### so it will count the number of a's in Samantha

##a=input('What is your name ')
##for b in range(10):
##    print(a*b)

##q='twinkle twinkle little star. how i wonder what you are'
##
##for letters in q:
##    if letters in 'aeiou':
##      print(letters)

##for a in range(0,20,2):
##    print(a)
##total=0
##for b in range(1,101):
##    total=total+b
##print(total)
##
##bcount=0
##
##for letters in 'Barry B':
##    if letters =='B':
##        bcount=bcount+1
##
##
##print(bcount)

##import turtle
##i=turtle.Turtle()
##shape=int(input('What polygon do you want'))
##angle=360/shape
##for a in range(shape):
##    i.forward(100)
##    i.left(72)
##
##for b in range(1,7):
##    print(b*'*')
##    
##for b in range(7,1,-1):
##    print(b*'*')

#An iterator variable defines what is coming next in a sequence

##word=input('What is your favorite word')
##l=input('What is your favorite letter ')
##count=0
##for letter in word:
##    if letter == l:
##        count = count + 1
##print('Number of time',l,'occurs',count)
##
##for a in range(0,105,5):
##    print(a)

#In forloop, to use range, you must write 'for' then the iterator variable then you write range and bracket you write in integer, the beginning number of the sequence, the ending number of the sequence and the number it is being counted up by, close brackets. The, colons and print it.
##spaces=0
##c=input('enter a sentence  ')
##for b in c:
##    spaces=spaces+1
##print(spaces)


##x= int(input('Pick a random number '))
##print('Your numbers multiplication table is equal to')
##for a in range(1,11,1):
##    print(x,'x',a,'=',x*a)
##
##
##
####
##x= int(input('Pick a random number '))
##b=int(input('What number do you want to start from? '))
##c=int(input('What number do you want to end at? '))
##print('Your numbers multiplication table is equal to')
##for a in range(b,c+1,1):
##    print(x,'x',a,'=',x*a)

##
##a= int(input('Pick a random number '))
##print('Your numbers fact0rs are equal to')
##for x in range(1,a+1):
##    if a%x==0:
##        print(x)
##
##word='rose'   
##print('Guess my word')
##o=7
##for i in range(7):
##    g=input('Guess a letter: ')
##    for letter in word:
##        if letter==g:
##            print('You guessed a letter, keep going')

            



