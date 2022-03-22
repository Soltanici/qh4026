#initialise an empty dictionary
phonebook = {}
d2 = dict()
#initialise a non empty dictionary
piotr = {"Name":"Piotr", "Age": 18, "Doggo": False, "Title":"Mr"}
#printing full dictionary
print(piotr)
print(len(piotr))
#acces individual elements from the dictionary
print(piotr["Age"])
print(piotr["Doggo"])
print(f'{piotr["Name"]} is {piotr["Age"]}  years old and their title is {piotr["Title"]}')
#add elements to dictionary
phonebook["Hugo"] = "+447706224562"
phonebook["Sadia"] = "+44776326622"
phonebook["Lucian"] = "+63156213122"
phonebook["Roxana"] = None
print(phonebook)
#add more items to the phonebook
for i in range(3):
  name = input("Enter new name :")
  numb = input(f"Enter number for {name}: ")
  phonebook[name] = numb
print(phonebook)
#calling a particular person from phoneook
name = input("Who you gonna call?")
if name in phonebook:
  print(f"Calling {name} with number {phonebook[name]}")
else:
  print(f"This perrons is not in your phonebook!")