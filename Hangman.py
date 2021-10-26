import time
import random
import os


name = raw_input("Player's Name:")
print "Hello, " + name, "Time to play Hangman!"
time.sleep(0.5)

print "Loading Game",
dots='.....'
for i in dots:
    print i,
    time.sleep(0.5)

print "\nGuess the Movie Name..."
time.sleep(0.5)

words=['iron man','amelia','exorcist','the god father','titanic','deadpool','black panther','annihilation','red sparrow','sherlock holmes','aquaman','the ring','grudge','captain america']
word=random.choice(words)
guesses = ''
turns = 7
hang='HANGMAN'
while turns > 0:         
    failed = 0 
    for char in word:      
        if char in guesses:    
            print char,
        elif char==' ':
            print " ",
        else:
            print "_",     
            failed += 1    
    if failed == 0:        
        print "\nCongratulations!",name,"\nYou have won the game!"  
        break              
    inpt = raw_input("Guess a character:")
    guess = inpt.lower()
    if len(guess) <= 1:
        guesses += guess
    if guess not in word: 
        turns -= 1        
        print "Wrong Guess!"    
        print turns,"tries Left!\n",hang[:-turns]
        if turns == 0:
            print hang+"\nYou Loose!\nThe Correct Movie Name Was","'"+word+"'"
feedback=raw_input("\nGive your feedback here:\n")

fname=str(name)+" "+feedback[:2]+".txt"
direct=''
filename=os.path.join(direct,fname)
with open(filename,'w') as fw:
    fw.write(feedback)
    