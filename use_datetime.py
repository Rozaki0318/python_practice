import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()
print(today)

t = datetime.time(hour=1, minute=13, second=5, microsecond=10)
print(t)

print(now)
d = datetime.timedelta(weeks=1)
print(now - d)


import time 
print('###')
time.sleep(2)
print('###')


# backup file
import os
import shutil
import subprocess

file_name = 'test.txt'
if os.path.exists(file_name):
  shutil.copy(file_name, "backup_{}.{}".format(file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))


print(subprocess.run(['ls', '-la']))