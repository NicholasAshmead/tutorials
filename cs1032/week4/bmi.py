def bmi(weight,height):
    return weight/(height**2).__round__(1)

def bmiCategorise(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Healthy"
    elif bmi < 30: return "Overweight"
    elif bmi < 40: return "Obese"
    else: return "Severely Obese"


w = float(input("Weight (in kg):"))
h = float(input("Height (in m):"))
bmi = bmi(w,h)
print(bmi)
print(bmiCategorise(bmi))