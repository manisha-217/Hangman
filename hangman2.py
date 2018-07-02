
#importing the time module
import time

# set variable for level
i=1

#intro of player
name = input("What is your name? ")

#welcoming the user
print ("Hello ",  name ,"Time to play hangman!")

#start loop for level up
for i in range (9):
    
#print numering of reached level
    if i>=1:
       print("level up\n you are in level",i)

#wait for 1 second
    time.sleep(1)

    print ("Start guessing for level",i)

    time.sleep(0.5)

#import random for chosing diffrent word for diffrent level
    import random

#open that file which store the collection of word
    with open('test1.txt','r') as f:

#read the word of text file
         content=f.read().split()

#chose the random word for diffrent word 
    word=random.choice(content)



#creates an variable with an empty value
    guesses = ''

#determine the number of turns
    turns = 10

# Create a while loop

#check if the turns are more than zero

    while turns > 0:         

    # make a counter that starts with zero
        fail = 0             

    # for every character in secret_word    
        for char in word:      

    # see if the character is in the players guess
            if char in guesses:    
    
        # print then out the character
                print (char)    

            else:
    
        # if not found, print a dash
                print ("_")    
       
        # and increase the failed counter with one
                fail = fail+1    

    # if failed is equal to zero

    # print You Won
        if fail == 0:        
            print ("You won")  

    # exit the script
            break              

        print

    # ask the user go guess a character
        guess= input("guess a character:") 

    # set the players guess to guesses
        guesses +=guess            

    # if the guess is not found in the secret word
        if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
            turns =turns -1        
 
    # print wrong
            print ("Wrong")    
 
    # how many turns are left
            print ("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
            if turns == 0:           
    
        # print "You Loose"
                print ("You Loose")  

