import random                                                                           # To start my Game Project, I imported the "random" command.

playerX = 2                                                                             # These are my coordinates (x and y) for the player. My map has a grid of (0, 4) and my player is in the middle of my map, hence, the coordinates are (2, 2).
playerY = 2
treasureX = random.randint(0,4)                                                         # The treasure coordinates (x and y) are chosen randomly with the random feature imported at the top.
treasureY = random.randint(0,4)                                 
obstacleX0 = random.randint(0,4)                                                        # I used obstacle0 with its (x and y) randomly chosen coordinates for the first obstacle.
obstacleY0 = random.randint(0,4)
obstacleX1 = random.randint(0,4)                                                        # I used obstacle1 with its (x and y) randomly chosen coordinates for the second obstacle. 
obstacleY1 = random.randint(0,4)
obstacleX2 = random.randint(0,4)                                                        # I used obstacle2 with its (x and y) randomly chosen coordinates for the third obstacle.
obstacleY2 = random.randint(0,4)
obstacleX3 = random.randint(0,4)                                                        # I used obstacle3 with its (x and y) randomly chosen coordinates for the fourth obstacle.
obstacleY3 = random.randint(0,4)                               
extraCreditX0 = random.randint(0,4)                                                     # I used extraCredit0 with its (x and y) randomly chosen coordinates for my first extra credit challenge.
extraCreditY0 = random.randint(0,4)
extraCreditX1 = random.randint(0,4)                                                     # I used extraCredit1 with its (x and y) randomly chosen coordinates for my second extra credit challenge.
extraCreditY1 = random.randint(0,4)
extraCreditX2 = random.randint(0,4)                                                     # I used extraCredit2 with its (x and y) randomly chosen coordinates for my third extra credit challenge.
extraCreditY2 = random.randint(0,4)
extraCreditX3 = random.randint(0,4)                                                     # I used extraCredit3 with its (x and y) randomly chosen coordinates for my fourth extra credit challenge.
extraCreditY3 = random.randint(0,4)
extraCreditX4 = random.randint(0,4)                                                     # I used extraCredit4 with its (x and y) randomly chosen coordinates for my fifth extra credit challenge.
extraCreditY4 = random.randint(0,4)

def playerName():
    
    global yourName                                                                     # I am designating the variable "yourName" as a global variable to be able to use it outside of the function.
    
    yourName = raw_input("What is your name? ")                                         # This is the first "raw_input" asking the user for his/her name and informing him/her about the game's rules.
    print "\nWelcome to my game " + str(yourName.title()) + ". \n\nYou are about to embark on an adventure on a 5 x 5 grid map to find a hidden treasure. \nYou are in the middle of the map, and you have 20 moves to finish the game."
    print "Along the way, you will encounter obstacles or challenge questions. Answer them to continue your adventure, gain turns, or lose turns. \n\nTo move on the map use the following commands: up, down, right, or left (u, d, r, l)."
                                                                                        # I am printing the message to welcome the user, however, I am using the user's name in a "title" format so the first and last name would be capitalized.
                                                                                        # I am using the "yourName" variable throughout the game with the "title()"" function.
