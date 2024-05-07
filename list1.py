##password = "U1tra_Secret_P@ssw0rd"
##c = 0
##s = 0
##d = 0
##for character in password:
##    if not (character.isalnum()):
##        s+= 1
##    elif not character.isalpha() and character.isalnum():
##        d += 1
##    elif character.isupper():
##        c+= 1
##if c>= 2 and d >= 2 and s >= 2:
##    print("That's a strong password!")
##else:
##    print("You should try to make a stronger password!")
### the best way to store a name is as a string! Use quotes!
##friends = ["Noah", "Marny", "Lisa", "Gurpreet", "Isaac"]
### each name is a string, separated by commas
### oops! I forgot a name! Here's one way to add another one
##friends = friends + ["Jenny"] # this is list concatenation
### just like string concatenation, it makes a new list
### with all the elements from each list on the right
### in the same order they are added in
##print(friends) # this will print the whole list at once
##print(len(friends)) # the len function works on lists too
### a list is a collection, so we can loop through it
##for name in friends: # just like we loop through strings
##    print(name, "is invited to my party!")
##num=[1,2,3,4,5,6]
##
##a=int(input('What index value do you want'))
##
##print('The number',num[a],'is found at this index')
##
##   
##list = ['a', 'b', 'c', 'e', 'f']
####where_is_c = list.index('c') # where_is_c is the index of 'c'
####number_of_sevens = list.count(7)
####number_of_as = list.count('a')
####print(where_is_c,number_of_sevens,number_of_as)
##
##classvote=["Jen", "Jayden", "Jared", "Jen", "Jen", "Jayden", "Jayden", "Jen"]
##jencounter=0
##for name in classvote:
##    if name=='Jen':
##        jencounter+=1
##print('jen appears',jencounter,'times')
##jaydencount=classvote.count('Jayden')
##jaredcount=classvote.count('Jared')
##print('jared appears',jaredcount,'times')
##print('jayden appears',jaydencount,'times')
##friends_names = ["jeremy", "jason", "jaymit", "river",
##"lily", "jen", "ben", "harley", "frida"]
##friends_names= friends_names+['prisha','lisa','nathan']
####j_initialcount=0
####for name in friends_names:
####    if name[0]=='j':
######        j_initialcount+=1
######print(j_initialcount)
######
####for name in friends_names:
####    print(name.title())
####alphabet=['a','b','c','d']
####while True:
####    for a in alphabet:
####        print(a)
####    choice=input('enter y to modify the list')
####    if choice=='y':
####        insert=input('what do you wanna add')
####        alphabet.append(insert)
##alphabet=['a','b','c','d']
##while True:
##    for a in alphabet:
##        print(a)
##    choice=input('enter y to modify the list or n to stop ')
##    if choice=='y': 
##        indice=(input('which index '))
##        insert=input('what do you wanna add ')
##        while indice.isdigit()==False or int(indice)<0 or int(indice)>(len(alphabet)-1):
##            print('Invalid indices ')
##            indice=input('which index ')
##        else:
##            alphabet[int(indice)]=insert
##    if choice=='n':
##        break
##             
#### string is sequence of letters, list is a sequence of anything. Ex; floats,string, numbers
##        
# I am writing a book about a small dinosaur
# this program will help me pick the best title
titles = ["the littlest dinosaur", "tiny dinosaur",\
"itsy bitsy dino", "the dinosaur that never growed"]
# there is a mistake! Use item assignment to change the item
# the dinosaur that never growed to the dinosaur that never grew
# titles should have proper capitalization, let's change that
for i in range(len(titles)):
titles[i] = titles[i].title()
print(titles)
# my publisher tells me shorter titles are better!
long_titles = []
good_titles = []
for title in titles:
if len(title) > 20: # 20 characters is the limit
long_titles += [title]
else:
good_titles += [title]
# now we split it up into long and short titles
print(long_titles)
print(good_titles)
best_title = good_titles[?]
# replace ? with the index of your favouri
