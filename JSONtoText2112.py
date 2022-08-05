print("""

Hi, This Program is a file type converter (JSON to Text)

""")
x = input("Location of The File: ")
y = input("Name of the New File Generated: ")
z = input("Keywords to remove: ")

with open(x) as file:
    file.seek(0)
    data = file.read()

z = list(z.split(","))

b = []

for i in range(len(z)):
    b.append(i)

b = len(b)
c = []
for i2 in range(b):
    c.append("")

dictionary = dict(zip(z, c))



print(z)

data = data.replace("'", "").replace("{", "").replace("}", "").replace('"', '').replace("[", "").replace("]", '\n').replace(r'\n', ' \n ')

for index1, index2 in dictionary.items():
    data = data.replace(index1, index2)

print(data)


f = open(y, "w")
f.write(data)




