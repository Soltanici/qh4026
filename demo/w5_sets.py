#initialise an empty set
s = set()
s1 = {}
#check the data type is "set"
print(type(s))
#initialise a non-empty set
colours = {"blue", "purple","yellow", "green"}
print(colours)
#adding elements to a set
colours.add("magenda")
colours.add("turquoise")
print(colours)
#remove itemsfrom set
colours.remove("yellow")
print(colours)
#uniqueness of items wit a set
colours.add("red")
colours.add("purple")
print(colours)
#check memembership
if "blue" in colours:
  print("Yay - Ilove blue!")
else:
  print("You are missing important colour:( ")

c = {"Black", "White", "Cyan", "Burgundy", "Beige"}
#union - joining 2 sets together not keeping any duplicates
c2 = colours.union(c)
print(c2)
print(colours)
print(c)
#intersection - looking at "common" elements in both sets
c3 = colours.intersection(c)
print(c3)
#Difference of two sets - keep only elements in one set, not in the other
c4 = colours.differnce(c)
c5 = c.difference(colours)
print(c4)
print(c5)