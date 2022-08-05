print("""

Hi, This Program is a file type converter (JSON to Text)

""")
x = input("Location of The File: ")
y = input("Name of the New File Generated: ")
z = input("Keywords to remove: ")

with open(x) as file:
    file.seek(0)
    data = file.read()



data = data.replace("'", "").replace("{", "").replace("}", "").replace('"', '').replace("[", "").replace("]", '\n').replace(r'\n', ' \n ').replace(z, "")
print(data)


f = open(y, "w")
f.write(data)



