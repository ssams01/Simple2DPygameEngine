class SpringForce: 
    def __init__(self, name = "spring_force"): 
        self.spring_constant = 0.0025
        self.actions = []           
        self.name = name         
        self.verbose = False      
        self.active = True
        return 
 
    def insert_action(self, a):   
       a.entity_state = self 
       self.actions.append(a) 
       return 