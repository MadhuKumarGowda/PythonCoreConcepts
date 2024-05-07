# read the file here
file = open("number_file.txt", "r")
lines = file.readlines()
file.close()

# Edit the file here
for x in range(len(lines)):
    try:
        number = float(lines[x]) * 2
        lines[x] = f"{number}\n"
    except:
        pass
# Write the file here
file = open("number_file.txt","w")
file.writelines(lines)
file.close()
