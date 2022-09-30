
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
print(len(student_heights))
sum=0
for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
  sum=sum+int(student_heights[n])

# print(f"sum total {sum}")
round_dt=(sum/len(student_heights))
print(f"average = {round(round_dt)}")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

