# Distance Calculator
import math


def calculate(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    print("WELCOME TO THE DISTANCE CALCULATOR!")

    x1 = float(input("Enter X1 Value: "))
    y1 = float(input("Enter Y1 Value: "))
    x2 = float(input("Enter X2 Value: "))
    y2 = float(input("Enter Y2 Value: "))

    print(f"Distance between the two points is {calculate(x1, y1, x2, y2)}")


main()
