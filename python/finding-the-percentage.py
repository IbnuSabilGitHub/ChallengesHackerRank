def finding_percentage(dict, query_name):
    value = dict[query_name]
    return sum(value) / 3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    answer = finding_percentage(student_marks, query_name)
    print("{:.2f}".format(answer))