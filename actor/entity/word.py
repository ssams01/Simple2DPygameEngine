import pygame 

#initializes the word with the needed values that were passed in the make_word method call
class Word: 
    def __init__(self, x, y, color, word, name = "word_entity"): 
        self.actions = []   
        self.location = [x, y] 
        self.color = color
        self.word = word 
        self.name = name         
        self.verbose = False       
        self.active = True
        return       

    def insert_action(self, a):    
       a.entity_state = self 
       self.actions.append(a) 
       if self.verbose:
          print("\t" + self.name + " added " + a.name)
       return