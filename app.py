fName = ""
lName = ""

def input_name():
  global fName, lName
  fName = input("Enter your first name: ")
  lName = input("Enter your last name: ")

def greet():
  input_name()
  print(f"Hi there! {fName} {lName}")

greet()
