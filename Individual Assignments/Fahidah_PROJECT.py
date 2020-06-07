#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Fashion Store

products = {"Shirts": [300, 6], "Trousers": [500, 3],
            "Body Cream": [250, 7], "Jewelries": [400, 5],
            "Ladies Shoes": [700, 3], "Sunglasses": [600, 2],
            "Leather Belt": [450, 0], "Make Up kit": [1300,4],
            "Handbags": [900, 6], "Perfume": [1000, 2]}


# In[2]:


# User data

print("Please provide your details below!")

f_name = input("First name: ").upper()
l_name = input("Last name: ").upper()
age = int(input("Age: "))
phone = input("Telephone number: ")
print()


# In[3]:


count = 1
item_count = 0


if age < 18:
    print(f"Hi {f_name}, We are sorry you can't shop with us.")
    print("You need a guardian to come with you!!!")
else:
    print(f"Welcome {f_name},It is good to have you!")
    
    items = list(products.keys())
    
    
    print("Make you selection from the items display below:")
    print()
    print("S/N \t PRODUCTS \t PRICES \t QUANTITY")
    
    for i in list(products.values()):
        print(count, "\t", items[item_count], "\t", i[0], "\t\t", i[1])
        count += 1
        item_count += 1
        
    print()
    product = input("Product: ").title()
    qty = int(input("Quantity: "))
    
    
    if product in products:
        if (products[product][1] == 0):
            print("Sorry, the product is current not available!")
        elif (qty <= products[product][1]):
                total =  products[product][0] * qty
                print(f"Total Payable: {total}")
        else:
            print("We do not have up to that quantity!")
    else:
        print("No such Product!")
            


# In[4]:


print(f"THANK YOU FOR PATRONIZING US, {l_name}. \nWe hope to see you again soon!")

