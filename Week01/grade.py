student = {
    "A" : 66,
    "B" : 71,
    "C" : 25,
    "D" : 97,
    "E" : 85
}

total = 0

for name, score in student.items():
    if score >= 90:
        grade = 'A등급'
    elif score >= 80:
        grade = 'B등급'
    elif  score >= 70:
        grade = 'C등급'
    else:
        grade = 'D등급'

    print(name, '학생 :', score,'점,', grade)
    total = total + score


average = total / len(student)

print('전체 평균 : ', average)
print('최고점 : ', max(student.values()))
print('최저점 : ', min(student.values()))