import pygame 
from pygame.locals import *

class DrawRectangle:
     def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_rect_action"
        return
    
     def condition_to_act(self,data):
        if self.entity_state == None:
           return False
        if self.entity_state.active == False:
           return False

        #checks to see if there has been any data passed because, can't draw
        #if the method doesn't have the rectangle specifications
        if data == None:
           return False
        return True

     def act(self,data):
        if self.condition_to_act(data):
           self.draw(data)
           if self.verbose:
              print(self.name + " for " + self.entity_state.name)
        return

     #draws a rectangle to the screen with the given specifications it gets from the passed in instance of Rectangle
     #(represented by self)
     def draw(self, screen):
        pygame.draw.rect(screen, self.entity_state.color, self.entity_state.dimensions)
        return

    