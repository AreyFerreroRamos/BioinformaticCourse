s = "Hola, que tal?"

f = open("name_file.txt", "w")
f.write(s)
f.close()

f = open("name_file.txt", "r")
data = f.read()
print(data)
f.close()

with open("name_file.txt", "r") as f:
    print(f.read())
