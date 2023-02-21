class StartTimer: 
    def __init__(self): 
        self.types = ["loop"]                 
        self.entity_state = None               
        self.name = "start_timer_action"    
        self.verbose = False                    
        self.children = []                    
 
    def condition_to_act(self, event):           
       if self.entity_state == None: 
          return False 
       if self.entity_state.active == False: 
          return False 

       #if the "whackabox" moves, then the timer's start time
       #needs to be reset 
       if event == "move_action": 
          return True

      #if the alarm goes off the timer's start time needs
      #to be reset
       if event == "alarm_action":
          return True
       return False 
 
    def act(self, event):                      
       if self.condition_to_act(event):             
          self.start_timer()
       return  

    #calls the necessary timer methods to reset the start timer
    def start_timer(self):
       self.entity_state.get_start_time()
       self.entity_state.get_elapsed_time()
       self.entity_state.current_time = 0
       return 

 
 