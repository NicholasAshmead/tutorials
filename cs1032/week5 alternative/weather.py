temperatures = []
for i in range(7):
    temperatures.append(int(input(f"Enter the temperature on day {i+1}:")))

print((sum(temperatures)/7).__round__(2))