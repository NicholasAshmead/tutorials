def sumDigits(string):
    sum = 0
    for char in string:
        if char.isdigit(): sum += int(char) # including epic failsafe against letters
    return sum

print(sumDigits("Hello, 123!"))