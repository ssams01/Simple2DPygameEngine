
import pygame 

#initializes the letter with the needed values that were passed in the make_circ method call
class Circle: 
    def __init__(self,color,x, y,radius,name="circ_entity"): 
        self.actions = []          
        self.name = name
        self.color = color   
        self.position = [x, y] 
        #self.position = self.center 
        self.radius = radius 
        self.verbose = False       
        self.active = True         
        return 
 
    def insert_action(self, a):     
       a.entity_state = self 
       self.actions.append(a) 
       if self.verbose:
          print("\t" + self.name + " added " + a.name)
       return 