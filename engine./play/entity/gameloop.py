import pygame
from pygame.locals import *

class GameLooper():
    def __init__(self, name = "game_looper"):
        self.loop_content = []
        self.event_content = []
        self.display_content = []
        self.counter = 0
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_entity(self, e):
       if self.verbose:
          print("inserting entity " + str(e.name))

       #inserts each action associated with the created entities 
       for a in e.actions:
          self.insert_action(a)
       return

    #checks the type of the action passed in and assigns it the appropriate list
    def insert_action(self, a):
       if "event" in a.types:
           self.event_content.append(a)
           if self.verbose:
              print("\t" + self.name + " added " + a.name + " event action")
       if "loop" in a.types:
           self.loop_content.append(a)
           if self.verbose:
              print("\t" + self.name + " added " + a.name + " loop action")
       if "display" in a.types:
           self.display_content.append(a)
           if self.verbose:
              print("\t" + self.name + " added " + a.name + " display action")
       return

    def loop(self):

       #creates infinite loop 

        while self.active:
            events = pygame.event.get()
            for e in events:
                for a in self.event_content:
                    a.act(e)
            for a in self.loop_content: 
                    a.act(None)
            for a in self.display_content:
                    a.act(None)
            if self.verbose:
               self.counter += 1
               print(self.name + " counter = " + str(self.counter))

        return

