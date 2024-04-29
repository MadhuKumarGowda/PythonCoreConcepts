import sys

total = 1
del(sys.argv[0])
for argument in sys.argv:
    try:
        number = int(argument)
        total *= number    
    except Exception as e:
        print(e)
        print("Only numbers can be provided")

print(total)