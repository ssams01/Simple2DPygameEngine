from pygame.locals import *

class ScreenResize: 
    def __init__(self): 
        self.types = ["event"]                 
        self.entity_state = None               
        self.name = "screen resize"     
        self.verbose = False                  
        self.children = None          

    def condition_to_act(self, event):           
        if self.entity_state.active == False: 
           return False 

        #checks to see if the user adjusts the screen size before returning true
        if event.type == VIDEORESIZE:
           return True
        return False 
 
    def act(self, event):                       
        if self.condition_to_act(event):

           #sets the screen's dimensions to the new resized size
           self.entity_state.set_mode(event.size, self.entity_state.mode, self.entity_state.depth)
           if self.children != None:
              for i in self.children:
                 i.bounds = (0,0, self.entity_state.dimensions[0], self.entity_state.dimensions[1])
                  
 