student_scores = [55,78, 65, 89, 86, 55, 91, 64, 63,99,55,105]
# print(len(student_scores))
score=0
for i in range(0,len(student_scores)):
    # student_scores[i]=student_scores[i]
    if score < student_scores[i]:
        score=student_scores[i]

print(score)   
        #     
# highest_score=0
# for score in student_scores:
#     if score > highest_score:
#         highest_score=score
# print(highest_score)