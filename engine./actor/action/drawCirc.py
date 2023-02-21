import pygame 

class DrawCircle: 
     def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_circ_action"
        return

     def condition_to_act(self,data):
        if self.entity_state == None:
           return False
        if self.entity_state.active == False:
           return False

        #checks to see if there has been any data passed because, can't draw
        #if the method doesn't have the circle specifications   
        if data == None:
           return False
        return True

     def act(self,data):
        if self.condition_to_act(data):
           self.draw(data)
           if self.verbose:
              print(self.name + " for " + self.entity_state.name)
        return

     #draws a circle to the screen with the given specifications it gets from the passed in instance of Circle 
     #(represented by self)
     def draw(self,screen):
        pygame.draw.circle(screen, self.entity_state.color, self.entity_state.position, self.entity_state.radius)
        return