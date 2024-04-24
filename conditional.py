direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")        
    case "south":
        print("Down")
    case "west":
        print("Left")
    case "east":
        print("Right")
    case _:
        print("Not a valid direction")
    