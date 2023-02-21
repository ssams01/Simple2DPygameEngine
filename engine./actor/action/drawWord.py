import pygame

class DrawWord: 
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_word_action"
        return
    
    def condition_to_act(self,data):
       if self.entity_state == None:
          return False
       if self.entity_state.active == False:
          return False

       #checks to see if there has been any data passed because, can't draw
       #if there is no word
       if data == None:
          return False
       return True

    def act(self,data):
       if self.condition_to_act(data):
          self.draw(data)
          if self.verbose:
             print(self.name + " for " + self.entity_state.name)
       return
    
     #draws a word to the screen with the given specifications it gets from the passed in instance of Word
     #(represented by self)
    def draw(self, screen):

       #specifying the font style (default) and the font size
       font = pygame.font.Font(None, 30)

       letter = font.render(str(self.entity_state.word), True, self.entity_state.color)
       screen.blit(letter, self.entity_state.location)
       return 

    