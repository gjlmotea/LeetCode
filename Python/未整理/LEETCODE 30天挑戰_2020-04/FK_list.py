a = [1,2,3,4]
b = a.copy()
print(id(a))
print(id(b))

b[0] = 1234
print(a)
print(b)

print("================================")

x = [[1,2,3],[4,5,6],[7,8,9]]
y = x.copy()
print(id(x))
print(id(y))

x[0][0] = 999
print(x)
print(y)
