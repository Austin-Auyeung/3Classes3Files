class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks!")

    def attack(self):
        print(f"{self.name} bites a squirrel!")

    def get_info(self):
        print(f"Your dog, {self.name}, is {self.age} years old. The breed is a {self.breed}.")


name = input("Enter the name of your dog: ")
age = input("Enter the age of your dog: ")
breed = input("Enter the breed of your dog: ")
myDog = Dog(name, age, breed)

while True:
    action = input("What would you like your dog to do? [B]ark, [A]ttack, or get [I]nfo: ").upper()
    if action not in "BAI" or len(action) != 1:
        continue
    elif action == "B":
        myDog.bark()
    elif action == "A":
        myDog.attack()
    elif action == "I":
        myDog.get_info()