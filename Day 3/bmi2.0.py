height=float(input("Enter your height"))
weight=int(input("Enter your weight"))

bmi=round(weight/height ** 2)

if bmi< 18.5:
    print(f"your bmi is  {bmi}, and you are Underweight")
elif bmi<25:
    print(f"your bmi is  {bmi}, and you are normal wiehgt")
elif bmi>25 & bmi<30:
    print(f"your bmi is  {bmi}, and you are Overwieht")
elif bmi<35:
    print(f"your bmi is  {bmi}, and you are Obese")
elif bmi >35:
    print(f"your bmi is  {bmi}, and you are Clinically obese")