def greet_user(name):
    name= input(f"Hello, {name}")
    return name
# print(greet_user("Kamsi"))

def calculate_area(length, width):
    rectangle = int(input(length * width))
    return rectangle
area = calculate_area(4, 4)
print(area)