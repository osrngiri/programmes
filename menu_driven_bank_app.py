"""
Below is a menu driven program to simulate banking transactions.
There are basic functions create account, deposit amount, withdraw amount and show balance
"""
#Import required libraries
import random
import os
from datetime import date
from rich.table import Table #rich library is used to display account details in well formatted table
from rich.console import Console
def create_account(cust_name,init_amount):
"""
This function creates account and writes details to a file. It prompts customer name and initial amount and account number is generated
automatically and records date of transaction. If amount is less than or equal to zero then a message will be displayed.This function
checks if file exists then details are appended to file
"""
    if int(init_amount) <= 0:
        print('You need initial amount to open account...')
    if os.path.exists("account_details.csv"):
        with open('account_details.csv', 'a') as afile:
            account_num = random.randint(1111, 9999)
            afile.write(str(account_num) + ',' + cust_name.upper() + ',' + str(init_amount) + ',' + str(date.today())+"\n")
    else:
        with open('account_details.csv','w') as afile:
            account_num = random.randint(1111, 9999)
            afile.write(str(account_num) + ',' + cust_name.upper() + ',' + str(init_amount) + ',' + str(date.today())+"\n")

def display_balance():
"""
This function uses rich library to display results in formatted manner
"""
    with open('account_details.csv','r') as a2file:
        console = Console()
        table = Table(title="BANGALURU BANK LIMITED, BANGALORE")
        table.add_column("ACCOUNT NO", justify="right", style="cyan", no_wrap=True)
        table.add_column("CUSTOMER NAME", style="magenta",no_wrap=True)
        table.add_column("AMOUNT", justify="right", style="green")
        table.add_column("DEPOSIT DATE", justify="right", style="green")
        file_op = a2file.readlines()
        for r in file_op:
            n_accno,n_cname,n_amt,n_date = r.split(',')
            table.add_row(n_accno,n_cname, n_amt,n_date)
        console.print(table)

def deposit_amount(acc_no,amount):
"""
This function accepts acc number and amount to be deposited and reads details from file, converts into a dictionary, updates amounts.
Writes back value part of dictionary to file
"""
    if int(amount) <= 0:
        print('Amount deposited must be greater than 0')
    else:
        with open('account_details.csv', 'r') as rfile:
           d = {index:value for index,value in enumerate(rfile.readlines())}
           l = []
           for k,v in d.items():
               l = v.split(',')
               if str(acc_no) in l[0]:
                   new_amt = int(l[2]) + int(amount)
                   l[2] = str(new_amt)
                   d[k] = (','.join(l))
        with open('account_details.csv', 'w') as wfile:
            for k1,v1 in d.items():
                wfile.write(v1)
        display_balance()

def withdraw_amount(acc_no,amount):
"""
This similar to deposit functions.
"""
    if int(amount) <= 0:
        print('Amount deposited must be greater than 0')
    else:
        with open('account_details.csv', 'r') as rfile:
            d = {index: value for index, value in enumerate(rfile.readlines())}
            l = []
            for k, v in d.items():
                l = v.split(',')
                if str(acc_no) in l[0]:
                    if int(l[2]) <= int(amount):
                        print('Not enough balance in account...')
                    else:
                        new_amt = int(l[2]) - int(amount)
                        l[2] = str(new_amt)
                        d[k] = (','.join(l))
        with open('account_details.csv', 'w') as wfile:
            for k1, v1 in d.items():
                wfile.write(v1)
        display_balance()


print('1.Enter 1 to Create Account' )
print('2.Enter 2 to Deposit Account')
print('3.Enter 3 to Withdraw Amount')
print('4.Enter 4 to Display Account Details')
input1 = int(input("Enter your choice:"))

if input1 == 1:
    while True:
        w_name = input('Enter Customer Name:')
        w_amt  = input('Enter initial amount:')
        create_account(w_name, w_amt)
        w_cont = input('Enter q to quit, c to continue')
        if w_cont == 'q':
            display_balance()
            break
elif input1 == 2:
        z_accno = input('Enter account number:')
        z_amt = input('Enter amount to deposit:')
        deposit_amount(z_accno, z_amt)
elif input1 == 3:
        x_accno = input('Enter account number:')
        x_amt = input('Enter amount to withdraw:')
        withdraw_amount(x_accno, x_amt)
else:
        display_balance()