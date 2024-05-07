##menu = {'oatmeal': 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
##print(menu)
####students_in_classes = {"software design": ["Aaron", "Delila","Samson"], "cartography": ["Christopher", "Juan", "Marco"],"philosophy": ["Frederica", "Manu"]}
####To add a single key : value pair to a dictionary, we can use the syntax:
##my_dict["new_key"] = "new_value"
##For example, if we had our menu object from the first exercise:
##menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5,
##"blueberry mun": 2}
##and we wanted to add a new item, "cheesecake" for 8 dollars, we
##could use:
##menu["cheesecake"] = 8
##If we wanted to add 3 new rooms, we could use:
######sensors.update({"pantry": 22, "guest room": 25, "})
####
####breakfast={'milk':4,'eggs':3,'bread':2,'cake':5}
####print(breakfast)
####
####my_empty_dict={}
####print(my_empty_dict)
####
####animals_in_zoo={'zebras':8,'monkeys':12,'dinosaurs':0}
####print(animals_in_zoo)
##
##user_ids= {"teraCoder": 9018293, "proProgrammer": 119238}
##user_ids.update({'theLooper':138475,'stringQueen':85739})
##print(user_ids)
##
####oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature":"Zootopia"}
####oscar_winners["Supporting Actress"]="Viola Davis"
####oscar_winners["Best Picture"]="Moonlight"
####print(oscar_winners)
##
##students = {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
##students["James"]=77
##students['Sam']=66
##print(students)
##
##morning={'coffee':2,'bagel':3,'donut':1,'sandwich':5}
##print(morning)
##
##empty_dict={}
##empty_dict['soccer']=7
##empty_dict['rugby']=9
##empty_dict['basketball']=11
##print(empty_dict)
##user_ids.update({"cuteDUCK":178375,'sweetPie':92537})
##print(user_ids)
##
##movies= {"Best Picture": "Mickey Mouse", "Best Actor": "Mickey", "Best Actress": "Minnie", "Animated Feature": "Mouse"}
##movies['Supporting Actress']='Anyone'
##movies['Best Picture']='Frozen'
##
####fruits = {'apple': 6, 'strawberry': 7, 'watermelon': 3, 'pineapple': 4}
####fruits.update({'orange':17})
####fruits['watermelon']=5
####print(fruits)
##
empty_dict={}
print('create list of country and capitals')
while True:
    why=input('write y to enter a value, n to stop, d to delete ')
    if why=='y':
        h=input('enter country ')
        b=input('enter capital city ')
        empty_dict[h]=b
        print(empty_dict)
    elif why=='n':
        print(empty_dict)
        break
    elif why=='d':
        c=input('what country you wanna delete')
        empty_dict.pop(c)
        print(empty_dict)
##  
##biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80,"Coca-Cola": 69.7, "Amazon": 64.8}
##for company, value in biggest_brands.items:
##    print(company + " has a value of " + str(value) + " billion dollars.")
        
