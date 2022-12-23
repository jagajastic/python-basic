def greetings():
  print('Hello there!')


def sayHi(name):
  print(f"Hello, {name.capitalize()}")
  return name.capitalize()


sayHi("james") # calling the function 

def yourName():
  name = input("What's your name? ")
  print(f"Hello, {name.capitalize()}")


yourName()