# break
student_marks = [100,34,50,32,68,30]
for i in student_marks:
    if i < 33:
        print("You Are Fail In Exam")
        break;
    print("Congratulation You Are Pass.")

# continue
print("\n")
for i in student_marks:
    if i < 33:
        print("You Are Fail In Exam")
        continue
    print("Congratulation You Are Pass.")