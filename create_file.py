# x indicates, create file only if doesn't exists
file = open("testFile.txt", "x")
file.write("Welcome to Python world")
file.close()

# w indicates, overwriting the exisiting file
file = open("testFile.txt", "w")
file.write("Welcome to Python world, from madhu kumar")
file.close()

# a indicates, overwriting the exisiting file
file = open("testFile.txt", "a")
file.write("Append text,  Mysore")
file.close()