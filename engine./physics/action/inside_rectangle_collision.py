class InsideRectangleCollisionAction: 
    def __init__(self): 
        self.types = ["physics"]                 
        self.entity_state = None                
        self.name = "inside_rectangle_action"   
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
 
    #data is the particles
    def act(self, data):                       
       if self.condition_to_act(data):        
          for i in range(0, len(data.position)):
             
             #for each active goes through and corrects the position of the active particle
             #if any of it is outside the rectangle so that it is back inside
             if data.active_particle[i]:
                if data.position[i][0] < self.entity_state.llc[0]:
                   data.position[i][0] = 2.0 * self.entity_state.llc[0] - data.position[i][0]
                   data.velocity[i][0] = -data.velocity[i][0]
                elif data.position[i][0] > self.entity_state.urc[0]:
                     data.position[i][0] = 2.0 * self.entity_state.urc[0] - data.position[i][0]
                     data.velocity[i][0] = -data.velocity[i][0]
                elif data.position[i][1] < self.entity_state.llc[1]:
                     data.position[i][1] = 2.0 * self.entity_state.llc[1] - data.position[i][1]
                     data.velocity[i][1] = -data.velocity[i][1]
                elif data.position[i][1] > self.entity_state.urc[1]:
                     data.position[i][1] = 2.0 * self.entity_state.urc[1] - data.position[i][1]
                     data.velocity[i][1] = -data.velocity[i][1]
          for c in self.children:           
             c.act(data) 
          if self.verbose:                   
             print( self.name + " for " + self.entity_state.name) 
       return  
 