class Square:

    def  __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = 0
        self.perimeter = 0

    def calc_area(self):
        self.area = self.length * self.width
        return self.area

    def calc_perimeter(self):
        self.perimeter = self.length * 4
        return self.perimeter


if __name__ == '__main__':

    length = int(input("Enter the length of the square: "))
    width = int(input("Enter the width of the square: "))
    my_square = Square(length, width)

    while True:
        choice = input("What should I do? Calculate [A]rea or [P]erimeter: ").upper()
        if choice not in "AP" or len(choice) != 1:
            continue
        elif choice == "A":
            print(f"The area of the square is {my_square.calc_area()}")
        elif choice == "P":
            print(f"The perimeter of the square is {my_square.calc_perimeter()}")
