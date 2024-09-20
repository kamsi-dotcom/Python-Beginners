response = str(input("Welcome to Digital Fortress,what would you like to do?\n1. Enroll\n2. Class\n3. Enquiry\n>>>")).title()
if response == "1" or response == "Enroll":
    print("Fill the form below to begin your registration process")
    first_name = str(input("Enter your firstname: ")).title()
    last_name = str(input("Enter your lastname: ")).title()
    email = str(input("Enter your email address: ")).lower()
    for t in email:
        if t == "@":
            print("Verified Email")
        else:
            print("Invalid Email")
    DoB = str(input("Enter your date of birth: "))
    address = str(input("Enter your house address: ")).title()
    phone_number =str(input("Enter your phone no.: "))
    password1 = str(input("Enter password: "))
    password2 = str(input("Confirm password: "))
    if password1 or password2 < 8:
        print("Length of password is to short")
        if  password1 != password2 :
            print("Invalid password")
            exit()
        else:
            print("Password Successful")
    courses = {"1":"Python For Beginners",
               "2":"Data Analysis",
               "3":"Frontend",
               "4":"UI-UX",}
    reply = str(input(f"This are the courses we offer\nPick the number to select a course\n{courses}\nWhat course do you want to register for? "))

    if reply in courses:
        print(f"{first_name} {last_name} have successfully registered for {courses[reply]}\nThank you for choosing us.")
    else:
        print('Sorry we do not offer this course yet.')
elif response == "2" or response =="Class":
    print("Please wait in the waiting room until you receive word from your teacher.\nEnsure you have your ID card on!!!")
elif response =="3" or response == "Enquiry":
   print("This is digital fortress we offer different tech related courses\nBelow is a list of the courses we offer")
   print("1.Python for beginners\n2.Data analytics\n3.Frontend\n4.UI-UX")
   reply =str(input("Would you like to know the price range for the courses\n'True or False'\n>>>")).title()
   if reply == "True":
       print("1.Python for beginners(3 months)        NGN200,000\n2.Data analytics(4 months)       NGN150,000\n3.Frontend(6 months)      NGN300,000\n4.UI-UX(4 months)     NGN600,000")
   else:
       print("Here is a flier that shows a comprehensive list of what we offer.")
       print("Thank you for coming.\nFor further enquires please call'081-222-444-56'")
