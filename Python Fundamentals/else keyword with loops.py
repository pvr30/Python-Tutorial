# else keyword with loops.
# On loops, you can add an `else` clause.
# This only runs if the loop does not encounter a `break` or an error.
# That means, if the loop completes successfully, the `else` part will run.
student_marks = [100,34,50,39,68,37]
for i in student_marks:
    if i < 33:
        print("You Are Fail In Exam")
        break;
    print("Congratulation You Are Pass.")
else:
    print("All Students are Pass")
    