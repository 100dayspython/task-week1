def closing_msg(lname):
	print(f'\nPlease, pay to the cashier. \nThank you {lname} for shopping here!')
	
def display(products):
	for product, price in products.items():
		print(f'{product} ₦{price}')
		
def cart(temp_cart, products):
	cart = {}
	for i in temp_cart:
		cart.update({(str(temp_cart.count(i)) +' ' + i): (temp_cart.count(i) * products[i])})
	return cart
		
	
	
if __name__ == '__main__':
	products = {'Shirt': 2500, 'Belt': 1000, 'Socks': 300, 'Sunglass': 800, 'Sneaker': 5000, 'Boot': 4000, 'Earring': 500, 'Face Mask': 200, 'Glove': 500, 'Jeans': 3000}
	
	fullname = input('Enter Full name: ').split()
	age = int(input('Enter age: '))
	gender = input('Enter gender: ')
	p_number = input('Enter Telephone number: ')
	fname, lname = fullname[0], fullname[1]
	if age < 18:
		print("Sorry, we don't have clothes for minors yet")
	else:
		print(f'\n{fname}, Welcome to The John Fashion Store. \nSee all our products...\n')
		display(products)
		temp_cart = []
		print("\nType the name of the item to select it or press 'enter' to see cart. Thanks!")
		while True:
			a = input("Enter the name of the item to buy: ").title()
			if a in products:
				temp_cart.append(a)
			elif a == '':
				break
			else:
				print("Item not available for now")
		print(f'\n\nConfirm your cart.\n')
		cart = cart(temp_cart, products)
		display(cart)
		print(f'\nTotal cost of goods is ₦{sum(cart.values())}')
		closing_msg(lname)