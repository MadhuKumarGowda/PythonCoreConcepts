print("before")

try:
    print(age)
except NameError as e:
    print("This was a name issue")
    print(e)
except ZeroDivisionError:
    print("Can't divide by 0")
except Exception as e:
    print("Somethig went wrong")


class CustomError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise CustomError("The word has to have at lease one letter")
    return word.upper()

print(upper_fun(""))
