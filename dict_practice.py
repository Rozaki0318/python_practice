# dict_practice

x = {'key1':1, 'key2':2, 'key3':3}
print(x)

# Returns the number of items in the dictionary
print(len(x))

# Iterates over each key in the dictionary
for key in x:
  print(key)

# Iterates over each key,value pair in the dictionary
for key, value in x.items():
  print(key, value)

# Checks whether the key is in the dictionary
if 'key3' in x:
  print(True)

# Accesses the item with key key of the dictionary
print(x['key2'])

# Sets the value associated with key
x['key3'] = 'A'
print(x)

# Removes the item with key key from the dictionary
x['key4'] = 4
print(x)
del x['key1']
print(x)

## Methods

print(x.get('key4'))
print(x.keys())
print(x.values())

# Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
b = {'key1':'b', 'key2':'bb', 'key3':'bbb'}
x.update(b)
print(x)

# Removes all the items of the dictionary
x.clear()
print(x)

# try remove if the value exists in the dictionary
c = {'key1':'c', 'key2':'cc', 'key3':'ccc'}
try:
  c.remove('c')
except:
  pass
print(c)

