import os

# get current dir
print(os.getcwd())

# create dir and move the dir
#os.mkdir('new_dir')
#os.chdir('new_dir')
#print(os.getcwd())

# remove dir
os.mkdir('newer_dir')
os.rmdir('newer_dir')

print(os.listdir())
print(os.path.isdir())