class Planets(object):

    
    def __init__(self, name, designation, diameter):
         self.name = name
         self.designation = designation
         self.diameter = diameter
        
    def __str__(self):
         return f"Planet: {self.name}  Type: {self.designation}  Diameter: {self.diameter} Km"
         
