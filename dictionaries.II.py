zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries","Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini","Libra", "Aquarius"]}
print(zodiac_elements.get('earth'))
print(zodiac_elements.get('fire'))

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam":123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id=user_ids.get('teraCoder',100000)
print(tc_id)
stack_id=user_ids.get('superStackSmash',100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir":20, "strength sandwich": 25, "stamina grains": 15, "power stew": 3}
available_items.pop('power stew')
available_items.pop('stamina grains')
print(available_items)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22,"lists": 19, "classes": 18, "dictionaries": 18}
lessons=num_exercises.keys()
total=num_exercises.values()
print(lessons)
print(total)

women_in_occupation = {"CEO": 28, "Engineering Manager": 9,"Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer":9}
for info, value in women_in_occupation.items():
    print('Women make up',str(value),'percent of', info+'s')


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries","Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini","Libra", "Aquarius"]}

print(zodiac_elements.get('air'))


tc_id=user_ids.get('superCoder',100000)
print (tc_id)

stack_id= user_ids.get('fakeUser',100000)
print(stack_id)

fruits = {"apples": 10, "banana": 5, "berries": 20, "grapes": 25, "melon": 15,"pear": 30}
print(fruits)
fruits.pop('berries')
fruits.pop('melon')
print(fruits)

coding_languages = {"scratch": 10, "python": 13, "HTML": 15, "CSS": 22, "Java":19, "C": 18, "Javascript": 18}
lessons=coding_languages.keys()
total=coding_languages.values()
print(lessons)
print(total)

men_in_occupation = {"CEO": 28, "Engineering Manager": 9,"Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer":9}
for info, value in men_in_occupation.items():
    print('Men make up',str(value),'percent of', info+'s')









