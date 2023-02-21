import pygame
from pygame import mixer
from pygame.locals import *

class EmitSound: 
    def __init__(self): 
        self.types = ["event"]                 
        self.entity_state = None               
        self.name = "emit_sound"     
        self.verbose = True                   
        self.children = []                       
 
    #checks which action is occuring and plays the appropriate sound for which action it is
    def act(self, data): 
       if data == "button_pressed_action":
          getSound = "/Users/Stephen Sams/OneDrive/Desktop/vinsanity/assets/sounds/all_might_i_am_here.wav"
          pressedSound = mixer.Sound(getSound)
          pressedSound.play()

       if data == "alarm_action":
          getSound = "/Users/Stephen Sams/OneDrive/Desktop/vinsanity/assets/sounds/discord_notification.wav"
          timerSound = mixer.Sound(getSound)
          timerSound.play()
 
