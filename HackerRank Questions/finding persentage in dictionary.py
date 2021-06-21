if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


for name in student_marks:
    if query_name == name:
        marks_list = student_marks[query_name]


result = (marks_list[0]+marks_list[1]+marks_list[2])/3

print(format(result, '.2f'))
"""
names = {
    "name1": "Vishal",
    "name2": "Harsh",
    "name3": "Sahil"
}
name = input()
for l in names:
    if name == l:
        print(names[name])
"""