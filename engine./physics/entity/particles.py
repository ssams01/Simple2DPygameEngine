class Particle: 
    def __init__(self, name = "particle"):
        self.position = []
        self.velocity = []
        self.acceleration = []
        self.mass = []
        self.active_particle = [] 
        self.actions = []         
        self.name = name          
        self.verbose = False      
        self.active = True        
        return 
 
    def insert_action(self, a):    
       a.entity_state = self 
       self.actions.append(a) 
       return 
    
    #adds the attributes of the current particle being created and adds it to
    #the list of "active_particle"'s
    def add_particle(self, p, v, m):
       self.position.append(p)
       self.velocity.append(v)
       self.acceleration.append([0.0,0.0])
       self.mass.append(m)
       self.active_particle.append(True) 