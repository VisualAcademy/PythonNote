# if elif 구문을 사용한 점수에 따른 학점 계산 프로그램

score = int(input("당신의 점수는? "))
grade = 'F'

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("점수: ", score)
print("학점: ", grade)
