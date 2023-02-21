class hud: 
    def __init__(self,name = "hud"): 
        self.actions = []
        self.children = []
        self.name = name  
        self.verbose = False      
        self.active = True      
        return 
 
    def insert_action(self, a):       
       a.entity_state = self 
       self.actions.append(a) 
       if self.verbose:
          print("\t" + self.name + " added " + a.name)
       return 
 