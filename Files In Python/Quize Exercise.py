"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""

que = open("questions.txt", 'r')

questions = [line.strip() for line in que]

que.close()

score = 0
total = len(questions)

for lists in questions:
    q, a = lists.split("=")

    ans = input(f"{q}=")
    if a == ans:
        score += 1


calculate_score = open("result.txt", 'w')

calculate_score.write(f"Your Final Score Is {score}/{total}")

calculate_score.close()
