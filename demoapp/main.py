import csv
from pathlib import Path

class Roboko(object):
    def __init__(self, name):
        self.name = name
        self.list = []
        path = Path('./restaurant_list.csv')
        if not path.is_file():
            with open('restaurant_list.csv', 'w') as csv_file:
                fieldnames = ['Name','Count']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        else:
            self.list = self.file_read()

    def say_hello(self):
        print('Hello! I\'m {}. May I ask your name?'.format(self.name))
        username = input().capitalize()
        if username == '':
            return self.say_hello()
        else:
            return username

    def recommend(self, username):
        list = self.list
        if len(list) == 0:
            print('{}-san, which restaurant do you like?'.format(username))
            user_recommend = input()
            if user_recommend == '':
                return self.recommend(username)
            list = [[user_recommend, 1]]
            self.file_write(list)
        elif len(list) == 1:
            print('{}-san, my recommendation is {}. Do you like that? yes or no'.format(username, list[0][0]))
            ans = input().capitalize()
            if ans == 'Yes':
                list[0][1] = list[0][1] + 1
                self.file_write(list)
            else:
                print('{}-san, which restaurant do you like?'.format(username))
                user_recommend = input()
                if user_recommend == '':
                    return self.recommend(username)
                else:
                    for f in list:
                        flag = 0
                        if user_recommend == f[0]:
                            f[1] = f[1] + 1
                            flag = 1
                    if flag == 0:
                        list.append([user_recommend, 1])
                self.file_write(list)
        else:
            max_value = 0
            for i in 0,len(list)-2:
                print(i)
                if list[i][1] > list[i+1][1]:
                    max_value = list[i][1]
                elif list[i][1] < list[i+1][1]:
                    max_value = list[i+1][1]
                elif list[i][1] == list[i+1][1]:
                    max_value = list[i][1]
            for f in list:
                if max_value == f[1]:
                    recommend_restaurant = f[0]
            print('{}-san, my recommendation is {}. Do you like that? yes or no'.format(username, recommend_restaurant))
            ans = input().capitalize()
            if ans == 'Yes':
                for f in list:
                  if recommend_restaurant == f[0]:
                    f[1] = f[1] + 1
                self.file_write(list)
            else:
                print('{}-san, which restaurant do you like?'.format(username))
                user_recommend = input()
                if user_recommend == '':
                    return self.recommend(username)
                else:
                    for f in list:
                        flag = 0
                        if user_recommend == f[0]:
                            f[1] = f[1] + 1
                            flag = 1
                    if flag == 0:
                        list.append([user_recommend, 1])
                self.file_write(list)
        

    def file_read(self):
        with open('restaurant_list.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            list = []
            for row in reader:
                list.append([row['Name'], int(row['Count'])])
        return list


    def file_write(self, list):
        with open('./restaurant_list.csv', 'r+') as csv_file:
            csv_file.truncate(0)
        with open('./restaurant_list.csv', 'w') as csv_file:
            fieldnames = ['Name','Count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in list:
                writer.writerow({'Name': row[0], 'Count': row[1]})

    def say_goodbye(self):
        print('Thanks! Good bye!')

roboko = Roboko('Hanako')
print(roboko.list)
username = roboko.say_hello()
roboko.recommend(username)
roboko.say_goodbye()
