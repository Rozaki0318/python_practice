# list_practice

a = [1, 2, 3, 4, 5]

# 一番最初の要素
print(a[0])

# 一番最後の要素
print(a[-1])

# 最後に要素追加
a.append(6)
print(a)

# 途中に要素追加
a.insert(1,'A')
print(a)

# 要素取り出し
# index指定
a.pop(1)
print(a)

# value指定
a.remove(6)
print(a)

# 逆順
a.reverse()
print(a)

# ソート
b = [3, 1, 7, 2, 2, 8, 10, 5, 9, 6, 4]

b.sort()
print(b)

# count
c = ['apple', 'grape', 'orange', 'apple', 'apple', 'grape', 'apple', 'apple']
print("Apple: {}".format(c.count('apple')))
print("Grape: {}".format(c.count('grape')))

# List comprehenshion
# [expression for variable in sequence if condition]
print([x*2 for x in a if x % 2 == 1])

# try remove if the value exists in the dictionary
d = ['a', 'b', 'c']
e = ['a', 'b', 'c', 'd', 'e']
try:
  d.remove('c')
  e.remove('f')
except:
  pass
print("d is {}".format(d))
print("e is {}".format(e))