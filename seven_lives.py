import random as r
lives=7
heart_symbol = u'\u2764'
words=['chair','bears','lions','teeth','plane']

secret_word=r.choice(words)
clue=['?','?','?','?','?']
guessed_word_correctly=False

def update_clue(guessed_letter, secret_word, clue):
    index=0
    while index< len(secret_word):
        if secret_word[index] == guessed_letter:
            clue[index]=guessed_letter
        index=index+1
        
while lives> 0:
    print(clue)
    print('Lives left:'+heart_symbol*lives)
    guess=input('Guess a letter or the whole word: ')

    if guess==secret_word:
        guessed_word_correctly= True
        break
    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print('incorrect, you lose a life')
        lives=lives-1
        
if guessed_word_correctly== True:
    print('You won, the secret word was',+ secret_word)
else:
    print('you lost, the secret word was',secret_word)

