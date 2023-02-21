import pygame 


#initializes the rectangle with the needed values that were passed in the make_rect method call
class Rectangle: 
    def __init__(self, color, x, y, width, height, name="rectangle_entity"): 
        self.actions = []         
        self.color = color    
        self.dimensions = [x, y, width, height]
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

    # Check whether a position is inside the bounds 
    def is_inside(self, pos):  
       if pos[0] < self.dimensions[0]: 
          return False 
       if pos[0] > self.dimensions[2] + self.dimensions[0]: 
          return False 
       if pos[1] < self.dimensions[1]: 
          return False 
       if pos[1] > self.dimensions[3] + self.dimensions[1]: 
          return False 
       return True 