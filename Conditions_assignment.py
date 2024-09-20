print("WE have\n1. Coke---400\n2. Fanta---350\n3. Sprite---300\n4. Pepsi---400\n")
coke=400
fanta=350
sprite=300
pepsi=400
while True:
    drink=input("What drink do you want? ").title()
    if drink=='Coke' or drink== "1" :
        coke_options=['sugar free','zero coke']
        print(coke_options)
        option=input("What type of coke? ").lower()
        qty=int(input("How many are you buying? "))
        if option in coke_options :
            print(f'Here is your {option} coke.')
        else:
            print('Here is your original coke')
        balance=coke*qty
        print(f'Your balance is {balance}')    
        
    elif drink=='Fanta' or drink== "2" :
        fanta_options=['Orange','Pineapple']
        print(fanta_options)
        option=input("What type of fanta? ").title()
        qty=int(input("How many are you buying? "))
        if option in fanta_options :
            print(f'Here is your {option} fanta.')
        else:
            print('Here is your original fanta')
        balance=fanta*qty
        print(f'Your balance is {balance}')    
        
    elif drink=='Sprite' or drink== "3" :
        sprite_options=['Sprite1','Sprite2']
        print(sprite_options)
        option2=input("What type of sprite? ").title()
        qty=int(input("How many are you buying? "))
        if option2 in sprite_options :
            print(f'Here is your {option2} sprite.')
        else:
            print('Here is your original sprite')
        balance=sprite*qty
        print(f'Your balance is {balance}')        
        
    elif drink=='Pepsi' or drink== "4" :
        pepsi_options=['normal','zero sugar']
        print(pepsi_options)
        option3=input("What type of pepsi? ").lower()
        qty=int(input("How many are you buying? "))
        if option3 in pepsi_options :
            print(f'Here is your {option3} pepsi.')
        else:
            print('Here is your original pepsi')
        balance=pepsi*qty
        print(f'Your balance is {balance}')        
    else:
        print('Sorry we do not have your request.')
        continue
    break
    
print("Payment Type\n1. Cash Payment\n2. Bank Payment")
while True:
    response = input("Response: ").lower()
    if response == "cash" or response == "1":
        pay= int(input("How much do you have? "))
        while pay < balance:
            for i in range(1):
                print("Insufficient funds")
                pay= int(input("How much do you have? "))
            boolean =input("Do you want to continue? ").title
            if boolean == "No" or boolean =="0":
                print("Sorry we can't give you what you want.")
                break
            elif pay < balance:
                continue
            break
        change = pay - balance
        print(f"Your balance is {change}")
    elif response == "bank" or response == "2":
        print(f"We have deducted {balance} from your account")
    else:
        print("Invalid request")     
        continue
    break   