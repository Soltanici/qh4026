print("What is your name, human!")
n = input()
print("How old are you?")
a = int(input())
print("How tall are you?  (in meters)")
h = float(input())
print("How much do you weight? (in KG)")
w = float(input())
bmi = w/(h**2)
print(f"{n} you are {a} years old and your BMI {bmi:.2f}")