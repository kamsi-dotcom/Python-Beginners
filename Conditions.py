x=7
y=7

#Condition
# if x<y:
#     print('x is less than y')
# elif x>y:
#     print('x is greater than y')    
# else: 
#     print('x is equal to y')    

# if x<y or x>y:
#     print('x is not equal to y')
# else: 
#     print('x is equal to y')    
coke=400
fanta=350
sprite=300
pepsi=400

print("we have\n1. Coke\n2. Fanta\n3. Sprite\n4. Pepsi\n")
drinks=input('What do you want?').title()
if drinks== 'Coke' or drinks=='1':
    qty=int(input("How many are you buying?"))
    option=input("Enter 'free' for sugar free:").lower
    if option=='free':
        print('Here is your sugar free coke')
    else:
        print('Here is your original coke')
elif drinks== 'Fanta' or drinks=='2':
    print('Here is your fanta')
elif drinks== 'Sprite' or drinks=='3':
    print('Here is your sprite')   
elif drinks== 'Pepsi' or drinks=='4':
    print('Here is your sprite')         
else:
    print("Sorry we don't have your request.")    