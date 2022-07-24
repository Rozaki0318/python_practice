#!/usr/bin/env python3

import csv
import re
import operator

err_dict = {}
user_dict = {}

#The ranking of errors generated by the system
with open('syslog.log') as file:
    for line in file:
        err_line = re.search(r"ERROR\s([\w\s']*)", line)
        if err_line:
            if err_line.group(1).strip() in err_dict:
                err_dict[err_line.group(1).strip()] += 1
            else:
                err_dict[err_line.group(1).strip()] = 1
        else:
            pass

print(err_dict)
sort_err_dict = sorted(err_dict.items(), key = operator.itemgetter(1), reverse=True)
print(sort_err_dict)
#The user usage statistics for the service 
with open('syslog.log') as file:
    for line in file:
        line = line.strip()
        user_line = re.search(r"\(([.\s\w]*)\)$", line)
        if user_line:
            if user_line.group(1) in user_dict:
                if re.search(r"INFO", line):
                    user_dict[user_line.group(1)]['INFO'] += 1
                elif re.search(r"ERROR", line):
                    user_dict[user_line.group(1)]['ERROR'] += 1
            else:
                if re.search(r"INFO", line):
                    user_dict[user_line.group(1)] = {'INFO':1, 'ERROR':0}
                elif re.search(r"ERROR", line):
                    user_dict[user_line.group(1)] = {'INFO':0, 'ERROR':1}                                                                                                                   
sort_user_dict = sorted(user_dict.items(), key=operator.itemgetter(0))
print(sort_user_dict)
with open('error_message.csv', 'w') as csv_errfile:
    fieldsnames = ["Error", "Count"]
    writer = csv.DictWriter(csv_errfile, fieldnames=fieldsnames)
    writer.writeheader()
    for key in sort_err_dict:
        writer.writerow({"Error": key[0], "Count": key[1]})

with open('user_statistics.csv', 'w') as csv_userfile:
    fieldsnames = ["Username", "INFO", "ERROR"]
    writer = csv.DictWriter(csv_userfile, fieldnames=fieldsnames)
    writer.writeheader()
    for key in sort_user_dict:
        writer.writerow({"Username": key[0], "INFO": key[1]['INFO'], "ERROR": key[1]['ERROR']})