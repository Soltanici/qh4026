def box(word):
  l= len(word)
  print("#" * (l+4))
  print("#" + word + "#")
  print("#" * (l+4))

def low(word):
  print(word.lower())

def up(word):
  print(word.upper())

def mirror(word):
  print(word, "l", word[::-1])

def reapeat(word):
  n = int(input("Number of times to repeat: "))
  for times in range(n):
    if times % 2 == 0:
      up(word)
    else:
      low(word)

def run():
  print("Choose an option: 1-Box\n2-Lower\n3-Upper\n4-Mirror\n5-Repetetion")
opt = int(input())
if opt == 1:
  box()
elif opt == 2:
  low()
elif opt == 3:
  up()
elif opt == 4:
  mirror()
elif opt == 5:
  repeat(w)
else:
  print("No such option")
run()