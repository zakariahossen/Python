# ক্লাসের মধ্যে এনক্যাপসুলেশন ব্যবহার
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # এনক্যাপসুলেটেড তথ্য
        self.__balance = balance                # এনক্যাপসুলেটেড তথ্য

    # getter for account_number
    def get_account_number(self):
        return self.__account_number

    # setter for balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Amount cannot be negative.")

    # method to check balance
    def check_balance(self):
        print(f"Account Balance: {self.__balance}")

# অবজেক্ট তৈরি
account = BankAccount('123456789', 1000)
print("Account Number:", account.get_account_number())  # getter ব্যবহার

account.set_balance(1500)  # setter ব্যবহার করে ব্যালেন্স আপডেট
account.check_balance()    # ব্যালেন্স দেখানো হচ্ছে
