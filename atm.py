import sys
class ATM:
    def __init__(self):
        self.pin =  ""
        self.selected_acc = ""
        self.customer = {"00" : {'1' : 50, '2' : 100}, "01" : {'3' : 99, '4' : 0}, "10" : {'5' : 5}, "11" : {'6' : 27}}

    def insertCard(self):
        print("Please insert card.(Entering 1 : insert card, others : not insert card)")
        card = input()
        if card != '1':
            print("Banking service is finished because you didn't insert card.")
            sys.exit()

    def enterPIN(self):
        print("Please enter your PIN number.")
        self.pin = input()
        if self.pin not in self.customer:
            print("You are not registered to our banking system.")
            sys.exit()

    def selectAccount(self):
        print("These are accounts that you have.")
        for i,k in enumerate(self.customer[self.pin]):
            print(f"{i+1}. Account name:", k, "Balance:", self.customer[self.pin][k], "$")
        print("Please select account and enter the account's name to deposit or withdraw.")
        self.selected_acc = input()
        if self.selected_acc not in self.customer[self.pin]:
            print("You don't have account with that account's name.")
            sys.exit()

    def deposit(self):
        print("Please enter the amount that you want to deposit. Ex)50000")
        deposit_amount = int(input())
        print(f"Balance before deposit : {self.customer[self.pin][self.selected_acc]}    Balance after deposit : {self.customer[self.pin][self.selected_acc]+deposit_amount}")
        print("Would you like to deposit?(y/n)")
        deposit_answer = input()
        if deposit_answer == 'y':
            self.customer[self.pin][self.selected_acc] += deposit_amount
            print("Account name:", self.selected_acc, "Balance:", self.customer[self.pin][self.selected_acc],"$")
            print("Deposit has been completed.")
        elif deposit_answer == 'n':
            print("Deposit has been canceled.")

    def withdraw(self):
        print("Please enter the amount that you want to withdraw. Ex)10000")
        withdraw_amount = int(input())
        if withdraw_amount > self.customer[self.pin][self.selected_acc]:
            print("You've entered withdrawal amount more than balance.")
            sys.exit()
        else:
            print(f"Balance before withdrawal : {self.customer[self.pin][self.selected_acc]}    Balance after withdrawal : {self.customer[self.pin][self.selected_acc]-withdraw_amount}")
            print("Would you like to withdraw?(y/n)")
            withdraw_answer = input()
            if withdraw_answer == 'y':
                self.customer[self.pin][self.selected_acc] -= withdraw_amount
                print("Account name:", self.selected_acc, "Balance:", self.customer[self.pin][self.selected_acc],"$")
                print("Withdrawal has been completed.")
            elif withdraw_answer == 'n':
                print("Withdrawal has been canceled.")
    
    def main(self):
        self.insertCard()
        self.enterPIN()
        self.selectAccount()
        print("Please select the task that you want to do.")
        print("1. Deposit 2. Withdrawal")
        task = int(input())
        if task == 1:
            self.deposit()
        elif task == 2:
            self.withdraw()
