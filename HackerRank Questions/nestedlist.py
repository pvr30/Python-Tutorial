nested_list = []
scores = set()
second_lowest_names = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
        scores.add(score)

print(sorted(scores))
second_lowest = sorted(scores)[1]
print(second_lowest)

for name, score in nested_list:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name)





#print(nested_list)