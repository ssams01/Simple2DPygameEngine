class PositionSolveAction: 
    def __init__(self): 
        self.types = ["physics"]              
        self.entity_state = None      
        self.dt = 1.0          
        self.name = "position_solve_action"    
        self.verbose = False                   
        self.children = []                     

    def condition_to_act(self, data):           
       if self.entity_state == None: 
          return False 
       if self.entity_state.active == False: 
          return False 
       return True 
 
    def act(self, data):                       
       if self.condition_to_act(data):
          for i in range(0, len(self.entity_state.position)):

             #updates the positions of the active_particles
             if self.entity_state.active_particle[i]:
                self.entity_state.position[i][0] = self.entity_state.position[i][0] + self.dt + self.entity_state.velocity[i][0] 
                self.entity_state.position[i][1] = self.entity_state.position[i][1] + self.dt + self.entity_state.velocity[i][1]  

          #collisions can be handled via children    
          for c in self.children:             
             c.act(self.entity_state) 
          if self.verbose:                  
             print(self.name + " for " + self.entity_state.name) 
       return  
 