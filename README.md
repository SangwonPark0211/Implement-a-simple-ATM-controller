# Implement-a-simple-ATM-controller

## Description
This repository is implementation of a simple ATM controller. It contains basic functions like <b>inserting card</b>, <b>entering PIN</b>, <b>Seeing accounts and balance</b>, <b>Deposit</b>, <b>Withdrawal</b>.
</br></br>

## Download Repository
```
git clone https://github.com/SangwonPark0211/Implement-a-simple-ATM-controller.git
```
</br>

## Environment
```
python 3.X version is required
```
</br>

## Example data
```
self.customer = {"00" : {'1' : 50, '2' : 100}, "01" : {'3' : 99, '4' : 0}, "10" : {'5' : 5}, "11" : {'6' : 27}}
```
I made example data in ATM class for test implementation. There are 4 customers and their PIN is 00, 01, 10, 11. For example, customer with PIN 00 has 2 accounts. Their account names are 1, 2 with balance 50$, 100$ repectively. And customer with PIN 11 has only 1 accounts. Its account name is 6 with balance 27$.
</br>

## Usage
1. Run test.py file with command "python test.py"
2. It will require you to insert card. (Entering 1 means inserting card for convenience. Entering others means not inserting card so bancking service will be finished.)
3. Enter PIN.
4. Select account and enter the name of account
5. Select the task that you want to do(Deposit, Withdrawal)
</br>

## Corner cases
There can be some exceptional cases.
1. A customer didn't insert card.
2. A customer enter PIN that are not registered for the bank.
3. A customer enter account name which he or she doesn't have.
4. A customer enter withrawal amount more than the balance he or she has.

For case 1) If you enter anything except 1 when you asked ""Please insert card.(Entering 1 : insert card, others : not insert card)", the program will tell you ""Banking service is finished because you didn't insert card." and the banking service will be finished.</br>
For case2) You can enter PIN that are not in banking DB such as 54548 when you asked "Please enter your PIN number". Then, the program will tell you "You are not registered to our banking system" and the banking service will be finished.</br>
For case3) If you enter account name that you don't have when you asked ""Please select account and enter the account's name to deposit or withdraw." Then, the program will tell you "You don't have account with that account's name." and the banking service will be finished.</br>
For case4) If you enter withdrawal amount more than the balance you have when you asked "Please enter the amount that you want to withdraw. Ex)10000", the program will tell you "You've entered withdrawal amount more than balance." and the banking service will be finished.