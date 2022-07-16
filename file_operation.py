import os
import datetime

# remove file, rename file
#os.remove("novel.txt")
#os.rename("old.txt", "new.txt")

# check if file exists
print(os.path.exists("text.txt"))
print(os.path.exists("novel.txt"))

# size of file
print(os.path.getsize('text.txt'))

# timestamp of file
timestamp = os.path.getmtime('text.txt')
print(datetime.datetime.fromtimestamp(timestamp))
# extract the date portion yyyy-mm-dd
htimestamp = str(datetime.datetime.fromtimestamp(timestamp))
print(htimestamp[:10])

# get full path of file
print(os.path.abspath('text.txt'))