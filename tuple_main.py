a = []
b = ()
print(type(a))
print(type(b))
a = [1, 2, 3, "jui"]
b = (1, 2, 3, "jui")

print(a)
print(b)

# a = [4]
# print(a)
# print(type(a))

b = ("1",)
print(b)
print(type(b))

b = b + ("2",)
print(b)
print(type(b))

for i in a:
    print(type(i), i)

for i in b:
    print(type(i), i)

c = len(b)
print(c)

a = tuple(a)
print(type(a))
print(a)

b = list(b)
print(type(b))
print(b)

# Todo: Thanks
