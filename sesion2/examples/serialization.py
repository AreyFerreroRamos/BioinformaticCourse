import pickle

with open("lorem_ipsum.txt", "r") as f:
    data = f.read()

words = data.split()
print(words)

pickle.dump(words, open("my_ser.pickle", "w"))

words2 = pickle.load(open("my_ser.pickle", "w"))
print(words2)

a = "kjadrdhgjrjH"
print(a.startswith("k"))
