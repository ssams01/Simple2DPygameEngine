from pygame.locals import * 
 
class ButtonPressed: 
    def __init__(self): 
        self.types = ["event"] 
        self.entity_state = None 
        self.name = "button_pressed_action" 
        self.children = [] 
 
    def condition_to_act(self, event): 
       if self.entity_state == None: 
          return False 
       if self.entity_state.active == False: 
          return False 

       #checks if the event was a mouse click
       if event.type == MOUSEBUTTONDOWN: 

          # check whether the person clicked within the "whackabox"
          pos = event.pos 
          return self.entity_state.is_inside(pos) 
       return False 
 
    def act(self, event): 
       if self.condition_to_act(event): 

          #loops through and runs all the child actions of press_button
          for c in self.children: 
             c.act(self.name) 
          if self.verbose: 
             print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
       return  