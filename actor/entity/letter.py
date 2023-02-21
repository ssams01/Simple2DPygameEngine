import pygame 

#initializes the letter with the needed values that were passed in the make_letter method call
class Letter: 
    def __init__(self, x, y, color,letter, name="letter_entity"): 
        self.actions = []   
        self.location = [x, y] 
        self.color = color
        self.letter = letter   
        self.name = name         
        self.verbose = False       
        self.active = True       

    def insert_action(self, a):    
       a.entity_state = self 
       self.actions.append(a) 
       if self.verbose:
          print("\t" + self.name + " added " + a.name)
       return