class vehicle():
    make = "Alfa Romeo Giulia"
    color = "Navy"
    horse_power = 280
    cylinders = 4 
    
car1 = vehicle()

print("Make:", car1.make,'\n' "Color:", car1.color,'\n', "Power:", car1.horse_power, '\n', "Number of Cylinders:", car1.cylinders)

class auto:
    
    def __init__(self, model, colori,hp, cc):
        print("This is the constructor")
        self.model = model
        self.colori = colori
        self.hp = hp
        self.cc = cc
        
auto1 = auto("Alfa Romeo Stelvio", "Black", 140, 6)
print(auto)
        