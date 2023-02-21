class Deactivate: 
    def __init__(self): 
        self.types = ["event"]                 
        self.entity_state = None               
        self.name = "deactivate_action"   
        self.verbose = False                   
        self.children = []                    
 
    def condition_to_act(self, data):         
       if self.entity_state == None: 
          return False  

       #checks to make sure the entities active state is True because,
       #you can't deactivate something that is already deactive   
       if self.entity_state.active == True: 
          return True
       return False 
 
    def act(self, data):                       
       if self.condition_to_act(data):  
        
          #sets the entity's active variable to False thus deactivating it     
          self.entity_state.active = False
       return  
 
 