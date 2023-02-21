import pygame
from pygame.locals import *
from sys import exit

class FrameViewer():
    def __init__(self, nx = 1280, ny = 720, mode = RESIZABLE | DOUBLEBUF, depth = 12, title = "HangMan", name = "Frame_Viewer"):
        pygame.init()
        self.screen = pygame.display.set_mode((nx,ny), mode, depth)
        self.dimensions = [nx, ny] 
        self.mode = mode
        self.depth = depth
        self.title = title
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True

    def insert_action(self, a):
       a.entity_state = self
       self.actions.append(a)
       return
    
    #quits the window
    def terminate(self):
       if self.verbose:
          print(self.name + " terminating") 
       pygame.quit()
       exit()

    #sets the title of the frame window
    def set_title(self, title):
       self.title = title
       pygame.display.set_caption(title)
       if self.verbose:
          print(self.name + " title changed to = " + self.title)
       return

    def set_mode(self, ssize, mode, depth):
       self.screen = pygame.display.set_mode(ssize, mode, depth)
       self.dimensions = [ssize[0], ssize[1]]
       self.mode = mode
       self.depth = depth
       if self.verbose:
          print(self.name + " new size = " + str(self.dimensions))
       return