name=input("Enter you name: ")
print("Hello, " + name + "! Welcome to the Web Programming course.")
print(f"Hello, {name}! Welcome to the Web Programming course.This line is printed using an f-string.")

name=["John", "Jane", "Doe"]
print("Names in the list:", name)
print(name[0])
print(name[0][0])

def square(x):
    return x * x

for i in range(5):
    print(f"The square of {i} is {square(i)}")

class Point:
    def __init__(self,input1,input2):
        self.input1= input1
        self.input2= input2

p= Point(3, 4)
print(f"Point coordinates: ({p.input1}, {p.input2})")


# how to implement my own __init__ method in a class
class Point:
    def __create__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

p = Point()           # No arguments here
p.__create__(10, 15)  # Now initialize
print(f"Point coordinates: ({p.input1}, {p.input2})")