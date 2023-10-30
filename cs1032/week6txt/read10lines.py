try:
    file = open("/Users/na/Documents/GitHub/tutorials/cs1032/week6txt/example.txt", "r")
    for i in range(10):
        print(file.readline())
    file.close()
except IOError:
    print("File not found or path is incorrect :(")
except:
    print("An error occurred while reading the file!")