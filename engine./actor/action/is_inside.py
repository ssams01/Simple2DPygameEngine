import pygame 
from pygame.locals import *

class IsInside:
    def __init__(self):
        self.types = ["loop"] 
        self.entity_state = None
        self.verbose = False
        self.children = []
        self.name = "is_inside_action"
        return

    def condition_to_act(self,data): 
       if self.entity_state == None:
          return False
       if self.entity_state.active == False:
          return False
       if data == None:
          return False
       return True

    def act(self, data):
      if self.condition_to_act(data):
         
         #meant to hold the index of all the particles that are found to 
         #be inside the entity
         is_inside_index = []
    
         #loops through each particle position
         for i in range(0, len(data.position)):

            #checks to see if the particle is inside the entity and if so
            #activates it
            if(self.is_inside(data.position[i])):

               #adds the index to the list of particle indexes and
               #if it's not there, adds it
               if i not in is_inside_index:
                  is_inside_index.append(i)

               #passes the children action the list of particle index's that
               #"are inside" so that, they will only act on this particles
               for c in self.children[:1]:
                  c.act(is_inside_index)

    # Check whether a position is inside the bounds 
    def is_inside(self, pos):  
       if pos[0] < self.entity_state.dimensions[0]: 
          return False 
       if pos[0] > self.entity_state.dimensions[2] + self.entity_state.dimensions[0]: 
          return False 
       if pos[1] < self.entity_state.dimensions[1]: 
          return False 
       if pos[1] > self.entity_state.dimensions[3] + self.entity_state.dimensions[1]: 
          return False 
       return True 



