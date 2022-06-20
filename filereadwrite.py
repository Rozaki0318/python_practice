file = './test.txt'
l = ['Tako', 'Ika', 'Same']

with open(file, 'w') as f:
  for line in l:
    f.write(line + '\n')

with open(file, 'r') as f:
  while True:
    line = f.readline()
    print(line, end='')
    if not line:
      break