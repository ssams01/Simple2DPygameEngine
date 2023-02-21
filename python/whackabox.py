import sys

sys.path.insert(0, "./")

import engine.play as pl 
import engine.actor as act
import engine.ui as ui 
import engine.sound as sd
import engine.utility as ut
import random
from pygame import time
from pygame.locals import * 

class Move: 
   def __init__(self): 
       self.types = ["event"]                  
       self.entity_state = None              
       self.name = "move_action"    
       self.verbose = True                 
       self.children = []                     
 
   def condition_to_act(self, event):          
      if self.entity_state == None: 
         return False 
      if self.entity_state.active == False: 
         return False 

      #makes sure the "whackabox" moves if the alarm goes off
      if event == "alarm_action":
         return True

      #makes sure the "whackabox" moves when the user clicks within the box
      if event.type == MOUSEBUTTONDOWN:
         pos = event.pos
         if self.entity_state.is_inside(pos):
            return True
      return False 
 
   def act(self, data):                       
      if self.condition_to_act(data):        
         self.move()
         if self.verbose:                   
            print( self.name + " for " + self.entity_state.name) 
      return  

   def move(self):

      #sets "whackabox"'s active variable to false while a new position and color are being random generated
      ut.deactivate_action()

      #changes "whackabox"'s position to some random position
      randomX = random.randrange(0, 1280 - self.entity_state.bounds[2])
      randomY = random.randrange(0, 720 - self.entity_state.bounds[3])

      #makes sure the "whackabox" can't appear inside the hud's area
      if randomX < 175 and randomY < 75:
         randomX = 200
         randomY = 100
       
      #changes "whackabox"'s color to some random color
      randomRed = random.randrange(50, 255)
      randomGreen = random.randrange(50, 255)
      randomBlue = random.randrange(50, 255)

      #updates "whackabox" with the randomly generated position and color
      self.entity_state.bounds = (randomX, randomY, 100, 100)
      self.entity_state.color = (randomRed, randomGreen, randomBlue)

      #sets "whackabox"'s active back to true after the position and color have been updated
      ut.activate_action()
      return

class GenerateMessage: 
    def __init__(self): 
        self.types = ["display"]                

        #holds the value for the counter of the "Total: " message line                              
        self.totalCounter = 0

        #holds the value for the counter of the "Successes: " message line
        self.successesCounter = 0
        self.entity_state = None               
        self.name = "generate_message_action"     
        self.verbose = False                   
        self.active = True                
        self.children = []                     
        return
 
    def condition_to_act(self, data):           
       if self.entity_state == None: 
          return False 
       if self.entity_state.active == False: 
          return False 
       if data == None:
          return False
       return True

    def act(self, data):
       if self.condition_to_act(data): 
          self.update_counter_values()
          self.update_counter_displays()
          if self.verbose:                   
                print( self.name + " for " + self.entity_state.name) 
          return        

    def update_counter_values(self):
       for c in self.children:

         #checks the name of the counter in order to make sure that,
         #the right counter is incremented
          if c.name == "total_counter":
             self.totalCounter = c.number
          if c.name == "successes_counter":
             self.successesCounter = c.number
       return

    def update_counter_displays(self):
       for c in self.entity_state.children:
          if c.name == "hud_total_message":

            #updates the current total message line with the current value of the total counter
             c.word = "Total: " + str(self.totalCounter)
          if c.name == "hud_successes_message":

            #updates the current successes message line with the current value of the successes counter
             c.word = "Successes: " + str(self.successesCounter)
       return
          
def make_move_action():
   return Move()

def make_generate_message_action():
   return GenerateMessage()

 
################## Viewer ############################################# 

#creates frame
viewer = pl.make_frame_viewer(1280,720) 
 
#adds necessary game actions to frame entity (screen updater, game/frame closer, letter checker)
viewer.insert_action(  pl.make_terminate_action() ) 
viewer.set_title("WhackABox")
viewer.insert_action(  pl.make_screen_resize_action() ) 
display = pl.make_screen_display_action() 
viewer.insert_action(  display ) 
 
game_content = [ viewer ] 
 
 
################## Button(s) ############################################# 

#makes sure that the whackabox starts at a random position for each run of the program
#while also making sure it doesn't start in the hud area
randomX = random.randrange(175, 1280)
randomY = random.randrange(75, 720)
 
#creates the button with initial position, initial color, and its size
button_bounds = (randomX, randomY,100,100) 
button_color = (255, 30, 30) 
basic_button = ui.make_basic_button(button_bounds, button_color) 
basic_button.name = "whackabox" 
 
#creates and adds the necessary actions to the basicButton entity
press_sound = sd.make_emit_sound_action()
press_action = ui.make_button_press_action()  
press_action.verbose = True
press_action.children.append(press_sound) 
move_action = make_move_action()

basic_button.insert_action(press_action)  
basic_button.insert_action(ui.make_draw_button_action())  
basic_button.insert_action(move_action)           
basic_button.verbose = True            

display.insert_entity(basic_button)    
game_content.append(basic_button)    

### Counter(s) and Counter Action(s) ###
totalCounter = ut.make_counter(0, "total_counter")
successesCounter = ut.make_counter(0, "successes_counter")

totalIncrementor = ut.increment_counter_action()
successesIncrementor = ut.increment_counter_action()

#adds the increment action as a child of the button press action so that the counter(s) will
#increment every time the button is pressed
press_action.children.append(totalIncrementor)
press_action.children.append(successesIncrementor)

totalCounter.insert_action(totalIncrementor)
successesCounter.insert_action(successesIncrementor)

### Hud stuff ###
hud = ui.make_hud()

#creates the "Total: " message line and adds it to the hud
hudTotalMessage = act.make_word(20, 15, 254, 216, 177, "Total: 0", "hud_total_message")
hudTotalMessage.insert_action(act.make_draw_word())
hud.children.append(hudTotalMessage)

#creates the "Successes: " message line and adds it to the hud
hudSuccessesMessage = act.make_word(20, 45, 254 , 216, 177, "Successes: 0", "hud_successes_message")
hudSuccessesMessage.insert_action(act.make_draw_word())
hud.children.append(hudSuccessesMessage)

#Creates an instance of generateMessage and adds the 2 counter entities to it so that the counter's
#value can be updated everytime it increments
hudMessages = make_generate_message_action()
hudMessages.children.append(totalCounter)
hudMessages.children.append(successesCounter)
hud.insert_action(hudMessages)

#inserts the action necessary to make the hud visible
hud.insert_action(ui.make_draw_hud_action())

display.insert_entity(hud)
game_content.append(hud)

### Timer ###
button_timer = ut.make_timer(2000, 0, 0, 0)
timer_action = ut.start_timer_action()
update_timer = ut.update_timer_action()

button_timer.insert_action(timer_action)
button_timer.insert_action(update_timer)

#resets timer if button moves
move_action.children.append(timer_action)

game_content.append(button_timer)

#resets timer if the alarm goes off
timer_alarm = ut.alarm_action(button_timer.alotted_time)
button_timer.insert_action(timer_alarm) 

#add all the child actions the alarm needs to work correctly 
timer_alarm.children.append(timer_action)
timer_alarm.children.append(move_action)
timer_alarm.children.append(totalIncrementor)
timer_alarm.children.append(press_sound)

################## Looper ############################################# 
 
game_looper = pl.make_game_looper( game_content ) 
game_looper.verbose = False 
game_looper.loop()