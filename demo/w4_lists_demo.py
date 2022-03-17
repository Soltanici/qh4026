#DECLARE AN EMPTY LIST
bleh = []
meh = list()
#declare a non-empty list
yummy = ["Pizza","Lasagne","Fish and Chips"]
#Print an entire list
print(yummy)
#print a single item
print(yummy[2])
#print some items
print(yummy[:2])
#add elements to our list(expandit)-adding at the end
print(bleh)
bleh.append("Sea food")
bleh.append("Soup")
bleh.append("Liver")
print(bleh)

#adding multiple items to the list, baser on user input 
for i in range(5):
  
 yummy.append(input("Enter new Yummy Food: "))
 yummy[i]  = input() 
print(yummy)
#adding new item, at specific position on the list
bleh.insert(3,"Cabbage")
print(bleh)
#remove items from list based on name 
if "Potates" in bleh:
 bleh.remove("Potatoes")

bleh.remove("Soup")
print(bleh)
#remove item by index

lista = ["Fred", True , 6 , 8, -3.6, Flase, 55]
for item in lista:
  if isinstance(item, str):
    print(item)