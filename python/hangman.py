import sys

sys.path.insert(0, "./")

import engine.play as pl
import engine.actor as act
from english_words import english_words_lower_alpha_set
import random

################## Viewer ############################################# 

#generating the random word to be guessed
while True:
    hangmanWord = random.choice(tuple(english_words_lower_alpha_set))
    if len(hangmanWord) > 4 and len(hangmanWord) < 9:
        break

#creates frame 
viewer = pl.make_frame_viewer(1280,720) 
 
#adds necessary game actions to frame entity (screen updater, game/frame closer, letter checker)
viewer.insert_action(pl.make_terminate_action()) 
viewer.set_title("HangMan")
display = pl.make_screen_display_action() 
viewer.insert_action(display) 
viewer.insert_action(act.make_check_letter(hangmanWord))
 
game_content = [viewer] 

################## Shapes and Letters #################################

#rectangles and circles

#draws the rectangles necessary to create the hangman stand

standOne = act.make_rect(275,75, 35, 450, 255, 0, 0)
standOne.insert_action(act.make_draw_rect())
standOne.verbose = True
display.insert_entity(standOne)
game_content.append(standOne)

standTwo = act.make_rect(310,75, 300, 35, 255, 0, 0)
standTwo.insert_action(act.make_draw_rect())
standTwo.verbose = True
display.insert_entity(standTwo)
game_content.append(standTwo)

standThree = act.make_rect(610,75, 35, 90, 255, 0, 0)
standThree.insert_action(act.make_draw_rect())
standThree.verbose = True
display.insert_entity(standThree)
game_content.append(standThree)

standFour = act.make_rect(275,75, 35, 400, 255, 0, 0)
standFour.insert_action(act.make_draw_rect())
standOne.verbose = True
display.insert_entity(standFour)
game_content.append(standFour)

standFive = act.make_rect(195, 525, 200, 35, 255, 0, 0)
standFive.insert_action(act.make_draw_rect())
standFive.verbose = True
display.insert_entity(standFive)
game_content.append(standFive)

#creates each piece of the hangman and sets the active (and thus visibility) of them to False until,
#Each amount of wrong guesses has been committed
head = act.make_circ(630,190, 50, 0, 0, 255)
head.insert_action(act.make_draw_circ())
head.verbose = True
head.active = False
head.name = "hangman1"
display.insert_entity(head)
game_content.append(head)

body = act.make_rect(613,235, 35, 150, 0, 0, 255)
body.insert_action(act.make_draw_rect())
body.verbose = True
body.active = False
body.name = "hangman2"
display.insert_entity(body)
game_content.append(body)

armOne = act.make_rect(500,275, 115, 25, 0, 0, 255)
armOne.insert_action(act.make_draw_rect())
armOne.verbose = True
armOne.active = False
armOne.name = "hangman3"
display.insert_entity(armOne)
game_content.append(armOne)

armTwo = act.make_rect(640,275, 115, 25, 0, 0, 255)
armTwo.insert_action(act.make_draw_rect())
armTwo.verbose = True
armTwo.active = False
armTwo.name = "hangman4"
display.insert_entity(armTwo)
game_content.append(armTwo)

torso = act.make_rect(540,385, 180, 35, 0, 0, 255)
torso.insert_action(act.make_draw_rect())
torso.verbose = True
torso.active = False
torso.name = "hangman5"
display.insert_entity(torso)
game_content.append(torso)

legOne = act.make_rect(540,420, 35, 85, 0, 0, 255)
legOne.insert_action(act.make_draw_rect())
legOne.verbose = True
legOne.active = False
legOne.name = "hangman6"
display.insert_entity(legOne)
game_content.append(legOne)

legTwo = act.make_rect(685,420, 35, 85, 0, 0, 255)
legTwo.insert_action(act.make_draw_rect())
legTwo.verbose = True
legTwo.active = False
legTwo.name = "hangman7"
display.insert_entity(legTwo)
game_content.append(legTwo)

#Creates rectangles for each letter in the generated word

#needed for formatting
blankSpace = 0

#loops as many times as there are letters in the generated word and creates the rectangles
for i in hangmanWord:
   wordRectangle = act.make_rect((500 + blankSpace), 600, 35, 35, 0, 255, 0)
   wordRectangle.insert_action(act.make_draw_rect())
   wordRectangle.verbose = True
   wordRectangle.active = True
   wordRectangle.name = str(i) + "_letterRectangle"
   blankSpace += 50
   display.insert_entity(wordRectangle)
   game_content.append(wordRectangle)

#letters

#displaying generated word to the screen
blankSpace = 0

#holds each of the letters in the generated word so that, they can be passed to our compare 
#method one at a time and compared to the keys that are pressed
wordLetters = []

#loops as many times as there are letters in the generated word and draws the letters to the screen
#and makes them non-visible (to be made visible when guessed correctly)
for i in hangmanWord:
    currentLetter = str(i)
    wordLetter = act.make_letter((500 + blankSpace), 600, 0, 0, 0, currentLetter)
    wordLetter.name = str(i) + "_letter"
    wordLetter.insert_action(act.make_draw_letter())
    wordLetter.active = False
    wordLetters.append(wordLetter)

    blankSpace += 50

for i in wordLetters:
    display.insert_entity(i)
    game_content.append(i)

################## Looper ############################################# 
 
#creates the game loop and passes game content (entities and actions)
game_looper = pl.make_game_looper(game_content) 
game_looper.verbose = False 
game_looper.loop() 