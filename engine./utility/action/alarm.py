class Alarm: 
    def __init__(self, alottedTime): 
        self.types = ["loop"]                 
        self.entity_state = None               
        self.name = "alarm_action"     
        self.verbose = False                    
        self.children = []                      
        self.alotted_time = alottedTime
 
    def condition_to_act(self, event):
       #print(self.entity_state.current_time)  
       if self.entity_state == None: 
          return False 
       if self.entity_state.active == False: 
          return False 

      #checks to see if the current time is equal or exceeded the timer's alloted time
      #and if so signals for the alarm to go off
       if self.entity_state.current_time >= self.alotted_time: 
          return True
       return False 
 
    def act(self, event):                       
       if self.condition_to_act(event): 
          #loops through and runs all the child actions of alarm        
          for c in self.children:            
             c.act(event) 
             
       return  
 
 