import csv
from datetime import date
from pathlib import Path


class bankManager(object):
    def __init__(self):
        path = Path('./accountactivity.csv')
        if not path.is_file():
            with open('accountactivity.csv', 'w') as csv_file:
                fieldnames = ['Account', 'Type', 'Amount', 'Date']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                self.accountactivity = []
        else:
            self.accountactivity = self.file_read()

    def ask_wants(self):
        print('What do you want? 1:Check Deposit, 2:Deposit/Withdraw')
        want = input()
        if want != '1' and want != '2':
            return self.ask_wants()
        elif want == '1':
            return want
        elif want == '2':
            return want

    def show_deposit(self, account):
        total_deposit = 0
        for row in self.accountactivity:
            if row[0] == account and row[1] == 'Deposit':
                total_deposit += int(row[2])
            elif row[0] == account and row[1] == 'Withdraw':
                total_deposit -= int(row[2])
        print("{}'s Deposit:{}".format(account, total_deposit))

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

    def confirm_registration(self, list):
        print("I'll register this activity below.")
        print("=====ACCOUNT ACTIVITY INFORMATION=====")
        print('ACCOUNT: ', list[0])
        print('ACTIVITY: ', list[1])
        print('AMOUNT: ', list[2])
        print("======================================")
        print("1:OK, 2:Cancel")
        confirmation = input()
        if confirmation != '1' and confirmation != '2':
            return self.confirm_registration(list)
        else:
            return confirmation

    def file_read(self):
        with open('accountactivity.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            list = []
            for row in reader:
                list.append([row['Account'],
                            row['Type'],
                            int(row['Amount']),
                            row['Date']])
        return list

    def file_write(self, list):
        self.accountactivity.append(list)
        with open('./accountactivity.csv', 'a') as csv_file:
            fieldnames = ['Account', 'Type', 'Amount', 'Date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Account': list[0],
                            'Type': list[1],
                             'Amount': list[2],
                             'Date': date.today()})

    def say_goodbye(self):
        print('Thanks! Good bye!')


if __name__ == '__main__':
    mymanager = bankManager()
    while True:
        process = mymanager.ask_wants()
        if process == '1':
            the_account = mymanager.ask_account()
            mymanager.show_deposit(the_account)
            continue
        elif process == '2':
            the_account = mymanager.ask_account()
            the_activity = mymanager.ask_activity()
            the_amount = mymanager.ask_amount()
            the_activity_inf = [the_account, the_activity, the_amount]
            confirmation = mymanager.confirm_registration(the_activity_inf)
            if confirmation == '1':
                mymanager.file_write(the_activity_inf)
            elif confirmation == '2':
                mymanager.say_goodbye()
            continue
