a = 1
print(id(a))
b = 0
print(id(b))
b = a
print(id(b))
a = 2
print(id(a))
print(id(b))
print(a,b)