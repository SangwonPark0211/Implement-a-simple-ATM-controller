# Implement-a-simple-ATM-controller

## Description
This repository is implementation of a simple ATM controller. It contains basic functions like <b>inserting card</b>, <b>entering PIN</b>, <b>Selecting accounts, Seeing balance</b>, <b>Deposit</b>, and <b>Withdrawal</b>.
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
I made an example data in ATM class for test implementation. There are 4 customers and their PIN are 00, 01, 10, 11. For example, customer with PIN 00 has 2 accounts. Account names are 1, 2 with balance 50$, 100$ repectively. And customer with PIN 11 has only 1 accounts. Account name is 6 with balance 27$.
</br></br>

## Usage
1. Run test.py file with command "python test.py"
2. It will require you to <b>insert card.</b> (Entering 1 means inserting card for convenience. Entering others means not inserting card so banking service will be finished.)
3. Enter <b>PIN.</b>
4. Select account and <b>enter the name of account</b>
5. Select the <b>task</b> that you want to do(Deposit, Withdrawal)
</br>

## Corner cases
There can be some exceptional cases.
1. A customer <b>didn't insert card.</b>
2. A customer enter PIN that are <b>not registered</b> for the bank.
3. A customer enter account name which he or she <b>doesn't have.</b>
4. A customer enter withrawal amount <b>more than the balance</b> he or she has.

<b>For case 1)</b> If you enter anything except 1 when you asked ""Please insert card.(Entering 1 : insert card, others : not insert card)", the program will tell you ""Banking service is finished because you didn't insert card." and the banking service will be finished.</br></br>
<b>For case 2)</b> You can enter PIN that are not in banking DB such as 54548 when you asked "Please enter your PIN number". Then, the program will tell you "You are not registered to our banking system" and the banking service will be finished.</br></br>
<b>For case 3)</b> If you enter account name that you don't have when you asked ""Please select account and enter the account's name to deposit or withdraw." Then, the program will tell you "You don't have account with that account's name." and the banking service will be finished.</br></br>
<b>For case 4)</b> If you enter withdrawal amount more than the balance you have when you asked "Please enter the amount that you want to withdraw. Ex)10000", the program will tell you "You've entered withdrawal amount more than balance." and the banking service will be finished.