def moveOnMap():                                                                        # This is the 2nd function that holds most of our game.
    
    global playerX                                                                      # I had the "global" function for all of the coordinates, so the moveOnMap function can use the global values for these variables.
    global playerY
    global treasureX
    global treasureY
    global obstacleX0
    global obstacleY0
    global obstacleX1
    global obstacleY1
    global obstacleX2
    global obstacleY2
    global obstacleX3
    global obstacleY3
    global extraCreditX0
    global extraCreditY0
    global extraCreditX1
    global extraCreditY1
    global extraCreditX2
    global extraCreditY2 
    global extraCreditX3
    global extraCreditY3
    global extraCreditX4
    global extraCreditY4
    global turns 
    
    playerX = 2                                                                         # Once again, I have restated all the variables with their coordinates inside our function, which are randomly chosen by the "random" feature.
    playerY = 2
    treasureX = random.randint(0,4)
    treasureY = random.randint(0,4)
    obstacleX0 = random.randint(0,4)
    obstacleY0 = random.randint(0,4)
    obstacleX1 = random.randint(0,4)
    obstacleY1 = random.randint(0,4)
    obstacleX2 = random.randint(0,4)
    obstacleY2 = random.randint(0,4)
    obstacleX3 = random.randint(0,4)
    obstacleY3 = random.randint(0,4)
    extraCreditX0 = random.randint(0,4)
    extraCreditY0 = random.randint(0,4)
    extraCreditX1 = random.randint(0,4)
    extraCreditY1 = random.randint(0,4)
    extraCreditX2 = random.randint(0,4)
    extraCreditY2 = random.randint(0,4)
    extraCreditX3 = random.randint(0,4)
    extraCreditY3 = random.randint(0,4)
    extraCreditX4 = random.randint(0,4)
    extraCreditY4 = random.randint(0,4)
    
    while (((playerX == treasureX) and (playerY == treasureY)) or                       # This is the very first "while loop" that states that while any of the coordinates of any of the variables fall on the same spot...
           ((playerX == obstacleX0) and (playerY == obstacleY0)) or                     # It is excruciatingly long. I have accounted for every possible combination between the player, treasure, obstacle0, obstacle1, obstacle2, obstacle3,
           ((playerX == obstacleX1) and (playerY == obstacleY1)) or                     # extracredit0, extracredit1, extracredit2, extracredit3, and extracredit4
           ((playerX == obstacleX2) and (playerY == obstacleY2)) or                 
           ((playerX == obstacleX3) and (playerY == obstacleY3)) or
           ((playerX == extraCreditX0) and (playerY == extraCreditY0)) or
           ((playerX == extraCreditX1) and (playerY == extraCreditY1)) or
           ((playerX == extraCreditX2) and (playerY == extraCreditY2)) or
           ((playerX == extraCreditX3) and (playerY == extraCreditY3)) or
           ((playerX == extraCreditX4) and (playerY == extraCreditY4)) or
           ((treasureX == obstacleX0) and (treasureY == obstacleY0)) or
           ((treasureX == obstacleX1) and (treasureY == obstacleY1)) or
           ((treasureX == obstacleX2) and (treasureY == obstacleY2)) or
           ((treasureX == obstacleX3) and (treasureY == obstacleY3)) or
           ((treasureX == extraCreditX0) and (treasureY == extraCreditY0)) or
           ((treasureX == extraCreditX1) and (treasureY == extraCreditY1)) or
           ((treasureX == extraCreditX2) and (treasureY == extraCreditY2)) or
           ((treasureX == extraCreditX3) and (treasureY == extraCreditY3)) or
           ((treasureX == extraCreditX4) and (treasureY == extraCreditY4)) or
           ((obstacleX0 == obstacleX1) and (obstacleY0 == obstacleY1)) or
           ((obstacleX0 == obstacleX2) and (obstacleY0 == obstacleY2)) or
           ((obstacleX0 == obstacleX3) and (obstacleY0 == obstacleY3)) or
           ((obstacleX0 == extraCreditX0) and (obstacleY0 == extraCreditY0)) or
           ((obstacleX0 == extraCreditX1) and (obstacleY0 == extraCreditY1)) or
           ((obstacleX0 == extraCreditX2) and (obstacleY0 == extraCreditY2)) or
           ((obstacleX0 == extraCreditX3) and (obstacleY0 == extraCreditY3)) or
           ((obstacleX0 == extraCreditX4) and (obstacleY0 == extraCreditY4)) or
           ((obstacleX1 == obstacleX2) and (obstacleY1 == obstacleY2)) or
           ((obstacleX1 == obstacleX3) and (obstacleY1 == obstacleY3)) or
           ((obstacleX1 == extraCreditX0) and (obstacleY1 == extraCreditY0)) or
           ((obstacleX1 == extraCreditX1) and (obstacleY1 == extraCreditY1)) or
           ((obstacleX1 == extraCreditX2) and (obstacleY1 == extraCreditY2)) or
           ((obstacleX1 == extraCreditX3) and (obstacleY1 == extraCreditY3)) or
           ((obstacleX1 == extraCreditX4) and (obstacleY1 == extraCreditY4)) or
           ((obstacleX2 == obstacleX3) and (obstacleY2 == obstacleY3)) or
           ((obstacleX2 == extraCreditX0) and (obstacleY2 == extraCreditY0)) or
           ((obstacleX2 == extraCreditX1) and (obstacleY2 == extraCreditY1)) or
           ((obstacleX2 == extraCreditX2) and (obstacleY2 == extraCreditY2)) or
           ((obstacleX2 == extraCreditX3) and (obstacleY2 == extraCreditY3)) or
           ((obstacleX2 == extraCreditX4) and (obstacleY2 == extraCreditY4)) or
           ((obstacleX3 == extraCreditX0) and (obstacleY3 == extraCreditY0)) or
           ((obstacleX3 == extraCreditX1) and (obstacleY3 == extraCreditY1)) or
           ((obstacleX3 == extraCreditX2) and (obstacleY3 == extraCreditY2)) or
           ((obstacleX3 == extraCreditX3) and (obstacleY3 == extraCreditY3)) or
           ((obstacleX3 == extraCreditX4) and (obstacleY3 == extraCreditY4)) or
           ((extraCreditX0 == extraCreditX1) and (extraCreditY0 == extraCreditY1)) or
           ((extraCreditX0 == extraCreditX2) and (extraCreditY0 == extraCreditY2)) or
           ((extraCreditX0 == extraCreditX3) and (extraCreditY0 == extraCreditY3)) or
           ((extraCreditX0 == extraCreditX4) and (extraCreditY0 == extraCreditY4)) or
           ((extraCreditX1 == extraCreditX2) and (extraCreditY1 == extraCreditY2)) or
           ((extraCreditX1 == extraCreditX3) and (extraCreditY1 == extraCreditY3)) or
           ((extraCreditX1 == extraCreditX4) and (extraCreditY1 == extraCreditY4)) or
           ((extraCreditX2 == extraCreditX3) and (extraCreditY2 == extraCreditY3)) or
           ((extraCreditX2 == extraCreditX4) and (extraCreditY2 == extraCreditY4)) or
           ((extraCreditX3 == extraCreditX4) and (extraCreditY3 == extraCreditY4))):
           
        treasureX = random.randint(0,4)                                                 # The system should keep regenerating new randomly chosen coordinates for all of the variables, so they would be in different spots.
        treasureY = random.randint(0,4)                                                 # Since the player will start from the middle of the grid at (2, 2), I do not need a randomly chosen number for the player.
        obstacleX0 = random.randint(0,4)
        obstacleY0 = random.randint(0,4)
        obstacleX1 = random.randint(0,4)                                                # The coordinates and the "random" command are used after the "while" loop, so if they are on the same spot, they will be regenerated after
        obstacleY1 = random.randint(0,4)                                                # the "while" loop command is implemented.
        obstacleX2 = random.randint(0,4)
        obstacleY2 = random.randint(0,4)
        obstacleX3 = random.randint(0,4)
        obstacleY3 = random.randint(0,4)
        extraCreditX0 = random.randint(0,4)
        extraCreditY0 = random.randint(0,4)
        extraCreditX1 = random.randint(0,4)
        extraCreditY1 = random.randint(0,4)
        extraCreditX2 = random.randint(0,4)
        extraCreditY2 = random.randint(0,4)
        extraCreditX3 = random.randint(0,4)
        extraCreditY3 = random.randint(0,4)
        extraCreditX4 = random.randint(0,4)
        extraCreditY4 = random.randint(0,4)
    

    turns = 20                                                                          # This is the very first value we have to work with, since we are allowing the player only 20 turns.
    count = 0                                                                           # Count starts at 0.
    bKeepGoing = True                                                                   # This is the main Boolean "True" value that controls the continuation of the game.
    bWonGame = True                                                                     # This Boolean "True" value is used to stop the game from continuing whenever the player finds the treasure.
    bTreasureGuesses = True                                                             # This Boolean expression is used with the treasure.
    bobstacleGuesses0 = True                                                            # This Boolean expression is used with the first obstacle.
    bobstacleGuesses1 = True                                                            # This Boolean expression is used with the second obstacle.
    bobstacleGuesses2 = True                                                            # This Boolean expression is used with the third obstacle.
    bobstacleGuesses3 = True                                                            # This Boolean expression is used with the fourth obstacle.
    bExtraLooping0 = True                                                               # This Boolean expression is used with the first extra credit.
    bExtraLooping1 = True                                                               # This Boolean expression is used with the second extra credit.
    bExtraLooping2 = True                                                               # This Boolean expression is used with the third extra credit.
    bExtraLooping3 = True                                                               # This Boolean expression is used with the fourth extra credit.
    bExtraLooping4 = True                                                               # This Boolean expression is used with the fifth extra credit.
    
    print"You are on " + "(" + str(playerX) + ", " + str(playerY) + ")"                 # This prints the initial coordinates of the player.
    print "You have " + str(turns) + " moves left."                                     # This reminds the player of the number of turns.
    
    while ((count < turns) and (bKeepGoing == True)):                                   # while count is less than the number of turns and the Boolean expression "bKeepGoing" is "True", the game should go through the loop.
        
        whereMove = raw_input("\nWhere would you like to move " + str(yourName.title()) + "? ") # This "raw_input" is used to ask the user where he/she would like to move, combined with his/her inputted name from the first function playerName().
       
        if ((whereMove != "") and (whereMove.lower() == "up" or whereMove.lower() == "u")):   # I used "whereMove !=" argument in case the user presses "Enter" instead of the required commands, especially later in the game. 
                                                                                        # The ".lower()" option makes the responses of the user in lowercase and makes the Boolean expression easier instead of using all variations of the inputted choices for the argument.
            playerY = playerY + 1                                                       # If the user picks "up", the "y" coordinate of playerY will go up by one.
           
            if (playerY > 4):                                                           # This is an "if" statement within another. If the "y" coordinate goes outside of the grid, I am looping the player around to the other side.
                playerY = 0                                                             # If the player  goes beyond position "4", I am moving him/her to the opposite side of the map and placing him/her on "0". 
                print "\nBe careful " + str(yourName.title()) + ", that move is not allowed... You just looped around the map. Try again."  # The warning that will be printed for the user.
                turns = turns + 1                                                       # Here, I do not want the user to lose a "turn", therefore I am adding a turn, to keep his/her turn count the same, since it will be subtracted later down the command lines.
                
        elif ((whereMove != "") and (whereMove.lower() == "down" or whereMove.lower() == "d")):             # Same thing with the "y" coordinate, controlling the down movement.
            playerY = playerY - 1                                                       # "playerY" 's coordinate would be 1 less than before to be able to move down.
            
            if (playerY < 0):                                                           # This is the "if" statement that controls the player going below the "0" grid line.
                playerY = 4                                                             # In this case if the player moves below "0", I am wrapping him/her around the map to the opposite position "4".
                print "\nBe careful " + str(yourName.title()) + ", that move is not allowed... You just looped around the map. Try again."
                turns = turns + 1                                                       # I do not want the user to lose a "turn", therefore, I am adding a turn to account for the one that will be subtracted down the command lines.
                
        elif ((whereMove != "") and (whereMove.lower() == "right" or whereMove.lower() == "r")):            # This controls the "x" coordinate of the player, moving right.
            playerX = playerX + 1                                                       # The value of the variable playerX would be 1 more than the previous value to move the player right on the map.
            
            if (playerX > 4):                                                           # Here, I am controlling the player's move, not to allow him/her to move beyond "4" on the map grid.
                playerX = 0                                                             # Same way as the previous coordinates, I am wrapping the player around the map and placing him/her on the opposite side of the map at "0".
                print "\nBe careful " + str(yourName.title()) + ", that move is not allowed... You just looped around the map. Try again." # The message will warn the player that he/she was wrapped around the map.
                turns = turns + 1                                                       # No loss of "turn".
        
        elif ((whereMove != "") and (whereMove.lower() == "left" or whereMove.lower() == "l")):             # Controlling the "x" coordinate to move left.
            playerX = playerX - 1                                                       # To move the player left, the "x" coordinate should be 1 less than the previous value.
            
            if (playerX < 0):                                                           # Similar command as previous coordinates, I am not allowing te user to go outside of the grid.
                playerX = 4                                                             # I am moving the user to the other side of the grid if they try to go beyond the "0" coordinate.
                print "\nBe careful " + str(yourName.title()) + ", that move is not allowed... You just looped around the map. Try again." # Message will be printed for the user.
                turns = turns + 1                                                       # No loss of "turn".
                
        else:                                                                           # This "else" statement controls the input of the user. In case the options are outside of the given criteria, the message.
            print "\nThat is not a valid option " + str(yourName.title()) + ". Try again using up, down, left, or right commands (u, d, l, r)."      # will warn the user that the entered characters are not valid, without losing a turn.
            turns = turns + 1
        
        turns = turns - 1                                                               # This command controls the actual turns, and with every move the user loses a turn.
        print str(yourName.title()) + ", you are on " + "(" + str(playerX) + ", " + str(playerY) + ")" # This is the message that will be printed after every move to let the user know where he/she is on the map, while incorporating the coordinates of (x and y) and the user's name.
        print "You have " + str(turns) + " moves left."                                 # This will let the user be aware of the "turns" left, incorporating the user's name as a string.
        
        if ((playerX == treasureX) and (playerY == treasureY) and (turns != 0)):        # If the user arrives at the "treasure", then the player's (x and y) coordinates have to match the "treasure's" (x and y) coordinates. I did not use the (whereMove != "") argument here, because
                                                                                        # there's no way for the player to land on the treasure again during the game. The player either wins the game or loses the game, therefore no need for the argument in this "if" statement.
            guesses = 0                                                                 # "Guesses" start with "0" and the user has "2" guesses to solve the problem.
            bTreasureGuesses = True                                                     # This is a Boolean expression that is "True" only for the treasure portion of the game.
            x = random.randint(1,50)                                                    # The variables of the math problem that need to be solved are randomly generated.
            y = random.randint(1,50)
            z = random.randint(1,50)
            v = random.randint(1,50)
           
            print "\nHurrah... " + str(yourName.title()) + ", you are on top of the treasure. To win the game, solve the following equation."     # This informs the user that he/she is on the "treasure" and the number of "guesses" left.
            print "You have 2 guesses otherwise you lose the game."
            
            while ((guesses < 2) and (bTreasureGuesses == True)):                       # I used a "while" loop to control the "treasure" commands.
                loopingNumber = True                                                    # This Boolean expression will repeat if the "raw-input" is not a digit.
    
                while loopingNumber: 
                    treasureGuess = (x - y) * (z + v)                                   # This is the equation of the math problem.
                    print "\n(" + str(x) + " - " + str(y) + ") * (" + str(z) + " + " + str(v) +") = "   # This is where the user will see the math problem generated by the randomly chosen numbers.
                    treasureAnswer = raw_input("\nIt is equal to: " )                   # The user will answer with a "raw_input".
                    treasureAnswer2 = treasureAnswer.replace ("." , "")                 # I used the "replace" command to account for any decimal inputs.
                    treasureAnswer3 = treasureAnswer2.replace ("-" , "")                # I used a third variable to "replace" the negative "-" sign input.
                    
                    if (treasureAnswer3.isdigit() == True):                             # I am checking here to see if the variable inputted by the user is a valid number.
                        loopingNumber = False                                           # If the previous variable is a valid number, no need to loop through the process again, hence the "False" value of the Boolean "loopingNumber" expression.
                        treasureAnswer3 = int(treasureAnswer)                           # I am converting the "raw_input" variable that went through the "replace" values to an integer again.
                    
                    else: 
                        print  "\n" + str(yourName.title()) + ", you need to go back to school! That's not a number."  # If the previously entered "raw_input" is not a number, this is the message the user will see.
                        loopingNumber = True                                            # The Boolean "True" value will force the looping to re-ask the user for his/her answer.
        
                if (treasureAnswer3 == treasureGuess):                                  # In case the answer matches the correct number the following ensues.
                    print "\nCongratulations " + str(yourName.title()) + ", " + str(treasureAnswer3) + " is the correct answer. \n\nYou just won the game."   # The message congratulates the user on the correct answer and lets the user know that he/she won.
                    bTreasureGuesses = False                                            # This Boolean expression will be "False", stopping the looping of the treasure commands.
                    bKeepGoing = False                                                  # This expression will stop the game from continuing.
                    bWonGame = True                                                     # This expression is used later in the game to stop the game from running, in case the "treasure" is found.
                                                                       
                else:
                    if (guesses < 2):                                                   # In case the user inputs the wrong answer, he/she will be prompted for another try.
                        bTreasureGuesses = True                                         # The Boolean expression of the "treasure" will run again.
                        guesses = guesses + 1                                           # The number of "guesses" will go up by 1.
                        print "\nSorry " + str(yourName.title()) + ", you have " + str(2 - guesses) + " guess left." # This message will print, combining the player's name and informing the player of the "guesses" left.
                        
            else: 
                
                if ((bWonGame == False) or (guesses == 2)):                             # In case the "guesses" are used up or the game is not won...
                    print "\nYou used up all your guesses."                             # This is the message that will print.
                    bWonGame = False                    
                    bKeepGoing = False
                    guesses = 0                                                         # I am resetting the "guesses" to "0" for future problems.

        if ((playerX == obstacleX0) and (playerY == obstacleY0) and (turns != 0) and (whereMove != "")):  # If the player lands on "obstacle0" matching the same (x and y) coordinates and the "whereMove" is not empty with just "Enter" pressed, this "if" expression will kick in.
                                                                                        # I added the "whereMove !=" argument because I noticed that after answering the obstacle question, if the player pressed "enter" without typing anything, the player will stay on the same square,
                                                                                        # and the same question will be asked again, with newly generated numbers. Therefore, to force the player to enter something other than pressing "Enter", I added the (whereMove != " ") argument.
            hurdle0 = 0                                                                 # I am using "hurdles" to control the number of "guesses".
            bobstacleGuesses0 = True                                                    # This Boolean "True" expression will control the looping of the first "obstacle0".
            x0 = random.randint(1,100)                                                  # Randomly generated values for (x0 and y0) to be used for the math problem later.
            y0 = random.randint(1,100)
            
            print "\nYou just encountered an obstacle " + str(yourName.title()) + ". Answer the following question correctly to continue your journey." # This will print to inform the user, using his/her first name, that he/she landed on an obstacle.
            print "You have 2 guesses otherwise you lose the game."                     # I am informing the user of the number of "guesses" left.
            
            while ((hurdle0 < 2) and (bobstacleGuesses0 == True)):                      # "While" looping rules for "guesses" that are less than "2" and if the "obstacle0" Boolean expression is "True".
                loopingObstacle0 = True 
    
                while loopingObstacle0: 
                    obstacleGuess0 = (x0 + 2 * (y0))                                    # The math problem of the first "obstacle0".
                    print "\n[" + str(x0) + " + (2 * " + str(y0) + ")]"                 # The message that will appear to the user.
                
                    obstacleAnswer0 = raw_input("The answer is = ")                     # The "raw_input" asked of the user.
                    obstacleAnswer01 = obstacleAnswer0.replace ("." , "")               # Manipulating the decimals in the "raw_input". 
                    obstacleAnswer02 = obstacleAnswer01.replace ("-" , "")              # Manipulating the negative "-" sign in the "raw_input".
                    
                    if (obstacleAnswer02.isdigit() == True):                            # Checking to see if the "raw_input" is a number otherwise the "else" command will kick in.
                        loopingObstacle0 = False                                        # If the previous check is correct, the looping should stop with the "False" value.
                        obstacleAnswer02 = int(obstacleAnswer0)                         # Converting the "raw_input" to an integer.
                        
                    else: 
                        print "\n" + str(yourName.title()) +", you need to go back to school! That's not a number. Try again."  # If the "raw_input" contains non-number characters, this will be printed.
                        loopingObstacle0 = True                                         # This forces the looping of the "obstacle0" problem again, to give the user another opportunity to answer the question.
                
                if (obstacleAnswer02 == obstacleGuess0):                                # If the answer is correct...
                    print "\nThat is correct " + str(yourName.title()) + ". You may continue." # This message  will print.
                    print "You are on " + "(" + str(playerX) + ", " + str(playerY) + ")"       # This will inform the player on his/her position...
                    print "You have " + str(turns) + " moves left."                     # and the number of "turns" left.
                    bobstacleGuesses0 = False                                           # The looping should stop.
                    bWonGame = False                                                    # However, the game is not won, therefore, this expression is "False" and the game will continue.
                    
                else:                                                                   # This is the "else" command in case the answer is incorrect.
                    if (hurdle0 < 2):                                                   # If the first try is incorrect and the "guesses" are less than "2", the user will have another opportunity.
                        
                        bobstacleGuesses0 = True                                        # The looping of the question will be "True".
                        hurdle0 = hurdle0 + 1                                           # The number of "guesses", designated as "hurdle0" will go up by 1.
                        print "\nSorry " + str(yourName.title()) +", that is incorrect. You have " + str(2 - hurdle0) + " guess left."   # This message will print with every try, decreasing the number of "guesses" outputted to the user.
            
            else:                                                                       # This is the "else" command in case the "guesses" are used up.
                if (hurdle0 == 2):                                                      # If the "guesses" are used up...
                    print "\nYou used up all your guesses."                             # The user will see this message.
                    bWonGame = False                                                    # This expression will control the upcoming message that will tell the user that he/she lost.
                    bKeepGoing = False                                                  # The game will stop from running again.
                    hurdle0 = 0                                                         # Resetting the value of "guesses" or "hurdle0" to "0" for future runs.
    
        if ((playerX == obstacleX1) and (playerY == obstacleY1) and (turns != 0) and (whereMove != "")):  # If the player lands on "obstacle1" matching the same (x and y) coordinates and the "whereMove" is not empty with just "Enter" pressed, this "if" expression will kick in.
                                
            hurdle1 = 0                                                                 # I am using "hurdles" to control the number of "guesses".
            bobstacleGuesses1 = True                                                    # This Boolean "True" expression will control the looping of the first "obstacle1".
            x1 = random.randint(1,8)                                                    # Randomly generated values for (x and y) to be used in the math problem later.
            y1 = random.randint(1,4)
            
            print "\nYou just encountered an obstacle " + str(yourName.title()) + ". Answer the following question correctly to continue your journey." # This will print to inform the user, using his/her first name, that he/she landed on an obstacle.
            print "You have 2 guesses otherwise you lose the game."                     # I am informing the user of the number of "guesses" left.
            
            while ((hurdle1 < 2) and (bobstacleGuesses1 == True)):                      # "While" looping rules for "guesses" that are less than 2 and if the "obstacle1" Boolean expression is "True".
                loopingObstacle1 = True 
    
                while loopingObstacle1: 
                    obstacleGuess1 = (x1 ** y1)                                         # The math problem of the first "obstacle1".
                    print "\n" + str(x1) + " ^ (to the power of) " + str(y1)            # The message that will appear to the user.
                
                    obstacleAnswer1 = raw_input("The answer is = ")                     # The "raw_input" asked of the user.
                    obstacleAnswer11 = obstacleAnswer1.replace ("." , "")               # Manipulating the decimals in the "raw_input". 
                    obstacleAnswer12 = obstacleAnswer11.replace ("-" , "")              # Manipulating the negative "-" sign in the "raw_input".
                    
                    if (obstacleAnswer12.isdigit() == True):                            # Checking to see if the "raw_input" is a number otherwise the "else" command will kick in.
                        loopingObstacle1 = False                                        # If the previous check is correct, the looping should stop with the "False" value.
                        obstacleAnswer12 = int(obstacleAnswer1)                         # Converting the "raw_input" to an integer.
                        
                    else: 
                        print "\n" + str(yourName.title()) +", you need to go back to school! That's not a number. Try again."  # If the "raw_input" contains non-number characters, this will be printed.
                        loopingObstacle1 = True                                         # This forces the looping of the "obstacle1" problem again, to give the user another opportunity to answer the question.
                
                if (obstacleAnswer12 == obstacleGuess1):                                # If the answer is correct...
                    print "\nThat is correct " + str(yourName.title()) + ". You may continue." # This message  will print.
                    print "You are on " + "(" + str(playerX) + ", " + str(playerY) + ")"       # This will inform the player on his/her position...
                    print "You have " + str(turns) + " moves left."                     # and the number of "turns" left.
                    bobstacleGuesses1 = False                                           # The looping should stop.
                    bWonGame = False                                                    # However, the game is not won, therefore, this expression is "False" and the game will continue.
                    
                else:                                                                   # This is the "else" command in case the answer is incorrect.
                    if (hurdle1 < 2):                                                   # If the first try is incorrect and the "guesses" are less than "2", the user will have another opportunity.
                        
                        bobstacleGuesses1 = True                                        # The looping of the question will be "True".
                        hurdle1 = hurdle1 + 1                                           # The number of "guesses", designated as "hurdle1" will go up by 1.
                        print "\nSorry " + str(yourName.title()) +", that is incorrect. You have " + str(2 - hurdle1) + " guess left."   # This message will print with every try, decreasing the number of "guesses" outputted to the user.
            
            else:                                                                       # This is the "else" command in case the "guesses" are used up.
                if (hurdle1 == 2):                                                      # If the "guesses" are used up...
                    print "\nYou used up all your guesses."                             # The user will see this message.
                    bWonGame = False                                                    # This expression will control the upcoming message that will tell the user that he/she lost.
                    bKeepGoing = False                                                  # The game will stop from running again.
                    hurdle1 = 0                                                         # Resetting the value of "guesses" or "hurdle1" to "0" for future runs.
        
        if ((playerX == obstacleX2) and (playerY == obstacleY2) and (turns != 0) and (whereMove != "")):  # This is similar to the previous "obstacle1" rules.
                                        
            hurdle2 = 0                                                                 # I used "hurdle2" instead of "guesses".
            bobstacleGuesses2 = True                                                    # The Boolean expression that will control the second "obstacle2" "while" looping.
            x2 = random.randint(1,100)                                                  # Randomly generated values for the variables of the math problem.
            y2 = random.randint(1,100)
            z2 = random.randint(2,5)   
               
            print "\nYou just encountered an obstacle " + str(yourName.title()) + ". Answer the following question correctly to continue your journey."
            print "You have 2 guesses otherwise you lose the game."
            
            while ((hurdle2 < 2) and (bobstacleGuesses2 == True)):                      # As long as the count number of "hurdle2" is less than "2" this "while" loop will run.
                loopingObstacle2 = True
    
                while loopingObstacle2: 
                    obstacleGuess2 = (x2 + y2) * z2
                    print "\n(" + str(x2) + " + " + str(y2) + ") * " + str(z2)          # Printing the math problem to solve.
                    
                    obstacleAnswer2 = raw_input("The answer is = ")                     # "Raw_input" of the answer asked from the user.
                    obstacleAnswer21 = obstacleAnswer2.replace ("." , "")               # Replacing the decimal in the number inputted by the user, in case there is one. Saving it as another variable.
                    obstacleAnswer22 = obstacleAnswer21.replace ("-" , "")              # Replacing the negative "-" sign in the "raw_input" and saving it in a third new variable.
                    
                    if (obstacleAnswer22.isdigit() == True):                            # Checking to see if the "raw_input" is a valid number.
                        loopingObstacle2 = False
                        obstacleAnswer22 = int(obstacleAnswer2)                         # Converting the variable "obstacleAnswer22" to an integer after all the previous replacements.
                        
                    else: 
                        print "\n" + str(yourName.title()) +", you need to go back to school! That's not a number. Try again." # This would print if the "raw_input" does not consist of a number.
                        loopingObstacle2 = True    
                    
                if (obstacleAnswer22 == obstacleGuess2):                                # Same as the previous obstacles, if the answer is correct the player will be able to continue the game.
                    print "\nThat is correct " + str(yourName.title()) + ". You may continue."
                    print "You are on " + "(" + str(playerX) + ", " + str(playerY) + ")"
                    print "You have " + str(turns) + " moves left."
                    bobstacleGuesses2 = False
                    bWonGame = False
                    
                else:                                                                   # The looping will continue if the "guesses" are less than "2".
                    if (hurdle2 < 2):
                        
                        bobstacleGuesses2 = True
                        hurdle2 = hurdle2 + 1
                        print "\nSorry " + str(yourName.title()) + ", that is incorrect. You have " + str(2 - hurdle2) + " guess left."
            else:                                                                       # The looping will end when the "guesses" reach "2" and the game is lost.
                if (hurdle2 == 2):
                    print "\nSorry, you used up all your guesses."
                    bWonGame = False
                    bKeepGoing = False
                    hurdle2 = 0                                                         # Resetting the value of "hurdle2" to "0" for future runs.
                    
        if ((playerX == obstacleX3) and (playerY == obstacleY3) and (turns != 0) and (whereMove != "")):      # Rules for the fourth obstacle, "obstacle3". 
                            
            hurdle3 = 0                                                                 # Using "hurdle3" as a counter for the number of "guesses".
            bobstacleGuesses3 = True
            x3 = random.randint(1,100)                                                  # Randomly generating variables for our math problem computation.
            y3 = random.randint(1,100)
            z3 = random.randint(2,5)   
               
            print "\n" + str(yourName.title()) + ", you just encountered an obstacle. Solve the following math problem to continue your adventure."
            print "You have 2 guesses otherwise you lose the game."
                
            while ((hurdle3 < 2) and (bobstacleGuesses3 == True)):
                loopingObstacle3 = True
                
                while loopingObstacle3: 
                    obstacleGuess3 = x3 * (y3 + z3) / 2.0
                    print "\n" + str(x3) + " (" + str(y3) + " + " + str(z3) + ") / 2" 
                
                    obstacleAnswer3 = raw_input("The answer is = ")
                    obstacleAnswer31 = obstacleAnswer3.replace ("." , "")
                    obstacleAnswer32 = obstacleAnswer31.replace ("-" , "")
                    
                    if (obstacleAnswer32.isdigit() == True):                            # Checking again to see if the "raw_input" is a number.           
                        loopingObstacle3 = False
                        obstacleAnswer32 = float(obstacleAnswer3)
                        
                    else: 
                        print "\nYou need to go back to school " + str(yourName.title()) + "! That's not a number."   # If the "raw_input" is not a number, this message will warn the user.
                        loopingObstacle3 = True    
        
                if (obstacleAnswer32 == obstacleGuess3):                                # If the "raw_input" is correct...
                    print "\nThat is correct " + str(yourName.title()) + ". You may continue."  # A message will let the user know that his/her "guess" is correct.
                    print "You are on " + "(" + str(playerX) + ", " + str(playerY) + ")"        # Reprinting the coordinates.
                    print "You have " + str(turns) + " moves left."                     # Informing the user of the "turns" left in the game.
                    bobstacleGuesses3 = False                                           # The Boolean expression of the "obstacle3" "guess" will stop from running.
                    bKeepGoing = True
                    bWonGame = False
                    
                else:
                    if (hurdle3 < 2):                                                   # If the "guesses" are less than 2, then the user will have another option.
                       
                        bobstacleGuesses3 = True
                        hurdle3 = hurdle3 + 1
                        print "\nSorry " + str(yourName.title()) + ", that is incorrect. You have " + str(2 - hurdle3) + " guess left."     # A message will print to let the user know of the number of "guesses" left.
            else:    
                if (hurdle3 == 2):
                    print "\nSorry you used up all your guesses."                       # This will end the game if the "guesses" are exhausted.
                    bWonGame = False
                    bKeepGoing = False
                    hurdle3 = 0                                                         # Resetting the number of "hurdles3" to "0" for future runs.
        
        if ((playerX == extraCreditX0) and (playerY == extraCreditY0) and (turns != 0) and (whereMove != "")):   # This is the first extra "credit0" option. Similar to the obstacles, If the player lands on the same 
                                                                                        # coordinates as the extra credit0, and the moving direction selected is not empty (just "Enter" pressed with no direction selected), then
                                                                                        # the following "if" statement will run.
            credits = 0                                                                 # Using "credits" to keep track of the number of "guesses".
            bExtraLooping0 = True                                                       # Using this Boolean expression to control the extra "credit0" looping.
            print "\n" + str(yourName.title()) + ", you just encountered an extra turn option. Answer the following question correctly to earn an extra turn."
            print "You have 2 guesses otherwise you lose the opportunity and you lose a turn."
           
            while bExtraLooping0:                                                       # First "while" looping command for extra "credit0".
                while ((credits < 2) and (bExtraLooping0 == True)):                     # If the "credits" are less than "2" and the extra "credit0" Boolean expression is "True".
                 
                    extraAnswer0 = str(raw_input("\nHow do you write the decimal number 49 in Roman numerals? "))  # The "raw_input" that is asking the Roman numerals question and getting the answer from the user.
                    extraAnswer0 = extraAnswer0.upper()                                 # I am converting all the letters to uppercase to check later.
                    extraAnswer01 = extraAnswer0.replace(" ", "")                       # I am replacing the space in the "raw_input" response to check later if all the characters are only letters...
                                                                                        # While giving the "raw_input" a new variable name.
                    if extraAnswer01.isalpha() == True:                                 # Checking to see if the variable with the replaced space character, consists only of letters. 
                        if (extraAnswer0 == "XLIX"):                                    # Here I am checking the original "raw_input", with uppercase characters, to see if they match the correct answer.
                            
                            bExtraLooping0 = False                                      # Looping would stop for the question.
                            bWonGame = False                                            # The game is not won yet.
                            turns = turns + 1                                           # I am giving the user an extra "turn" if he/she guesses correctly.
                            print "\n'" + str(extraAnswer0.upper()) + "', that is correct " + str(yourName.title()) + ". You earned an extra turn."     # If the answer is correct, this message will print.
                            print "\nYou are on " + "(" + str(playerX) + ", " + str(playerY) + ")" # Coordinates of the player will print.
                            print "You have " + str(turns) + " moves left."             # I am printing the new "turns" left to let the user know.
                            
                        else:
                            if (credits < 2):
                                
                                bExtraLooping0 = True                                   # The extra "credit0" question looping will run again, as long as "guesses" are less than "2".
                                credits = credits + 1                                   # The number of "guesses", designated as "credits" will go up by one, 
                                print "\nSorry " + str(yourName.title()) + ", that is incorrect. You have " + str(2 - credits) + " guess left."  # if the answer is incorrect, this message will be printed.
                    else:
                        print str(yourName.title()) + ", those are not Roman numerals. Try using your letters." # If the "raw_input" has invalid characters, this message will print.
                        
                else:    
                    if (credits == 2):                                                  # If the number of "guesses" are exhausted, this message will print.
                        turns = turns - 1                                               # The player will lose a "turn" if he/she does not guess correctly.
                        print "\nSorry " + str(yourName.title()) + ", you used up all your guesses and you lost a turn."  # This will print to let the user know that he/she lost a "turn".
                        print "\nYou are on " + "(" + str(playerX) + ", " + str(playerY) + ")"   # Coordinates of the player will re-print.
                        print "You have " + str(turns) + " moves left."                 # I am printing the number of "turns" left.
                        bWonGame = False                                                # The game is not won.
                        bExtraLooping0 = False                                          # The "credit0" looping would stop.
                        credits = 0                                                     # I am resetting the number of "guesses" designated by "credits" back to "0" for future problems.
        
        if ((playerX == extraCreditX1) and (playerY == extraCreditY1) and (turns != 0) and (whereMove != "")):   # Extra "credit1" option.
                            
            credits = 0                                                                 # Using "credits" to keep track of the number of "guesses".
            bExtraLooping1 = True                                                       # Using this Boolean expression to control the extra "credit1" looping.
            print "\n" + str(yourName.title()) + ", you just encountered an extra turn option. Answer the following question correctly to earn an extra turn."
            print "You have 2 guesses otherwise you lose the opportunity and you lose a turn."
           
            while bExtraLooping1:                                                       # First "while" looping command for extra "credit1"...
                while ((credits < 2) and (bExtraLooping1 == True)):                     # If the "credits" are less than "2" and the extra "credit1" Boolean expression is "True".
                 
                    extraAnswer = str(raw_input("\nWhat are the first two words programming students learn? "))  # The "raw_input" that is asking the trivia question and getting the answer from the user.
                    extraAnswer = extraAnswer.lower()                                   # I am converting all the letters to lowercase to check later.
                    extraAnswer1 = extraAnswer.replace(" ", "")                         # I am replacing the space in the "raw_input"-ted response to check later if all the characters are only letters...
                                                                                        # While giving the "raw_input" a new variable name.
                    if extraAnswer1.isalpha() == True:                                  # Checking to see if the variable with the replaced space character, consists only of letters. 
                        if (extraAnswer == "hello world"):                              # Here I am checking the original "raw_input", with lowercase characters, to see if they match the correct answer.
                            
                            bExtraLooping1 = False                                      # Looping would stop for the question.
                            bWonGame = False                                            # The game is not won yet.
                            turns = turns + 1                                           # I am giving the user an extra turn if they guess correctly.
                            print "\n'" + str(extraAnswer.title()) + "', that is correct " + str(yourName.title()) + ". You earned an extra turn."     # If the answer is correct, this message will print.
                            print "\nYou are on " + "(" + str(playerX) + ", " + str(playerY) + ")" # Coordinates of the player will print.
                            print "You have " + str(turns) + " moves left."             # I am printing the new "turns" left to let the user know.
                            
                        else:
                            if (credits < 2):
                                
                                bExtraLooping1 = True                                   # The extra "credit1" question looping will run again, as long as "guesses" are less than "2".
                                credits = credits + 1                                   # The number of "guesses" designated as "credits" will go up by one, 
                                print "\nSorry " + str(yourName.title()) + ", that is incorrect. You have " + str(2 - credits) + " guess left."  # if the answer is incorrect, this message will be printed.
                    else:
                        print str(yourName.title()) + ", those are not valid characters. Try using your letters." # If the "raw_input" has invalid characters, this message will print.
                        
                else:    
                    if (credits == 2):                                                  # If the number of "guesses" are exhausted, this message will print.
                        turns = turns - 1                                               # The player will lose a "turn" if he/she does not guess correctly.
                        print "\nSorry " + str(yourName.title()) + ", you used up all your guesses and you lost a turn."  # This will print to let the user know that he/she lost a "turn".
                        print "\nYou are on " + "(" + str(playerX) + ", " + str(playerY) + ")"   # Coordinates of the player will re-print.
                        print "You have " + str(turns) + " moves left."                 # I am printing the number of "turns" left.
                        bWonGame = False                                                # The game is not won.
                        bExtraLooping1 = False                                          # The "credit1" looping would stop.
                        credits = 0                                                     # I am resetting the number of "guesses" designated as "credits" back to "0" for future problems.
                    
        if ((playerX == extraCreditX2) and (playerY == extraCreditY2) and (turns != 0) and (whereMove != "")): # Extra "credit2" option.
                            
            credits = 0                                                                 # "Credits" will start with a value of "0".
            bExtraLooping2 = True
            print "\n" + str(yourName.title()) + ", you just encountered an extra turn option. Answer the following question correctly to earn an extra turn."
            print "You have 2 guesses otherwise you lose the opportunity and you lose a turn."
             
            while bExtraLooping2:    
                while ((credits < 2) and (bExtraLooping2 == True)):
                    extraAnswer2 = raw_input("\nWhat is the capital of Canada? ")       # This is our "raw_input" question.
                    
                    if extraAnswer2.isalpha() == True:                                  # I am checking to see if the characters of the "raw_input" are valid letters.
                        if (extraAnswer2.lower() == "ottawa"):                          # Converting all the letters in the "raw_input" to lowercase.
                            
                            bExtraLooping2 = False                                      # The extra looping of the ".isalpha" check would stop.
                            bWonGame = False                                            # The game is not won yet.
                            turns = turns + 1                                           # An extra "turn" is earned with a correct answer.
                            print "\n'" + str(extraAnswer2.capitalize()) + "', that is correct " + str(yourName.title()) + ". You earned an extra turn."        # if the user guesses correctly, this message will print.
                            print "You are on " + "(" + str(playerX) + ", " + str(playerY) + ")" # Coordinates of the player will re-print to let the user know of his/her position on the map.
                            print "You have " + str(turns) + " moves left."             # This printed message will let the user know of the "turns" left in the game.
                        
                        else:
                            if (credits < 2):                                           # Same rules as the previous extra credits question, if "credits" are less than "2" argument will run, since we are allowing only 2 guesses. 
                                
                                bExtraLooping2 = True                                   # The extra "credit2" Boolean expression will run again.
                                credits = credits + 1                                   # However, the number of "credits" will increase by one with each turn.
                                print "\nSorry " + str(yourName.title()) + ", that is incorrect. You have " + str(2 - credits) + " guess left."   # Message that will be outputted to the player, stating the remaining "guesses".
                    else:                                                               # If the user has non-letters in the "raw_input" this will be printed.
                        print "Those are invalid characters " + str(yourName.title()) + ". Please use your letters to answer the question."  # In case the characters used are not letters, this message will warn the user.
            
                else:    
                    if (credits == 2):                                                  # If the "credits" are exhausted the game continues and the user loses a "turn".
                        turns = turns - 1                                               # The player will lose a "turn" if he/she does not guess correctly.
                        print "\nSorry " + str(yourName.title()) + ", you used up all your guesses and you lost a turn."  
                        print "\nYou are on " + "(" + str(playerX) + ", " + str(playerY) + ")"   # Coordinates of the player will print.
                        print "You have " + str(turns) + " moves left."                 # I am printing the new "turns" left.
                        bWonGame = False
                        bExtraLooping2 = False                                          # The game continues.
                        credits = 0                 
                
        if ((playerX == extraCreditX3) and (playerY == extraCreditY3) and (turns != 0) and (whereMove != "")): #Fourth extra credit, "credit3" option.
            
            credits = 0
            bExtraLooping3 = True
            print "\n" + str(yourName.title()) + ", you just encountered an extra turn option. Answer the following problem correctly to earn an extra turn."
            print "You have 2 guesses otherwise you lose the opportunity and you lose a turn."
            
            while ((credits < 2) and (bExtraLooping3 == True)):
                
                binary = 1111                                                           # Using a binary number variable.
                loopingCredit3 = True                                                   # Boolean expression that will control the fourth extra "credit3" looping
                
                while loopingCredit3:                                                   # "While" statement that will initiate the looping.
                    print "\nHow is 15 (decimal base) written in Base 2 (binary) in a 4 bit system?"    # The question that will be printed.
                    
                    extraAnswer3 = raw_input("The answer is = ")                        # The "raw_input" answer asked from the user.
                    extraAnswer31 = extraAnswer3.replace ("." , "")                     # Replacing the decimal in the "raw_input" while saving it in a second variable.
                    extraAnswer32 = extraAnswer31.replace ("-" , "")                    # Replacing the negative "-" in the "raw_input" while saving it in a third variable.
                    
                    if (extraAnswer32.isdigit() == True):                               # Checking to see if the third variable, after all the replaced values, is a number.
                        loopingCredit3 = False
                        extraAnswer32 = int(extraAnswer3)                               # Converting the third variable to an integer.
                        
                    else: 
                        print "\nYou need to go back to school " + str(yourName.title()) + "! That's not a binary number. Try again." # This will print if the user types a non-number.
                        loopingCredit3 = True                                           # Looping of the extra "credit3" question continues and the user is asked again.
                    
                if (extraAnswer32 == binary):                                           # If the "raw_input" is correct and it matches the binary code, this message will be printed.
                    bExtraLooping3 = False
                    bWonGame = False                                                    # The game is not won.
                    turns = turns + 1                                                   # An extra "turn" is added to the game.
                   
                    print "\nThat is correct " + str(yourName.title()) + ". You earned an extra turn."  # This message will let the user know that the answer was correct and that an extra "turn" was earned.
                    print "You are on " + "(" + str(playerX) + ", " + str(playerY) + ")"# The coordinates of the player will re-print.
                    print "You have " + str(turns) + " moves left."                     # "Turns" left are printed.
                    
                else:                                                                   # Same as the previous extra credit questions, if the previous "guess" is incorrect. 
                    if (credits < 2):
                        
                        bExtraLooping3 = True
                        credits = credits + 1
                        print "\nSorry, that is incorrect " + str(yourName.title()) + ". You have " + str(2 - credits) + " guess left."
            else:    
                if (credits == 2):                                                      # Same as the previous extra credit questions, when the "credits" or "guesses" are exhausted.
                    turns = turns - 1                                                   # The player will lose a "turn" if he/she does not guess correctly.
                    print "\nSorry " + str(yourName.title()) + ", you used up all your guesses and you lost a turn."  # This will print to let the user know that he/she lost a "turn".
                    print "\nYou are on " + "(" + str(playerX) + ", " + str(playerY) + ")"   # Coordinates of the player will print.
                    print "You have " + str(turns) + " moves left."                     # I am printing the new "turns" left for the user.
                    bWonGame = False
                    bExtraLooping3 = False                                              # The Boolean expression of the fourth extra "credit3" is "False" , which would stop the looping, but the game will continue.
                    credits = 0                                                         # "Credits" are reset to "0".
                    
        if ((playerX == extraCreditX4) and (playerY == extraCreditY4) and (turns != 0) and (whereMove != "")):  # Fifth extra credit, "credit4" option.
            
            credits = 0                                                                 # "Credits" start with a "0" value.
            bExtraLooping4 = True
            x4 = random.randint (1,10)                                                  # I have one variable generated randomly.  
            print "\n" + str(yourName.title()) + ", you just encountered an extra turn option. Answer the following problem correctly to earn an extra turn."
            print "You have 3 guesses otherwise you lose the opportunity and you lose a turn."
            
            while ((credits < 3) and (bExtraLooping4 == True)):                         # For this question, I am giving the user 3 "guesses".
                loopingCredit4 = True                                                   # This will control the fifth extra "credit4" looping.
    
                while loopingCredit4: 
                    guessMyNumber = raw_input("\nGuess my number between 1 and 10: ")   # The "raw_input" that asks the user for a number guess.
                    
                    if (guessMyNumber.isdigit() == True):                               # Checking to see if the "raw_input" is a number.
                        loopingCredit4 = False
                        guessMyNumber = int(guessMyNumber)                              # changing the "raw_input" to an integer.
    
                    else:                                                               # If the "raw_input" is not a number, this message will print.
                        print "That is not a valid number " + str(yourName.title()) + ". You need to learn your numbers. Try again."   
                        loopingCredit4 = True                                           # looping  will re-ask the user for a number again, without decreasing the "guesses".
                    
                if (guessMyNumber == x4):                                               # If the guess is correct, this rule will apply.
                    bExtraLooping4 = False                                              # No need to loop through the question again.
                    bWonGame = False                                                    # Game is not won.
                    turns = turns + 1                                                   # A "turn" is added to the game.
                    print "\nThat's just right, you guessed my number. " + str(yourName.title()) + ", you are great at this game."  # This message will be printed.
                    print "You are on " + "(" + str(playerX) + ", " + str(playerY) + ")"
                    print "You have " + str(turns) + " moves left"                      # Number of "turns" left is outputted to the user.
                    
                else:                                                                   # In case the "guess" is incorrect we have 2 options.
                    if ((credits < 3) and (guessMyNumber < x4)):                        # With this Boolean expression I am outputting a message if the "guess" is "too low".
                        print "\nThat number is too low. Try again."
                        bExtraLooping4 = True                                           # Looping continues to ask the user again.
                        credits = credits + 1                                           # This will use up one "guess".
                    
                    if ((credits < 3) and (guessMyNumber > x4)):                        # On the other hand, if the answer is "too high", this message will print.
                        print "\nThat number is too high. Try again."  
                        bExtraLooping4 = True                                           # Looping continues to ask the user again.
                        credits = credits + 1                                           # "Guesses" will go up by one.
                
            else:                                                                       # If the "guesses" are exhausted.
                if (credits == 3): 
                    turns = turns - 1                                                   # The player will lose a "turn" if he/she does not guess correctly.
                    print "\nSorry " + str(yourName.title()) + ", you used up all your guesses and lost a turn."  # This will print to let the user know that he/she lost a "turn".
                    print "\nYou are on " + "(" + str(playerX) + ", " + str(playerY) + ")"   # Coordinates of the player will print.
                    print "You have " + str(turns) + " moves left."                     # I am printing the new "turns" left.
                    bWonGame = False                                                    # Game is not won.
                    bExtraLooping4 = False                                              # Extra looping of the fifth extra "credit4" will stop after losing a "turn".
                    credits = 0                                                         # "Credits" are reset to "0".
    
    else:                                                                               # This "else" statement will be activated:
        if ((bWonGame == False) or (turns < 1)):                                        # (1) if the game is not won by finding the treasure or
                                                                                        # (2) If the "obstacles" (0-1-2-3) were not answered correctly or 
                                                                                        # (3) No "turns" are left.
            
            print "\nGame over " + str(yourName.title()) + "! Sorry, you lost. Better luck next time."         # This message will be printed to let the user know that he/she lost the game.

