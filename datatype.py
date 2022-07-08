# Dict
d = {'x':10, 'y':20, 'z':[30,40,50]}
d2 = {'x':1000, 'j': "text"}
print(d['z'])
print(d2)
d.update(d2)
print(d)

for v in d:
    print('value:{}'.format(v))
# Keyがprintされる

for k, v in d.items():
    print('key:{}, value:{}'.format(k, v))
# Dict型が持つitemsメソッドを使うと、KeyとValueがprintされる