####secret_word = "Cat"[0] + "Dog"[1] + "Bird"[3] + "Snake"[4] + "r"
####print(secret_word)
####
####my_name = input('Enter your name ')
####first_letter = my_name[0]
####print(first_letter)
####
######last_letter = my_name[len(my_name) - 1]
######print(last_letter)
####first= input('What is your first name')
####last= input('What is ur last name')
####firstinitial= first[0]
####lastinitial= last[0]
####print('Your initials are',firstinitial+lastinitial)
##string = "Blueberry Pancakes!"
##print(string[0:9:2])
### step is 2, meaning our slice includes index 0, 2, 4, ...
### so this will print "Bubry"
##print(string[4:9:1]) # this prints 'berry'
### We do not need to use 3 inputs all the time
### If you omit the step, it assumes you want your step to be 1
##print(string[4:9]) # so this is the same! it also prints 'berry'
### You don't even need to give it a start or end!
### If you omit the start, it starts at the beginning
##print(string[:9])
### this is the same as string[0:9:1], so it prints "Blueberry"
###f you omit the end, Python assumes you want to go to the end
##print(string[10:])
### this is the same as string[10:19:1] so it prints "Pancakes!"
### What if you omit everything?
##print(string[:]) # what will be printed here?
### What about a negative index?
##print(string[19:9:-1])
### this starts with index 19, then moves -1 steps to index 18
### then 17, 16, all the way until (but not including) index 9
##### So this prints '!sekacnaP', which is 'Pancakes!' backwards!
##### with negative indices, start has to be BIGGER than the end
####print(string[::-1])
##### this is how you omit start and end but include a step
##### what should this print?
##a='Strawberry shortcake'
##print(a[0],a[11],a[-9],a[-20])
##
##a=input('what is your full name ')
##print('The first letter of your name is',a[0])
##print(a[::-1])
##
##message = "ccowdcionygy nrzuclwepsq!q"
##print(message[0::2])
##name= 'Justin Timberlake'
##print(name[7::]+name[0:6:])

##secret = "isagbnxiwrptysu ctuueogbyal hlklrae qweoinbkp zusoyY"
##print(secret[::-2])
##
##address='5 washington drive'
##print(address[2::])
##print(address[0])
##a='ThE pirates of the carribean' #27characters
##print(a[2],a[9],a[17],a[25],a[-26],a[-19],a[-11],a[-3])
##
##sm='LLLsaebccrdeetZ nmfegshsiajgkeb:s)dMM'
##print(sm[3:-3:2])
##sm=' sushiiIi lllooovvveee   cccooo0ookkkiiieeessspumpkin'
##print(sm[6:-7:3])


