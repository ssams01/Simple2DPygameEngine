
class Activate: 
    def __init__(self): 
        self.types = ["event"]                 
        self.entity_state = None               
        self.name = "activate_action"   
        self.verbose = False                    
        self.children = []                      
 
    def condition_to_act(self, data):          
       if self.entity_state == None: 
          return False  

       #checks to make sure the entities active state is False because,
       #you can't activate something that is already active   
       if self.entity_state.active == False: 
          return True
       return False 
 
    def act(self, data):                        
       if self.condition_to_act(data): 
     
          #sets the entity's active variable to True thus activating it            
          self.entity_state.active = True
       return  
 
 