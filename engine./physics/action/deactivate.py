class Deactivate: 
    def __init__(self): 
        self.types = ["position"]                 
        self.entity_state = None               
        self.name = "deactivate_action"   
        self.verbose = False                   
        self.children = []                     
 
    def condition_to_act(self, data):     
       if self.entity_state == None: 
          return False  

       #checks to see if the entity is already False because,
       #you can't deactivate what is already deactive
       if self.entity_state.active == False: 
          return False 
       return True  
 
    def act(self, data):    
              
       if self.condition_to_act(data):    
          for d in data:
         
             #sets the particle at the index's active_particle to False thus deactivating it 
             self.entity_state.active_particle[d] = False

       return