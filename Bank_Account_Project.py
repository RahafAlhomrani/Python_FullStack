# Bank account
from datetime import datetime

formated_date = datetime.now().strftime('%A, %B, %Y')
formated_time = datetime.now().strftime('%I:%M %p')

class User_Account:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"A deposit of {amount} SAR has been made to your bank account on {formated_date} at {formated_time}")
            # call st_balance method
            self.set_balance()

    def get_balance(self):
        return print(f"Your current balance is: {self.__balance}")

    def set_balance(self):
        if self.__balance >= 0:
            return print(f"Your current balance is: {self.__balance}")
        else:
            print("Invalid balance amount")

    def withdrawal(self,amount):
        if self.__balance >0:
            self.__balance -= amount
            print(f"A withdrawal of {amount} SAR has been made to your bank account on {formated_date} at {formated_time}")
            #call st_balance method
            self.set_balance()


# object 1
user_1 = User_Account(0)
user_1.deposit(500)
user_1.withdrawal(100)
# object 2
user_2 = User_Account(0)
user_2.get_balance()
user_2.deposit(1000)
user_2.withdrawal(70)






