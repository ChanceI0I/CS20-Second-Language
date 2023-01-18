# Dice-Roll-Simulator
import random


def rollDice(Time):
    result = []
    for _ in range (int(Time)):
        result.append([random.randint(1,6),random.randint(1,6)])
    return result


def getSum(Dice:list):
    return sum(Dice)


def Action(Meanu):

    if Meanu == "1":
        return F"{rollDice(1)[0]} (Sum: {getSum(rollDice(1)[0])})\n"
    
    elif Meanu == "2":
        result = ""
        for e in rollDice(5):
            result += F"{e} (Sum: {getSum(e)})\n"
        return result
    
    elif Meanu == "3":
        result = ""
        for e in rollDice(input("How many rolls would you like: ")):
            result += F"{e} (Sum: {getSum(e)})\n"
        return result
    
    elif Meanu == "4":
        result = ""
        count = 0
        while True:
            count += 1
            D = rollDice(1)[0]
            result += F"{D} (Sum: {getSum(D)})\n"
            if getSum(D) == 2:
                result += F"SNAKE EYES! It took {count} rolls to get snake eyes."
                return result
    
            
            
def main():
    
    while True:
        print("Dice Roll Simulator Menu\n")
        print("1. Roll Dice Once\n2. Roll Dice 5 Times\n3. Roll Dice ‘n’ Times\n4. Roll Dice until Snake Eyes\n5. Exit\n")
        Meanu = input("Select an option (1-5): ")
        if Meanu != "5":
            print(Action(Meanu))
        else:
            print("Thanks for playing\n")
            return


main()