import pygame
from pygame.locals import *

class CheckLetter: 
    def __init__(self,word): 
       self.types = ["event"]                 
       self.entity_state = None               
       self.name = "check_letter_action"    
       self.verbose = True                   
       self.children = []
       self.word = word
       self.rightGuesses = []
       self.wrongGuesses = []
       self.maxWrongGuesses = 7        

    def condition_to_act(self, event):
       if self.entity_state == None:
          return False
       if self.entity_state.active == False:
          return False

       #checks to make sure that the event that happend was a key being pressed before proceeding
       if event.type != KEYDOWN:
          return False
       return True           
 
    def act(self, event):
       if self.condition_to_act(event):

          #gets the letter of the key the user pressed
          self.get_letter(event)

          #draws the respective letters and hangman parts
          self.draw()

          if self.verbose:
             print(self.name + " for " + self.entity_state.name)

       return

    def draw(self):

      #Goes through and makes it to where when a right letter is pressed, the rectangle representing the letter
      #disappears and the letter is visible on the screen
      for i in self.word:
         if i in self.rightGuesses:
            self.onAndOff(str(i) + "_letter", True)
            self.onAndOff(str(i) + "_letterRectangle", False)

      #makes each part of the hangman appear as a wrong letter is guessed
      for i in range(1, len(self.wrongGuesses)):
         self.onAndOff("hangman" + str(i), True)

    #sets the entity's active attribute to either True or False in order to
    #make them appear and disappear depending on the state of the game
    def onAndOff(self, name, status):
       for i in self.entity_state.actions:
          if i.name == "screen display":
             for e in i.children:
                if e.entity_state.name == name:
                   e.entity_state.active = status

    #goes through each letter of the generated word and compares each of its characters with the key pressed
    #by the user and if it is in the word, it adds it to the list of rightGuesses, and if not the list of wrongGuesses
    def letterComparer(self, pressedLetter):
       for char in self.word:
          if char == pressedLetter:
            if pressedLetter not in self.rightGuesses:
               self.rightGuesses.append(pressedLetter)
            print("correctly guessed the letter: " + pressedLetter)
       if pressedLetter not in self.rightGuesses:
          if pressedLetter not in self.wrongGuesses:
             self.wrongGuesses.append(pressedLetter)
          print(pressedLetter + " is not one of the letters in the word")
       return
    
    #checks to see which letter is pressed and prints to the screen which one to help show that the key press was registered and then
    #passes that pressed letter to the "letterComparer" method to check if the word to be guessed has that letter
    def get_letter(self, event):
       if event.type == KEYDOWN:
          if event.key == K_q:
             if self.verbose:
                print("Key q pressed")
                self.letterComparer("q")
          elif event.key == K_w:
             if self.verbose:
                print("Key w pressed")
                self.letterComparer("w")
          elif event.key == K_e:
             if self.verbose:
                print("Key e pressed")
                self.letterComparer("e")
          elif event.key == K_r:
             if self.verbose:
                print("Key r pressed")
                self.letterComparer("r")
          elif event.key == K_t:
             if self.verbose:
                print("Key t pressed")
                self.letterComparer("t")
          elif event.key == K_y:
             if self.verbose:
                print("Key y pressed")
                self.letterComparer("y")
          elif event.key == K_u:
             if self.verbose:
                print("Key u pressed")
                self.letterComparer("u")
          elif event.key == K_i:
             if self.verbose:
                print("Key i pressed")
                self.letterComparer("i")
          elif event.key == K_o:
             if self.verbose:
                print("Key o pressed")
                self.letterComparer("o")
          elif event.key == K_p:
             if self.verbose:
                print("Key p pressed")
                self.letterComparer("p")
          elif event.key == K_a:
             if self.verbose:
                print("Key a pressed")
                self.letterComparer("a")
          elif event.key == K_s:
             if self.verbose:
                print("Key s pressed")
                self.letterComparer("s")
          elif event.key == K_d:
             if self.verbose:
                print("Key d pressed")
                self.letterComparer("d")
          elif event.key == K_f:
             if self.verbose:
                print("Key f pressed")
                self.letterComparer("f")
          elif event.key == K_g:
             if self.verbose:
                print("Key g pressed")
                self.letterComparer("g")
          elif event.key == K_h:
             if self.verbose:
                print("Key h pressed")
                self.letterComparer("h")
          elif event.key == K_j:
             if self.verbose:
                print("Key j pressed")
                self.letterComparer("j")
          elif event.key == K_k:
             if self.verbose:
                print("Key k pressed")
                self.letterComparer("k")
          elif event.key == K_l:
             if self.verbose:
                print("Key l pressed")
                self.letterComparer("l")
          elif event.key == K_z:
             if self.verbose:
                print("Key z pressed")
                self.letterComparer("z")
          elif event.key == K_x:
             if self.verbose:
                print("Key x pressed")
                self.letterComparer("x")
          elif event.key == K_c:
             if self.verbose:
                print("Key c pressed")
                self.letterComparer("c")
          elif event.key == K_v:
             if self.verbose:
                print("Key v pressed")
                self.letterComparer("v")
          elif event.key == K_b:
             if self.verbose:
                print("Key b pressed")
                self.letterComparer("b")
          elif event.key == K_n:
             if self.verbose:
                print("Key n pressed")
                self.letterComparer("n")
          elif event.key == K_m:
             if self.verbose:
                print("Key m pressed")
                self.letterComparer("m")
          return