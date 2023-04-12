a = {"n"}
print(type(a))
a.add("hh")
print(a)
b = ["Sayantan", "Kar"]
c = (54, 89)
a.update(b)
a.update(c)
a.remove(54)
print(a)

if "Sayantan" in a:
    print(True)
else:
    print(False)

# b={"n":"This is string","m":"Hello world!"}
# print(type(b))

# c=[4,5,7,8,5,4,2,1]
# print(c)
# c=list(set(c))
# print(c)


# Todo: Thanks
