class Activate: 
    def __init__(self):
        self.types = ["position"]                
        self.entity_state = None               
        self.name = "activate_action"   
        self.verbose = False                    
        self.children = []                      
 
    def condition_to_act(self, data):       
       if self.entity_state == None: 
          return False  

       #checks to make sure the entities active state is False because,
       #you can't activate something that is already active   
       if self.entity_state.active == True: 
          return False

       return True
 
    def act(self, data):                        
       if self.condition_to_act(data):  
          for i in range(0, len(self.entity_state.active_particle)):

             #sets the particle at the index's active_particle to True thus activating it          
             self.entity_state.active_particle[i] = True
       return  
 