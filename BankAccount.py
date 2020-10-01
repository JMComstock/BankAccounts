class BankAccount:
	def __init__(self, int_rate, balance = 0):
		self.rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		return self
	
	def withdraw(self, amount):
		self.balance -= amount
		if self.balance < amount:
			print("Insufficient funds: Charging a $5 fee")
			self.balance -= 5
		return self

	def display_account_info(self):
		print(f"Balance: {self.balance}")
		return self
	
	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance * (self.rate)+self.balance
		return self
BankAccount1 = BankAccount(0.01, 1000)
BankAccount2 = BankAccount(0.01, 1000)

BankAccount1.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interest().display_account_info()

BankAccount2.deposit(1000).deposit(1000).withdraw(100).withdraw(200).withdraw(50).withdraw(50).yield_interest().display_account_info()