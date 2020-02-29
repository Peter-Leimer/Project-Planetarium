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



def selection ():
  selection = str(input("Pick a Planet (By name or type all for the whole solar system ): "))

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
       
       
 

def choose ():
  x=0
  while (x==0):
    print(selection())
    choose = str(input(f"choose another? Y,N: "))
    if (choose == "n" or choose == "N"):
       x+=1
       print("QUITER!")
    elif (choose == "y" or choose == "Y"):
      choose = "X"

print(choose())
