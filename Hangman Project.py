#Hangman Project

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

choosen_word = " "
#import Hangman_words  #same as "import random" module
#or

#from Hangman_words import word_list 

# for char in random.choice(word_list):
#     choosen_word += char
# print(choosen_word)

#OR

word_list = [
'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 
'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon',  'buxom', 'buzzard', 'buzzing', 
'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 
'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 
'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 
'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 
'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 
'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 
'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 
'marquis', 'matrix', 'megahertz', 'microwave', 
'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 
'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 
'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 
'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 
'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress','transplant','triphthong', 'twelfth', 'twelfths','unknown', 
'unworthy', 'unzip', 'uptown', 'vaporize', 
'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism','walkway','waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 
'whomever', 'wimpy','witchcraft','wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 
'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']


choosen_word = random.choice(word_list)  #camel

lives = 6
#Testing Code
print(f"the solution is {choosen_word}")  #choosen_word = camel

display = []
# for letter in choosen_word:
#     display += '_'
# print(display)   

#or

for _ in range(len(choosen_word)):  #length of camel = 5 and in range(0,5)
    display += '_'  #display = display+ '_' upto length(i.e. 4th position from 0th position)
print(display)    #['_', '_', '_', '_', '_']

end_of_game = False
while not end_of_game:  #not False = True
    guess = input("Guess a letter: ").lower()   #user can guess a letter = a.lower()


    for guess in display:
        print(f"You've already guessed letter {guess}")


    for position in range(len(choosen_word)):   #it checks position of letter from choosen_word upto the lenght of choosen word
        letter = choosen_word[position]  # i.e. letter = position from choosen word
        if letter == guess:   
            #if letter(a) == guess(a) then it will display if not equal again go "for position in range(len(choosen_word))" to check letter == guess
            display[position] = letter   #put that letter in diplay variable on that position
        
    print(display)   #letter == guess == a i.e. ['_', 'a', '_', '_', '_']

    if '_' not in display:  #to check, if all the blank underscore gets fill 
        end_of_game = True  #just to fulfill "while condition - not end_of_game = Not False = True"
        print("You won.")  

    if guess not in choosen_word:    
        print(f"You guessed {guess}, that's not in word.")
        lives -= 1
        if lives == 0:  #from lives n to 0
            end_of_game = True #just to fulfill "while condition - not end_of_game = Not False = True"
            print("You lose.")   
    print(stages[lives])         