def main():                                                                             # This is calling the "main()" function through the designated functions.
    playerName()                                                                        # First function that will run to ask the user's name.
    bKeepGoing = True                                                                   # In case the user wanted to continue the game, the Boolean expression is used to control the rerun.
    while bKeepGoing:                                                                   # "While" the previous Boolean expression is "True".
        moveOnMap()                                                                     # The program will run starting from the "moveOnMap()" function.
        
        gameOver = raw_input("\n" + str(yourName.title()) + ", would you like to play again (Y/N)? ")   # The "raw_input" question that will be printed to the user with a "yes" or "no" (and other) options, asking if he/she wants to play again.
        if (gameOver.lower() == "yes" or gameOver.lower() == "y"):                      # Converting the "raw_input" letters to lowercase and matching them with the user's choice.
            bKeepGoing = True                                                           # If the answer is "yes" or "y", the game will run gain starting from the "moveOnMap()" function.
                                                                                        # I am only running the game again, if the answer is "yes", otherwise the "else" statement will apply.
        else:                                                                           # Otherwise, if the player types anything besides "yes" or "y"...
            bKeepGoing = False                                                          # The Boolean expression is "False" and the game will not run again.
            print "\nThank you for playing " + str(yourName.title()) + ". Give it another try later on."    # This will be printed for the user.
main()                                                                                  # This is the call to "main()". The whole game is running through the "main()" function.
                                                                                        
                                                                                        # P.S. I hope you like the features of my game. I know my comments are probably excessive, but I wanted to be very thorough in explaining my reasoning
                                                                                        # behind the choices of my selected commands. Thank you for all your help during our Lab hours.
    
    