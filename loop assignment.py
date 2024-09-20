''' Task 1: Print the Elements of a List
- **For Loop:**
  - Write a program that iterates over a list of numbers and prints each number.
- **While Loop:**
  - Write the same program using a `while` loop instead of a `for` loop.'''
# CODE
numbers=[0,1,2,3,4,5,6]
for number in numbers :
  # print(number)
  ...
x=0
while x < len(numbers) :
  # print(numbers[x]) 
  # x = x + 1
  x += 1
  ...


''' Task 2: Sum of Numbers
- **For Loop:**
  - Write a program that calculates the sum of all numbers from 1 to 100 using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
sum = 0
for x in range(1,101):

  sum += x
  # sum = sum + x
# print(sum)

total = 0
k = 1
while k in range(1,101):
  total += k
  k += 1
# print(total)  
  
''' Task 3: Find the Factorial of a Number
- **For Loop:**
  - Write a program that calculates the factorial of a given number using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
number = 5
factorial = 1
for i in reversed(range(1, number + 1)):
  factorial *= i
# print(factorial)  

number = 5
factorial = 1
while number in reversed(range(1, number + 1)):
  factorial *= number
  number -= 1
# print(factorial)
  
  

''' Task 4: Multiplication Table
- **For Loop:**
  - Write a program that prints the multiplication table of a given number using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
# number = int(input("Number? "))
for i in range(1, 13):
  # print(f'{number} * {i} =={number * i}')
    pass

n = 1
while n <= 12:
    # print(f'{number} * {i} =={number * i}')
    n += 1
  


''' Task 5: Reverse a String
- **For Loop:**
  - Write a program that takes a string as input and prints the string in reverse order using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
words = "hello"
reversed_text = ""
for word in words:
    reversed_text = word + reversed_text
    # print(f"reversed text: {reversed_text}")
    
w = len(words) - 1
while w >= 0:
    reversed_text == words[w]
    w -= 1
print(f"reversed text: {reversed_text}")    

''' Task 6: FizzBuzz
- **For Loop:**
  - Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz" instead of
  the number, and for multiples of 5, print "Buzz." For numbers that are multiples of both
  3 and 5, print "FizzBuzz."
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE


''' Task 7: Guess the Number (Simple Game)
- **While Loop:**
  - Write a program that generates a random number between 1 and 20.
  Ask the user to guess the number and provide feedback if the guess is too high,
  too low, or correct. The loop should continue until the user guesses the correct number.'''
# CODE


