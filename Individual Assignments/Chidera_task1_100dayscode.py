class Store:
	
	def __init__(self,fullname,age,gender, phone):
		self.fullname = fullname
		self.age = age
		self.gender = gender
		self.phone = phone
		self.first,self.last = self.fullname.split()
		
		if self.age >= 18:
			print("Welcome to 100codes boutique, your one stop shop for quality clothing's")
		else:
			print("Sorry there are no clothes for your age range please check back with us when you are 18 or older")
			exit()
			
		self.products = {"aba stylish shoe ":150000,"aba vintage shirt":12000,"versace handbag":50000,"versace shoe":100000,"fendi jean trouser":10000,"gucci stilleto":45000,"gucci bag":70000,"aba bag":90000,"dior perfume":15000,"montblanc watch":20000}
	
	def current_goods_choice(self):
		
		print("This are the awesome good carefully selected for your glamorous look")
		for i in self.products.items():
			print(i)
		self.choices= []	
		while True:
			choice = input("Make your choice, choose a product now or enter 'exit' to quit: ")
			if choice.lower() == "exit":
				break
			elif choice.lower() not in self.products.keys():
				print("Sorry your choice product is not in stock currently,\
			Checkout other goods above")
				continue
			else:
				print(f"The cost of {choice} is #{self.products[choice]}")
				self.choices.append(choice)
				
	def display_info(self):
		total = 0
		print("This were the goods you ordered:")
		print(",".join(self.choices))
		for x in self.choices:
			total += self.products[x]
			
		print(f"The total cost of goods purchased = {total}")
		print(f"Goodbye! {self.last} hope you had a wonderful time at our store")
		
		
if __name__ == "__main__":
	fullname = input("Enter your fullname (firstname lastname):  ")
	age = int(input("Enter your age example '22': "))
	gender = input("Enter your gender m/f : ")
	phone = input("Enter your phone number: ")
	
	shop = Store(fullname,age,gender, phone)
	shop.current_goods_choice()
	shop.display_info()
		
			