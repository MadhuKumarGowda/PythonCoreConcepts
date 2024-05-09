import pickle

age = 33

#w is writing file and b is writing binary
file = open("test.txt", "wb")
pickle.dump(age, file)
file.close()

file = open("test.txt","rb")
new_age = pickle.load(file)
file.close()

print(new_age)