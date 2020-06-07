store={'hats':2500,'t-shirts':5000,'shorts':3000,'sun glases':10000,'ear rings':1500,'socks':700,'bracelets':15000,'bangles':7000,'anklet':2500,'sweat pants':8000}
print('What is your name')
name=str(input())
print('Enter lastname')
lastname=str(input())
print('Are you male or female')
gender=str(input())
print('Enter cellphone number')
cellphone=str(input())
print('How old are you')
age=int(input())
ans=""
for i in name:
    ans=ans+i
    if i==" ":
        break
while True:
    if age>18:
        print("Welcome to Collins' fashion store {}".format(ans))
        for k,v in store.items():
            print(k.ljust(20,'-')+" "+ '{}'.format(str(v).rjust(6)))
        print('Select an item to buy')
        total=0
        while True:
            choice=str(input())
            if choice in store.keys():
                for k,v in store.items():
                    if k==choice:
                        print(k,v)
                        total=total+v
            elif choice=="":
                break
            elif choice not in store.keys():
                print('the item you selected is not in stock ')
                break
        print('The total cost of your purchase is {}'.format(total))
        print("Thank you for purchasing from Collins' fashion store {}".format(lastname))
    else:
        print("We are sorry to announce to you that you do not meet up with the age requirements to purchase from our store")
    break