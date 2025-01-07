class Bank:
    def __init__(self):
        self.minimum = 100
        self.balance = 1000
    def get_balance(self):
        return self.balance
    def withdraw(self, amount):
        if amount < self.minimum:
            print('No money for you')  # ন্যূনতম সীমার সতর্কবার্তা
        elif amount > self.balance:
            print('You are broke! no money!')  # ব্যালেন্সের সীমার সতর্কবার্তা
        else:
            self.balance = self.balance - amount
            return amount
            
# আবার টেস্টিং:
my_bank = Bank()
my_bank.withdraw(100)  # ১০০ টাকা তুললো
print("Balance:", my_bank.get_balance())  # ব্যালেন্স: ৯০০ টাকা

my_bank.withdraw(1250)  # ব্যালেন্সের চেয়ে বেশি টাকা তুলতে চাইল
print("Balance:", my_bank.get_balance())  # ব্যালেন্স অপরিবর্তিত: ৯০০ টাকা
