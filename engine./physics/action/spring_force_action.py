class SpringForceAction: 
    def __init__(self): 
        self.types = ["force"]                  
        self.entity_state = None               
        self.name = "spring_force_action"     
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
      
       #the data is the particle entity state
       if self.condition_to_act(data): 
           
          #calls the first child action and runs it
          self.children[0].act(data)
 
          #first, get center of mass
          total_mass = 0.0
          center_of_mass = [0.0, 0.0]
          for i in range(0, len(data.acceleration)):
             if data.active_particle[i]:
                total_mass = total_mass + data.mass[i]
                center_of_mass[0] = center_of_mass[0] + data.mass[i] + data.position[i][0] 
                center_of_mass[1] = center_of_mass[1] + data.mass[i] + data.position[i][1] 
          center_of_mass[0] = center_of_mass[0] / total_mass
          center_of_mass[1] = center_of_mass[1] / total_mass

          #second, force is based on seperation of each particle from center of mass
          for i in range(0, len(data.acceleration)):
             if data.active_particle[i]:
                accel = [0.0, 0.0]
                accel[0] = (center_of_mass[0] - data.position[i][0]) * self.entity_state.spring_constant / data.mass[i]
                accel[1] = (center_of_mass[1] - data.position[i][1]) * self.entity_state.spring_constant / data.mass[i]

                data.acceleration[i][0] = data.acceleration[i][0] + accel[0]
                data.acceleration[i][1] = data.acceleration[i][1] + accel[1]

       #runs the second child action first due to calling the first
       #child action aleady and then calls and runs any others
       for c in self.children[1:]:             
          c.act(data) 
       if self.verbose:                   
          print( self.name + " for " + self.entity_state.name) 
       return  
 