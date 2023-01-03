N = int(input())
with open('applicants.txt', 'r') as f:
    data = [line.split() for line in f]

count = {'Biotech': 0, 'Chemistry': 0, 'Engineering': 0, 'Mathematics': 0, 'Physics': 0}
final = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
grade = {'Biotech': [3, 2], 'Chemistry': 3, 'Engineering': [5, 4], 'Mathematics': 4, 'Physics': [2, 4]}
used = []

for i in range(7, 10):
    for department in final.keys():
        if type(grade[department]) == list:
            sorted_data = sorted(data, key=lambda x: (-max(float(x[6]), ((float(x[grade[department][0]]) + float(x[grade[department][1]])) / 2)), x[0], x[1]))
        else:
            sorted_data = sorted(data, key=lambda x: (-max(float(x[6]), float(x[grade[department]])), x[0], x[1]))
        for entry in sorted_data:
            name = ' '.join([entry[0], entry[1]])
            if count[entry[i]] == N or name in used or entry[i] != department:
                continue
            else:
                if type(grade[department]) == list:
                    final[entry[i]].append(' '.join([name, str(max(float(entry[6]), (float(entry[grade[department][0]]) + float(entry[grade[department][1]])) / 2))]))
                else:
                    final[entry[i]].append(' '.join([name, str(max(float(entry[6]), float(entry[grade[department]])))]))
                count[entry[i]] += 1
                used.append(name)

for department in final.keys():
    with open('{}.txt'.format(department), 'w') as f:
        f.writelines(line + '\n' for line in sorted(final[department], key=lambda x: (-float(x.rsplit(' ', 1)[1]), x.rsplit(' ', 1)[0])))
