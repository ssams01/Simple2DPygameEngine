class Increment: 
    def __init__(self): 
        self.types = ["event"]                 
        self.entity_state = None               
        self.name = "increment_counter_action"    
        self.verbose = False                   
        self.children = []                     
 
    def condition_to_act(self, event):         
       if self.entity_state == None:   
          return False 
       if self.entity_state.active == False: 
          return False

       #checks to see if either the button was pressed or the alarm went off and if so,
       #increments/updates the particular counter instance   
       if event == "button_pressed_action":
          return True
       if event == "alarm_action":
          return True
       return False 
 
    def act(self, event):                       
       if self.condition_to_act(event):       
          self.buttonPressedIncrement()
          if self.verbose:                  
             print( self.name + "'s counter has been updated") 
       return  
    
    #increases the current counter value by 1
    def buttonPressedIncrement(self):

      #converts the counter to an integer so it can be incremented...
       currentCount = int(self.entity_state.number)
       currentCount += 1
       
       #...and then back to a string so that the value can be appended to the appropriate
       #message line in the hud
       backToString = str(currentCount)
       self.entity_state.number = backToString
 
 