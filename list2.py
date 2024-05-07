####### I am writing a book about a small dinosaur
####### this program will help me pick the best title
######titles = ["the littlest dinosaur", "tiny dinosaur",\
######"itsy bitsy dino", "the dinosaur that never grew"]
####### there is a mistake! Use item assignment to change the item
####### the dinosaur that never growed to the dinosaur that never grew
####### titles should have proper capitalization, let's change that
######for i in range(len(titles)):
######    titles[i] = titles[i].title()
######print(titles)
####### my publisher tells me shorter titles are better!
######long_titles = []
######good_titles = []
######for title in titles:
######    if len(title) > 20: # 20 characters is the limit
######        long_titles += [title]
######else:
######    good_titles += [title]
####### now we split it up into long and short titles
######print(long_titles)
######print(good_titles)
######best_title = good_titles[0]
######print(best_title)
####### replace ? with the index of your favouri
####numbers = [3,2,1]
####numbers.sort()
####print(numbers) # the list stored in numbers is DIFFERENT now
####student = "Liam"
####student.upper()
######print(student) # what does this prin
######student = student.upper()
######print(student) # now we print "LIAM
######weekdays = ['monday', 'tuesday']
######weekdays = weekdays.append('wednesday')
######print(weekdays)
######cities = ['oakville', 'niagara falls', 'toronto', 'vaughn']
######cities.append('brampton')
######first = cities[0]
######cities[0] = cities[0].upper()
######print(cities[1].upper())
####favanimal=['dog','girafe','cat','ferret','pig']
####favanimal.insert(2,'Chameleon')
####print(favanimal)
####favanimal.remove('pig')
####print(favanimal)
####favanimal.sort()
####print(favanimal)
####for a in range (len(favanimal)):
####    favanimal[a]=favanimal[a]+'!'
####print(favanimal)
####best_animals=favanimal[0:3]
####
####print(best_animals)
######
#########A string is a collection of characters,symbols,letters
#########A list is a collection of anything you want-strings,floats,integers
###mutability is a term that describes of piece of datas ability to change-mutable
####country_list=[]
####while True:
####    name=input('enter a country name ')
####    if name=='Done':
####        break
####    country_list.append(name.title())
####    print(country_list)
####country_list.sort()
####print(country_list)
####while len(country_list)!=0:
####    print(country_list.pop(0))
####
####print(country_list)
######
##cities = ["Portland", "San Francisco", "Houston", "Boston"]
##states = ["Oregon", "California", "Texas", "Massachusetts"]
##city_state=[]
##for a in range(len(cities)):
####    temp=cities[a]+', '+states[a]
####    city_state.append(temp) 
####print(city_state)
##days = ["monday", "wednesday", "thursday"]
##days.insert(1,'tuesday')
##days.append('friday')
##days.extend(['saturday','sunday'])
##print(days)
##
################
################blanklist=[]
################
################while True:
################    a=input('do you want to create a list, enter yes if so ')
################    if a!='yes':
################        break
################    else:
################        b=input('enter y to add to the list, enter n to remove from the list ')
################        if b=='y':
################            add=input('What will you add ')
################            blanklist.append(add)
################            print('this is your current list: ',blanklist)
################        elif b=='n':
################            subt=input('What will you delete ')
################            blanklist.remove(subt)
################            print('this is your current list: ',blanklist)
################        else:
################            print('This is your list: ',blanklist)
