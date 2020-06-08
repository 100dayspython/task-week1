full_name = input(" enter your full name: ")
age = int(input(" enter your age: "))
gender = input(" enter gender: ")
number = input(" enter phone number: ")
if age >= 18:
    print(full_name + " welcome to our boutique" )
else:
    print(" you must be 18 or above")
our_products = {"bags": 80, "shirts": 100, "shoes": 40, "trousers": 80, "belts": 20, "underwears": 75, "cap": 10, "wrist_watch": 55}
for key, values in our_products.items():
    print(key, values)
    total_cost = 0
    while True:
        a = input()
        if a.lower() in our_products:
            total_cost += our_products[a]
        elif a == 'quit':
            break
        else:
            print(' not available')

            
print(" thanks for patronising us")







