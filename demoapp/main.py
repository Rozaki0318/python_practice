import csv

class Roboko(object):
    def __init__(self, name):
        self.name = name
        print('{} has been created!'.format(self.name))
        
    def ask_name(self):
        word = "Hello! May I ask your name?\n"
        print('=' * len(word) + '\n' + word + '=' * len(word) + '\n')
        ans = input()
        return ans
    
    def ask_restaurant(self, username):
        print('===========================\n{}-san, Which restaurant do you like?\n==========================='.format(username))
        return input()



 #   with open('restaurant.csv', 'w') as csv_file:
 #     fieldnames = ['Name','Count']
 #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 #    writer.writeheader()
 #     writer.writerow({'Name': ans, 'Count': '1'})

roboko = Roboko('Hanako')
username = roboko.ask_name()
restaurant = roboko.ask_restaurant(username)
print(username, restaurant)
