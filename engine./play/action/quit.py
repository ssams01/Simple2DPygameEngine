from pygame.locals import *

class Terminate:
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "terminate"
        self.children = None
    
    def condition_to_act(self, event):
        if self.entity_state.active == False:
            return False
        if event.type == QUIT:
            return True

        #Adds the functionality of quitting the window when the ESC is pressed
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return True
        return False
    
    #when one of the condtions (ESC key or x button is pressed) is met, "terminates" the game
    def act(self,event):
        if self.condition_to_act(event):
            self.entity_state.terminate()