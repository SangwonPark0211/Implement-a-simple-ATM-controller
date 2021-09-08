import sys
class ATM:
    def __init__(self, iscard = 0):
        # check if customer insert card
        self.card = iscard
        self.customer = {"00" : {'1' : 50, '2' : 100}, "01" : {'3' : 99, '4' : 0}, "10" : {'5' : 5}, "11" : {'6' : 27}}

    def insertCard(self):
        if not self.card:
            print("Banking service is finished because you didn't insert card.")
            sys.exit()

    def enterPIN(self):
        print("Please enter your PIN number.")
        pin_num = input()
        if pin_num not in self.customer:
            print("You are not registered to our banking system.")
            sys.exit()
        elif pin_num in self.customer:
            print("We have found your account information.")

    def selectAccount(self):
        print("Please select account")
        pin = input()
        print("These are accounts that you have.")
        for acc_name in self.customer[pin]:
            for k in self.customer[pin][acc_name]:
                print(f"Account name : {k}")
        print("Please select account and enter the name of account to see balance or deposit or withdraw.")
        selected_acc = input()
        return pin, selected_acc

    def seeBalance(self, pin, selected_acc):
        print(f"Youre {selected_acc} account's balance is {self.customer[pin][selected_acc]}$")

    def deposit(self, pin, selected_acc):
        print("Please enter the amount that you want to deposit.")
        deposit_amount = int(input())
        print(f"Balance before deposit : {self.customer[pin][selected_acc]}    Balance after deposit : {self.customer[pin][selected_acc]+deposit_amount}")
        print("Would you like to deposit?(y/n)")
        deposit_answer = input()
        if deposit_answer == 'y':
            print("Deposit has been completed.")
        elif deposit_answer == 'n':
            print("Deposit has been canceled.")

    def withdraw(self, pin, selected_acc):
        print("Please enter the amount that you want to withdraw.")
        withdraw_amount = int(input())
        if withdraw_amount > self.customer[pin][selected_acc]:
            print("You've entered withdrawal amount more than balance.")
            sys.exit()
        else:
            print(f"Balance before withdrawal : {self.customer[pin][selected_acc]}    Balance after withdrawal : {self.customer[pin][selected_acc]-withdraw_amount}")
            print("Would you like to withdraw?(y/n)")
            withdraw_answer = input()
            if withdraw_answer == 'y':
                print("Withdrawal has been completed.")
            elif withdraw_answer == 'n':
                print("Withdrawal has been canceled.")