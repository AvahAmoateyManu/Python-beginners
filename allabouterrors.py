################################################name = input("What is your name?")
################################################if len(name) > 8:
################################################  print("Your name is quite long!")
################################################elif len(name) < 4:
################################################  print("Your name is quite short!")
################################################if name == "Jakob":
################################################  print("We have the same name!")
################################################else:
################################################  print(name, "is a lovely name!")
#Five types of errors: Name errors, Type errors, Syntax errors, Logic errors, Indentation Errors.

#1. name error is when you do not define a variable or write function improperly. type error is when you use data types incorrectly.
#Indentation error is when you add or remove an indent in Python
#Logic error is when your code is right, but does not do what you want it to
#Syntax error is when you did not write something properly. Ex: print with all caps or forgot comma
#


##2.
##Input('Give me a random number')
#3
##print(0.5*"five")
#4
##print "How are you"
###5
##i=int(input('write an integer')
##
##if i>0:
##print('That is not a negative number')
##elif i<0:
##print('That is a negative number')
##print('2x4 =', 2/4)





print("Welcome to my super hard MATH QUIZ!\n\nGet 4 points to be a Rookie, 6 points to be a Big Brain Beginner, 8 points to be a Super Scientist, and 10 or more points to be Mathematical Magician!")
print("Answer the questions right to gain 2 points. Get one wrong and you lose 2 points\n\n You start with 4 points")
points = 4
answer1 = int(input("What is 5 * 3 + 1 : "))
if answer1 == 16:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer1 != 16:
    points = points - 2
    print("INCORRECT! The answer was 16. Score: ", points)

answer2 = int(input("What is (3 + 1) * 2 + 1 : "))
if answer2 == 9:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer2 != 9:
    points = points - 2
    print("INCORRECT! The answer was 9. Score: ", points)
answer3 = int(input("What is 3 * 5 * 2 : "))
if answer3 == 30:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer1 != 30:
    points = points - 2
    print("INCORRECT! The answer was 30. Score: ", points)
answer5 = int(input("What is 11 - 5 * 2 + 2 : "))
if answer5 == 3:
    points += 2
    print("CORRECT! Score: ", points)
else:
    points = points - 2
    print("INCORRECT! The answer was 3. Score: ", points)

answer6 = int(input("What is 100 * 101 : "))
if answer6 == 10100:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer6 != 10100:
    points = points - 2
    print("INCORRECT! The answer was 10100. Score: ", points)

print("END OF TEST! Let's see your score!")

if points < 4:
    print("Score: ", points, "Try the test again!")
elif points == 4:
    print("You have a score of 6! Rookie Score!")
elif points == 6:
    print(" A score of 8! That makes you a Big Brain Beginner!")
elif points == 8:
    print("WOAH! A score of 10 makes you a Super Scientist!")
elif points > 10:
    print(points,"points! That is more than 10 points! We have a Mathematical Magician over here!")

