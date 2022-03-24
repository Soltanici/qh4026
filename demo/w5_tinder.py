def interests():
  print("Enter yput interests, one after the other, and enter \ stop \ when you are done")
  s1 = set()
  while True:
    interest = input()
    if interest.lower() == "stop":
      break
    else:
      s1.add(interest)
  return s1


def tinderDaSecond():
  print("First person: ")
  p1 = interests()
  print("Second person: ")
  p2 = interests()
  common = p1.intersection(p2)
  if len(common) >=3:
    print(f"Yay -You have a match in heaven! You have {len(common)} common interest")
  else:
    print(f"Well , I don't think it will work. You only have {len(common)} common interests")
tinderDaSecond()