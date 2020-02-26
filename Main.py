#main
from Planets import Planets

Earth = Planets("Earth" , "Rocky-Habitable",12756 )
Venus =  Planets("Venus" , "Rocky-Uninhabitable", 12104)
Mercury = Planets("Mercury" , "Rocky-Uninhabitable", 4878)
Jupiter = Planets("Jupiter" , "Gas Giant",142984 )
Saturn = Planets("Saturn" , "Gas Giant",120536 )
Neptune = Planets("Neptune" , "Gas Giant",49532 )
Mars = Planets("Mars" , "Rocky-Uninhabitable",6794 )
Uranus = Planets("Uranus" , "Gas Giant",51118 )

print(str(Mercury))
print(str(Venus))
print(str(Earth))
print(str(Mars))
print(str(Jupiter))
print(str(Saturn))
print(str(Uranus))
print(str(Neptune))
