file = open("testFile.txt", "r")
#one way to read file
#file_text = file.read()
#another way to read the file
#print(file_text)
lines =  file.readlines()
for line in lines:
    print(line)

file.close()

nfile = open("numbers.txt","r")
total = 1
for line in nfile:
    try:
        number = float(line)
        total *= number
    except:
        pass
print(total)

nfile.close()

