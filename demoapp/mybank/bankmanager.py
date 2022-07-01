import csv
from datetime import date
from pathlib import Path

class bankManager(object):
    def __init__(self):
        path = Path('./accountactivity.csv')
        if not path.is_file():
            with open('accountactivity.csv', 'w') as csv_file:
                fieldnames = ['Account','Type','Amount','Date']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        else:
            self.accountactivity = self.file_read()
            print(self.accountactivity)
    
    def ask_account(self):
        print('Which account? 1:Parents, 2:Seiya, 3:Kokone')
        account = input()
        if account != '1' and account != '2' and account != '3':
            return self.ask_account()
        elif account == '1':
            account = 'Parents'
        elif account == '2':
            account = 'Seiya'
        elif account == '3':
            account = 'Kokone'
        return account
         
    def ask_activity(self):
        print('Which activity? 1:Deposit, 2:Withdraw')
        activity = input()
        if activity != '1' and activity != '2':
            return self.ask_activity()
        elif activity == '1':
            activity = 'Deposit'
        elif activity == '2':
            activity = 'Withdraw'
        return activity
    
    def ask_amount(self):
        print('How much?')
        money = int(input())
        return money

    def confirm_registration(self, account, activity, amount):
        print("I'll register this activity below.")
        print("=====ACCOUNT ACTIVITY INFORMATION=====")
        print('ACCOUNT: ', account)
        print('ACTIVITY: ', activity)
        print('AMOUNT: ', amount)
        print("======================================")
        print("1:OK, 2:Cancel")
        confirmation = input()
        if confirmation != '1' and confirmation != '2':
            return self.confirm_registration(account, activity, amount)
        else:
            return confirmation

    def file_read(self):
        with open('accountactivity.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            list = []
            for row in reader:
                list.append([row['Account'], row['Type'], int(row['Amount']), row['Date']])
        return list

    def file_write(self, list):
        self.accountactivity.append(list)
        with open('./accountactivity.csv', 'r+') as csv_file:
            csv_file.truncate(0)
        with open('./accountactivity.csv', 'w') as csv_file:
            fieldnames = ['Account','Type','Amount','Date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.accountactivity:
                writer.writerow({'Account': row[0], 'Type': row[1], 'Amount': row[2], 'Date': date.today()})

    def say_goodbye(self):
        print('Thanks! Good bye!')    

if __name__ == '__main__':
    mymanager = bankManager()
    #confirmation = mymanager.confirm_registration(mymanager.ask_account(),mymanager.ask_activity(),mymanager.ask_amount())
    the_account = mymanager.ask_account()
    the_activity = mymanager.ask_activity()
    the_amount = mymanager.ask_amount()
    the_activity_inf = [the_account, the_activity, the_amount]
    confirmation = mymanager.confirm_registration(the_account,the_activity,the_amount)
    if confirmation == '1':
        mymanager.file_write(the_activity_inf)
    elif confirmation == '2':
        mymanager.say_goodbye()




