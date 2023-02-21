import pygame 

class ScreenDisplay:
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.children = []
        self.name = "screen display"
        self.verbose = False

        return 

    def insert_action(self, a):
       if "display" in a.types:
           self.children.append(a)

    #checks to see if the entity being passed has an action of type "display"
    #(as in it gets displayed to the screen) and if so adds it to the children list
    def insert_entity(self, e):
       for a in e.actions:
          if "display" in a.types:
              self.children.append(a)
    
    def condition_to_act(self, data):
       if self.entity_state == None:
          return False
       if self.entity_state.active == False:
          return False
       return True

    #updates the screen by clearing the screen buffer to black (using fill()),
    #runs in actions that were of type "display", and finally flip() to "flip the buffer"
    def act(self, data):
       if self.condition_to_act(data):
          self.entity_state.screen.fill((0,0,0))
          for t in self.children:
             t.act(self.entity_state.screen)
          pygame.display.flip()
       return
