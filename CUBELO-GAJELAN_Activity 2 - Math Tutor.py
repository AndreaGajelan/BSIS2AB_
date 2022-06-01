import random
import os

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtrct(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def dividiby(x, y):
    return x / y

while True:
    
    os.system("cls")
    
    print("-----  MATH TUTOR  -----\n\n")
    print("[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\n")
    
    # Asking the user to choose an operation and how many problems they want to do.
    choice = input("Choose operation: ")
    problemNum = int(input("How many problems?: "))
    i = 0
    score = 0
    if choice in ('1', '2', '3', '4'):

        # ADDITION OPERATION
        if choice == '1': 
            print("\n")
            # while loop to limit the number of questions based on the problems inputed by the user.
            while i < problemNum:
                # Generating two random numbers and adding them together.
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                
               # Asking the user to input an answer to the question.
                print("What is the sum of " + str(num1) + " and " + str(num2) + "?")
                answer = float(input("Answer: "))
                if num3 == answer:
                    print("Correct\n")
                    # Increment on score variable of the user.
                    score += 1
                else:
                    # Printing the correct answer.
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                # Increment on i variable for the while loop.
                i += 1
            # Printing the score of the user.
            print("Score: " + str(score) + "/" + str(problemNum))
            

        # SUBTRACTION OPERATION
        elif choice == '2': 
            print("\n")
            while i < problemNum:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtrct(num1, num2)

                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct\n")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                i += 1
            print("Score: " + str(score) + "/" + str(problemNum))
           
        
        # MULTIPLICATION OPERATION
        elif choice == '3': 
            print("\n")
            while i < problemNum:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)

                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct\n")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                i += 1
            print("Score: " + str(score) + "/" + str(problemNum))
           
        
        # DIVISION OPERATION
        elif choice == '4': 
            print("\n")
            while i < problemNum:
                num1 = round(float(random.randint(0, 9)),2)
                num2 = round(float(random.randrange(2, 10, 2)), 2)
                num3 = dividiby(num1, num2)

                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct\n")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                i += 1
            print("Score: " + str(score) + "/" + str(problemNum))
            

        # Check if the user wants another round
        # Break the while loop if answer is no
        try_again = input("Want to try again? (yes/no): ")
        if try_again == "no":
           print("--End of Math Tutor. Thank you!--\n")
           break

    else: 
        print("Invalid Input.")