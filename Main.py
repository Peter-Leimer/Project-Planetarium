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

selection = str(input("Pick a Planet (By name or type all for the whole solar system): "))

if (selection == "mercury" or selection == "Mercury"):
       print(str(Mercury))
elif (selection == "venus" or selection == "Venus"):
       print(str(Venus))
elif (selection == "Earth" or selection =="earth"):
       print(str(Earth))
elif (selection == "mars" or selection =="Mars"):
       print(str(Mars))
elif (selection == "jupiter" or selection == "Jupiter"):
       print(str(Jupiter))
elif (selection == "saturn" or selection == "Saturn"):
       print(str(Saturn))
elif (selection == "uranus" or selection == "Uranus"):
       print(str(Uranus))
elif (selection == "neptune" or selection == "Neptune"):
       print(str(Neptune))
elif (selection == "all" or selection == "All"):
       print(str(Mercury))
       print(str(Venus))
       print(str(Earth))
       print(str(Mars))
       print(str(Jupiter))
       print(str(Saturn))
       print(str(Uranus))
       print(str(Neptune))
