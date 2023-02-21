class UpdateTimer: 
    def __init__(self): 
        self.types = ["loop"]                 
        self.entity_state = None              
        self.name = "update_timer_action"    
        self.verbose = False                   
        self.children = []                     
 
    #updates the curren_time variable to the current time
    def act(self, event):                       
       self.entity_state.current_time = self.entity_state.tick()
       return True