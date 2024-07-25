def foo(x):
    return x + 1

l_especial = ["agumon", 3.45, dict(), foo]
print(l_especial[3](1))

dic = {
    1: "Arey",
    "Arey": 1,
    "function": foo,
    "lista": l_especial,
    "dict": {"a": 1, "b": 2} 
}
print(dic)
print(dic["Arey"])

print(dic.keys())
print(dic.values())

for x in l_especial:
    print(x)

print("**********")

for i in range(4):
    print(l_especial[i])
