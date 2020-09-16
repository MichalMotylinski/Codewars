import re
string = "AnItA"


def hello(name=""):
    if re.match("^[a-zA-Z]*$", name) and not len(name) == 0:
        return "Hello, " + name[0].upper() + name[1:].lower() + "!"
    else:
        return "Hello, World!"


print(hello(string))
