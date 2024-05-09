import sys

file_name = "todo_data.txt"
todos = []
# Read file
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

# Add Todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    todos.append(f"{sys.argv[2]}\n")

# Remove ToDo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        index_to_delete = int(sys.argv[2])
        if index_to_delete > 0:
            index_to_delete -= 1
            del(todos[index_to_delete])
        else:
            print("wrong index")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)


#Save File
file = open(file_name, "w")
todos = file.writelines(todos)
file.close()

# print List
if todos is not None:
    if len(todos) == 0:
        print("You have no todo")
    else:
        print("\nHere's your ToDo List:\n")
        for todo in range((len(todos))):
            print(f"{todo + 1}. {todos[todo]}")


#print commands
print(f"***********************************")
print(f"To view ToDo's:\n{sys.argv[0]}\n")
print(f"To add ToDo\n{sys.argv[0]} add \"clean Room\"\n")
print(f"To remove or complete ToDo's:\n{sys.argv[0]} remove 2\n")