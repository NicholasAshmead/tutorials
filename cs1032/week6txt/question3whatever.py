f = open("/Users/na/Documents/GitHub/tutorials/cs1032/week6txt/example.txt", "w+")

for line in f:
    if "rat" not in line:
        f.write(line + "rat\n")

f.write("This file has been ratted\n")