import random as r
valid_words=[]
with open ('Collins Scrabble Words (2019).txt','r') as f:
    for line in f:
        word=line.split('\n')
        valid_words.append(word[0])
##    print(valid_words[0:15])

##def int_input(prompt):
##    num=input(prompt)
##    while num.isdigit()==False:
##        print('Invalid input')
##        num=input(prompt)
##    return int(num)
##
##n=int_input('Enter your number: ')
##print(n,type(n))

##def str_input(prompt):
##    letter=input(prompt)
##    while letter.isalpha()==False:
##        print('Invalid input')
##        letter=input(prompt)
##    return str(letter)
##a=str_input('enter a letter: ')
##print(a,type(a))
TILES = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A',
         'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'R', 'T', 'N',
         'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'L', 'S', 'U', 'L', 'S', 'U', 'L',
         'S', 'U', 'L', 'S', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'C', 'M', 'P', 'B', 'C', 'M', 'P',
         'F', 'H', 'V', 'W', 'Y', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
def get_new_tiles(num):
    hand= r.sample(TILES,num)
    for tiles in hand:
        TILES.remove(tiles)
    return hand

h=get_new_tiles(5)
print(h)
##print(TILES)
##
tile_to_points = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                  'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
                  'Q': 10, 'Z': 10}


def print_hand(hand):
    for tile in hand:
        points=tile_to_points[tile]
        print(tile,':',points)
print_hand(h)

def get_points(word):
    total_points=0
    for letter in word:
        points=tile_to_points[letter]
        total_points+=points
    return total_points
print(get_points('ZEBRA'))


def is_valid_play(word,hand):
    if len(word)>7 or len(word)<1:
        return False
    word=word.upper()
    if word not in valid_words:
        return False
    for letter in word:    
        if letter not in hand:
            return False
        if word.count(letter)>hand.count(letter):
            return False
    return True
print(is_valid_play('dOG',['D', 'G', 'O','H', 'A', 'V', 'B']))

player_to_points={'Avah':20,'shreya':19,'bob':10,'luna':32}
def get_winner():
##    b=player_to_points.values()
##    print(b)
    max_points=max(player_to_points.values())
    print(max_points)
    for name,points in player_to_points.items():
        if points==max_points:
            return name.title()
print(get_winner())
def maxpoints():
    max_points=max(player_to_points.values())
    print(max_points)
    for mazx,points in player_to_points.values():
        if points==max_points:
            return mazx
    

print('The winner of the game is',get_winner(),'with', max(player_to_points.values()),'points')
a = {'peter':'RABBIT','ron':'LEMON','jess':'UNICORN'}
##print(player_to_words.values())
def get_best_word(player_words):
    best_word=''
    best_score=0
    for word in player_words:
        if score>best_score:
            score=get_points(word)
            best_score=score
            best_word=word
        return best_word

<ASCII/Latin1>
AaBbCcDdEeFfGgHhIiJj
1234567890#:+=(){}[]
¢£¥§©«®¶½ĞÀÁÂÃÄÅÇÐØß

<IPA,Greek,Cyrillic>
ɐɕɘɞɟɤɫɮɰɷɻʁʃʆʎʞʢʫʭʯ
ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκ
БбДдЖжПпФфЧчЪъЭэѠѤѬӜ

<Hebrew, Arabic>
אבגדהוזחטיךכלםמןנסעף
ابجدهوزحطي٠١٢٣٤٥٦٧٨٩

<Devanagari, Tamil>
०१२३४५६७८९अआइईउऊएऐओऔ
௦௧௨௩௪௫௬௭௮௯அஇஉஎ

<East Asian>
〇一二三四五六七八九
汉字漢字人木火土金水
가냐더려모뵤수유즈치
あいうえおアイウエオ
        
   
