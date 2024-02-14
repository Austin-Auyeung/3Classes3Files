class Rectangle:

    def  __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = 0
        self.perimeter = 0

    def calc_area(self):
        self.area = self.length * self.width
        return self.area

    def calc_perimeter(self):
        self.perimeter = self.length * 2 + self.width * 2
        return self.perimeter


if __name__ == '__main__':

    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    my_rectangle = Rectangle(length, width)

    while True:
        choice = input("What should I do? Calculate [A]rea or [P]erimeter: ").upper()
        if choice not in "AP" or len(choice) != 1:
            continue
        elif choice == "A":
            print(f"The area of the rectangle is {my_rectangle.calc_area()}")
        elif choice == "P":
            print(f"The perimeter of the rectangle is {my_rectangle.calc_perimeter()}")