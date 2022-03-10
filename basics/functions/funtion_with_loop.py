def cross_bridge(bob):
  for i in range(bob):
    print("Crossed step")
  if bob > 5:
    print("The bridge is colapsing!")
  else:
    print("We must be going")


cross_bridge(3)
cross_bridge(6)