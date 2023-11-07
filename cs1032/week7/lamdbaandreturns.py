# method 1
def lambdaDemo(x, y, operation):
    return operation(x, y) # lambda functions can be taken as arguments

print(lambdaDemo(1, 2, lambda x, y: x + y))

# method 2
def lambdaAdd():
    return lambda x, y: x + y

addWithLambda = lambdaAdd()
print(addWithLambda(1, 2))

# method 3
def add(x, y):
    return x + y 

print(add(1, 2))