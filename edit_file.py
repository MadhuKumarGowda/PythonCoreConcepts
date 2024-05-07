# read the file here
file = open("testFile.txt", "r")
lines = file.readlines()
file.close()

# Edit the file here
# below code will overwrite the content of file
# lines = ["Hello\n", "My Name", "is", "Madhu"]

# below code will insert the data any posiiton of the file
lines.insert(0, "Hello from Python\n")

# below code to insert the text end of the file, but it doesn't add new line
# so below code is help to add new line 
lines[-1] = lines[-1] + "\n"
lines.append("End of the file")


# Write the file here
file = open("testFile.txt","w")
file.writelines(lines)
file.close()

