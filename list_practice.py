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

# List comprehenshion
# [expression for variable in sequence if condition]
print([x*2 for x in a if x % 2 == 1])