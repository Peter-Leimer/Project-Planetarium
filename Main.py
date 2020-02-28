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

x=0

def selection ():
  selection = str(input("Pick a Planet (By name or type all for the whole solar system or type end  to end the program): "))

  if (selection == "mercury" or selection == "Mercury"):
       print(str(Mercury))
       #selection()
  elif (selection == "venus" or selection == "Venus"):
       print(str(Venus))
       #selection()
  elif (selection == "Earth" or selection =="earth"):
       print(str(Earth))
       #selection()
  elif (selection == "mars" or selection =="Mars"):
       print(str(Mars))
       #selection()
  elif (selection == "jupiter" or selection == "Jupiter"):
       print(str(Jupiter))
       #selection()
  elif (selection == "saturn" or selection == "Saturn"):
       print(str(Saturn))
       #selection()
  elif (selection == "uranus" or selection == "Uranus"):
       print(str(Uranus))
       #selection()
  elif (selection == "neptune" or selection == "Neptune"):
       print(str(Neptune))
      # selection()
       
  elif (selection == "all" or selection == "All"):
       print(str(Mercury))
       print(str(Venus))
       print(str(Earth))
       print(str(Mars))
       print(str(Jupiter))
       print(str(Saturn))
       print(str(Uranus))
       print(str(Neptune))
       #selection()
       
  elif (selection == "end" or selection == "End"):
       
       print("Program quit")
       I=1


#while (x==0):
 # print(selection()) 
  #  x==1
print(selection())
choose = str(input(f"Do it again Y,N"))
if 
