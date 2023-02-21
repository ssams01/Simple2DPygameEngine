import pygame


class Timer: 
    def __init__(self, alottedTime, startTime, currentTime, elapsedTime, name = "timer"): 

       #creates Clock object
        whackClock = pygame.time.Clock() 
        self.clock = whackClock
        self.actions = []          
        self.name = name        
        self.active = True      
        self.alotted_time = alottedTime
        self.start_time = startTime
        self.current_time = currentTime    
        self.elapsed_time = elapsedTime
        return 
 
    def insert_action(self, a):    
       a.entity_state = self 
       self.actions.append(a) 
       return 
    
    #calculates the start time
    def get_start_time(self):

       #gets the amount of time passed (in millisecond)
       ticktocks = pygame.time.get_ticks()
       tockticks = ticktocks 
       self.start_time = ticktocks - tockticks
       return self.start_time

    #updates the current time
    def tick(self):
       self.current_time = self.current_time + self.clock.tick(45)
       return self.current_time

   #calculates how much time has passed (the elapesed time)
    def get_elapsed_time(self):
       elapsed_time = abs(self.current_time - self.start_time)
       self.elapsed_time = elapsed_time
       return self.elapsed_time 