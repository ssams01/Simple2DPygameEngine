#Initializes the counter with the value and name passed in the make_counter call
class Counter: 
    def __init__(self, number, name = "counter"): 
        self.actions = []          
        self.number = number 
        self.name = name         
        self.verbose = False       
        self.active = True      
        return 
 
    def insert_action(self, a):     
       a.entity_state = self 
       self.actions.append(a) 
       return 