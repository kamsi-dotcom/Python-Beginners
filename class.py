# def calc(no1, no2):
#     calculate = ["add","subtract","multiply","divide"]
#     club=input("what do you want to do? ")
#     while True:
#         if club in calculate :
#             club == "add" 
#             balance = no1 + no2
#             return balance
#         elif club == "subtract" :
#             balance1 = no1 - no2
#             return balance1
#         elif club in calculate :
#             club == "multiply" 
#             balance2 = no1 * no2
#             return balance2  
#         elif club in calculate :
#             club == "divide" 
#             balance3 = no1 / no2
#             return balance3
#         else:
#             print("Invalid Operator")
#             break




# while True:
#     number1= int(input("what is your number? "))
#     operator = input("Enter +-/x \n")
#     number2= int(input("what is your number? "))
#     # print(calc(number1,number2))
#     if operator == "+":
#         print(f"{number1} + {number2} = {number1 + number2}")
#     elif operator == "-":
#         print(f"{number1} - {number2} = {number1 - number2}")
#     elif operator == "x":
#         print(f"{number1} x {number2} = {number1 * number2}")
#     elif operator == "/":
#         print(f"{number1} / {number2} = {number1 / number2}")
#     else:
#         print("Invalid Operator")
#         break



def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y ==0:
        return "Error! Division by zero."
    else:
        return x / y
    
# def calculator():
#     print('Welcome to our simple calculator')
#     print('select an operator')
#     print('1. Add')
#     print('2. Subtract')
#     print('3. Multiply ')
#     print('4. Divide')
    
#     choice = input("1/2/3/4\n")
#     num1= int(input("Enter your first number? "))
#     num2= int(input("Enter your second number? "))

#     while True:
#         if choice == "1":
#             print("Result:", add(num1, num2))
#         elif choice =="2":
#             print("Result:", subtract(num1, num2))
#         elif choice =="3":
#             print("Result:", multiply(num1, num2))
#         elif choice == "4":
#             print("Result:", divide(num1, num2))
#         else:
#             print("Invalid Operation")
#             continue
#         break
        
# calculator()

# bring out words that start with "T"
words = ["Training", 'Digital', "Fortress","tech","Transport","telephone"]
# if "Fortress" in words:
#     print('Yes')
# else:
#     print("No")

# for word in words:
#     if word[0]=="t" or word[0]== "T":
#         print(word)

# for word in words:
#     if word.startswith("t") or word.startswith("T"):
        # print(word)
        
item = [10,20, ["mango", "blue",[100, "class"],["people",[365]]],40, 50,["Fortress"], "Digital", ["Akowonjo"],"Egbeda",["Tech"]]
# print(item[6])
# print(item[2][2][1])

word =[
    {
        "name":"Emeka",
        "email": 'emeka@yahoo.com',
        "state":'Osun',
        'Occupation': "Full Stack"
    },
      {
        "name": "Titi",
        "email": "titi@yahoo.com",
        "state": "Osun",
        "occupation":"Python Developer"
    },
      {
        "name": "Glory",
        "email": "glory@yahoo.com",
        "state": ["Delta","Kogi","Abia","Benin"],
        "occupation":"Frontend"
      },
        {"name": "Toke",
          "email": "toke@yahoo.com",
          "state": "FCT",
          "occupation":"UI-UX"
    }
]

# print(word[3]["name"])
print(word[2]["state"][2])
# for i in word:
    # print(i["name"])