import csv
from pathlib import Path
import logging
import re

formatter = '%(asctime)s:%(levelname)s:%(message)s'
logging.basicConfig(filename='demoapp.log', level=logging.DEBUG, format=formatter)

class Roboko(object):
    def __init__(self, name):
        self.name = name
        self.csvfile = 'restaurant.csv'
        logging.debug('{} has been created!'.format(self.name))
        path = Path(self.csvfile)
        if not path.is_file():
            logging.debug('restaurant.csv not found, will be created.')
            with open('./restaurant.csv','w') as csv_file:
                fieldnames = ['Name', 'Count']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        else:
            logging.debug('restaurant.csv already exists. Nothing to do.')
        
    def ask_name(self):
        word = "Hello! May I ask your name?\n"
        print('=' * len(word) + '\n' + word + '=' * len(word) + '\n')
        ans = input()
        if not ans:
            return self.ask_name()
        return ans
    
    def ask_restaurant(self, username, recommend_restaurant):
        if not recommend_restaurant:
            word = "{}-san, Which restaurant do you like?\n".format(username)
            print('=' * len(word) + '\n' + word + '=' * len(word) + '\n')
            ans = input()
            if not ans:
                return self.ask_restaurant(username)
            return ans
        else:
            word = "{}-san, My recommend is {}. Do you like that?\n".format(username, recommend_restaurant)
            print('=' * len(word) + '\n' + word + '=' * len(word) + '\n')
            yorn = input()
            if not yorn:
                return self.ask_restaurant(username, recommend_restaurant)
            if yorn == "yes":
                return recommend_restaurant
            else:
                return self.ask_restaurant(username, "")
    
    def file_read(self):
        logging.debug('process is going into file_read')
        with open('./restaurant.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            restaurant_list = []
            for row in reader:
                restaurant_list.append([row['Name'], row['Count']])
            if len(restaurant_list) > 1:
                for i in len(restaurant_list)-1,-1,1:
                    if restaurant_list[i][1] > restaurant_list[i-1][1]: 
                        recommend_restaurant = restaurant_list[i][0]
                    elif restaurant_list[i][1] < restaurant_list[i-1][1]:
                        recommend_restaurant = restaurant_list[i-1][0]
                    else:
                        recommend_restaurant = restaurant_list[i][0]
            elif len(restaurant_list) == 1:
                recommend_restaurant = restaurant_list[0][0]
            else:
                recommend_restaurant = ""
            logging.debug('{} is returned from file_read, as recommendation'.format(recommend_restaurant))
            return recommend_restaurant
    
    def file_append(self, restaurant):
        with open('./restaurant.csv','a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([restaurant, 1])

roboko = Roboko('Hanako')
recommend_restaurant = roboko.file_read()
print(recommend_restaurant)
username = roboko.ask_name()
restaurant = roboko.ask_restaurant(username, recommend_restaurant)
print(username, restaurant)
roboko.file_append(restaurant)
