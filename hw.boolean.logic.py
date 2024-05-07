##print (not( 100 > 10))
##print( 4==-4)
##print(0<=0)
##print('i' in 'team')
##print('team' not in 'teamwork')
##print('1' in '123')
##
##print(3 == 3 and 4 == 4)
##print('A' != 'a' and 'b' in 'bob')
##print(not 3 == 4) or (not 4 < 5)
##print(6 <= 7 or 2 + 5 == 7)
##
##print(max(1,2,3 < 3))
##print(len('C' + 'oding') == 10)
##print(min(3,2,1) != min(23, 78, 1))
##print(round(2.3) != 2)
##print(2 + 4 == len('python'))
##print(int(3) == round(3.1))
##
##deci1= float(input(' Give me a random decimal number'))
##print(deci1,'is equal to or greater than 10:',deci1>= 10)
##word0='Supercalifragilisticexpialodocious'
##word1= input('Write the longest word you know ')
##print(len(word1)>len(word0))
##
##answer0='A coin'
##answer1= input(' What has a head and a tail, but no body?: ')
##print('Your answer is: ',answer1 == answer0)

answer1= 'jungle'

guess1= input(' Guess your letters/word: ')
print(guess1.lower() in answer1 or guess1.lower()==answer1)

guess1= input(' Guess your letters/word: ')
print(guess1.lowr() in answer1 or guess1==answer1)

guess1= input(' Guess your letters/word: ')
print(guess1 in answer1 or guess1==answer1)

guess1= input(' Guess your letters/word: ')
print(guess1 in answer1 or guess1==answer1)

guess1= input(' Guess your letters/word: ')
print(guess1 in answer1 or guess1==answer1)

guess1= input(' Guess your letters/word: ')
print(guess1 in answer1 or guess1==answer1)

print('The true word was', answer1)
