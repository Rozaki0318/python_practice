
a = 'aBvDcAvhA'
print(a.lower())
print(a.upper())
print(len(a))
for b in a:
  print(b)

print(a.count('A'))
print(a.count('v'))

c = ".s.e.v.b.a. de.h w.  .wawd......"
print(c.split('.'))
print(c.split(' '))


d = 'abcdeabcd'
print(d.replace('abcd', '777'))


f = ['omae','ha','ahoka']
print((' ').join(f))