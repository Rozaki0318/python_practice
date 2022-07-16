import shutil
import psutil


print(shutil.disk_usage('/'))

print(psutil.cpu_percent())

file = open('test.txt', 'r')
print(file.readline())
print(file.read())
file.close()

# readline
with open('test.txt') as file:
  print(file.readline())

with open('test.txt') as file:
  for line in file:
    print(line.strip().upper())

# readlines
with open('test.txt') as file:
  lines = file.readlines()
  lines.sort()
  print(lines)

# write
with open('test.txt', 'a') as file:
  file.write('kujira')

with open('test.txt') as file:
  for line in file:
    print(line.strip().upper())