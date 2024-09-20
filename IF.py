# print("Welcome to DFI")
# response = (input("Would you like to register for a course\nYes or No\n")).lower()
# if response =="yes":
#     Firstname =str(input("Input Firstname: ")).title()
#     Lastname = str(input("Input Lastname: ")).title()
#     gender = str(input("Male or Female: ")).title()
#     if gender == "Male":
#         print(f"Welcome Mr.{Firstname} {Lastname}")
#     elif gender == "Female":
#         print(f"Welcome Mrs.{Firstname} {Lastname}")
#     else:
#         print("Invalid Input")
#     age = str(input("How old are you? "))
#     phone_no =str(input("Input your phone number. "))
#     payment = str(input("How much did you pay? "))
#     print(f"Rregistration Successful.\nThank you for coming {Firstname} {Lastname}.\nThank you for choosing us.")
# elif response == "no":
#     alter = input("Type 'Yes' if you want to be shown round th place: ").title()
#     if alter == "Yes":
#         print("We would love to show you around")
#     else:
#         print("Thank you for coming")

courses ={"1":"Python for beginners","2" :"Data Analyst"}
response =input("pick a course")
if response in courses:
    print(courses["1"])