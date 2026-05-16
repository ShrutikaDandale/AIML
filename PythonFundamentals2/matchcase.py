# matchcase problem
color = input("enter colour: ")

match color:
    case "green":
        print("go")
    case "yellow":
        print("look")
    case "red":
        print("stop")
    case _ :
        print("wrong colour") #default case    

        # this case is not offently used