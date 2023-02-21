class GravityForceAction: 
    def __init__(self): 
        self.types = ["force"]                 
        self.entity_state = None               
        self.name = "gravity_force_action"    
        self.verbose = False                  
        self.children = []                

    def condition_to_act(self, data):          
       if self.entity_state == None: 
          return False 
       if self.entity_state.active == False: 
          return False 
       if data == None:
          return False 
       return True
 
    def act(self, data):

       #calls the first child action and runs it
       self.children[0].act(data)

       #the data is the particle entity_state                        
       if self.condition_to_act(data):
          for i in range(0, len(data.acceleration)):

             #adjusts the acceleration based on the "amount of gravity"
             if data.active_particle[i]:
                data.acceleration[i][0] = data.acceleration[i][0] + self.entity_state.gravity[0] 
                data.acceleration[i][1] = data.acceleration[i][1] + self.entity_state.gravity[1]        
       
       #calls the second child action and runs it
       self.children[1].act(data)

       if self.verbose:                    
          print( self.name + " for " + self.entity_state.name) 
       return  
 