def grading_system():
    no= int(input("Score: "))
    if no in range(90, 101):
        print("You have an A")
    elif no in range(80, 90):
        print("You have a B")
    elif no in range(70, 80):
        print("You have a C")
    elif no in range(60, 70):
        print("You have a D")
    else:
        print("You failed this course")   
    return no

# print(grading_system())
grade = grading_system
# print(grade)

def checker(num):
    if num % 2 == 0 :
        return "This number is even"
    else :
        return "This number is odd"

# print(checker(56))
# response = int(input("Type a number: "))
# check = checker(response)
# print(check)


def Names(name):
    return name
question = input("What is your name? ")

print(Names(question))