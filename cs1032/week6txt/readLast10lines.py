try:
    file = open("w/Users/na/Documents/GitHub/tutorials/cs1032/week6txt/example.txt", "r")
    lines = file.readlines()
    last_ten_lines = lines[-10:]
    for line in last_ten_lines:
        print(line)
    file.close()
except IOError:
    print("File not found or path is incorrect :(")
except:
    print("An error occurred while reading the file!")