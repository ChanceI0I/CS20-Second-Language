# Create A Quiz


# Answer Checking
def check(UserAnswer, *CorrectAnswer):
    global score
    for a in CorrectAnswer:
        if UserAnswer.lower() == a:
            score += 1
            return "Correct!"
    return F"Incorrect. The correct answer should be \"{CorrectAnswer[0]}\"."


# Giving feedback
def feedback():
    percentage = score/fullScore
    if percentage == 1:
        return "Terrific !!"
    elif percentage >= 0.8:
        return "Almost There !!"
    elif percentage >= 0.5:
        return "Well Done !!"
    elif percentage >= 0.2:
        return "You Can Do It !!"
    else:
        return "Don't Give Up !!"


def main():

    print("Welcome to Earth quiz !")

    print("\n1. What is the largest ocean on Earth?")
    print(check(input("Enter your answer: "), "the pacific ocean", "pacific ocean"))

    print("\n2. How many time zones does the Earth have?")
    print(check(input("Enter your answer: "), "24", "twenty-four"))

    print("\n3. What are the most common gases in Earth's atmosphere?")
    print(check(input("Enter your answer: "), "nitrogen"))

    print("\n4. What is the longest river in the world?")
    print(check(input("Enter your answer: "), "nile river"))

    print("\n5. What is the biggest island in the world?")
    print(check(input("Enter your answer: "), "greenland"))

    print("\n6. What is one of the most populous city in the world?")
    print(check(input("Enter your answer: "), "tokyo", "delhi", "shanhai", "beijing", "ciro", "vancouver", "new york", "new-york"))

    print("\n7. What is the tallest mammal on Earth?")
    print(check(input("Enter your answer: "), "giraffe"))

    print(F"\n\nYour Results: \n{score} / {fullScore} ({(score / fullScore) * 100}%) \n{feedback()}")


score = 0
fullScore = 7
main()

