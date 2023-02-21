import pygame

class DrawHud: 
    def __init__(self): 
       self.types = ["display"]               
       self.entity_state = None               
       self.name = "draw_hud_action"    
       self.verbose = False                   
       self.children = []                       
       return
 
    def condition_to_act(self,data): 
       if self.entity_state == None: 
          return False 
       if self.entity_state.active == False: 
          return False 

       #can't draw anything to the hud if there is nothing to draw
       if data == None: 
          return False 
       return True 
 
    def act(self,data): 
       if self.condition_to_act(data): 
          self.draw(data) 
          if self.verbose: 
             print(self.name + " for " + self.entity_state.name) 
       return 
 
    def draw(self, data): 

       #loops through each of the children of the hud...
       for c in self.entity_state.children:

         #...and runs the actions of each of the entities
          for a in c.actions:
            a.act(data)
       return 