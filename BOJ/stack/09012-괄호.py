t = int(input())

for tc in range(t):
    input_data = input()
    brackets = []

    for i in input_data:
        if i == "(":
            brackets.append(i)
        elif brackets and brackets[-1] == '(' and i == ")":
            brackets.pop()
        else:
            brackets.append(i)

    print("NO" if brackets else "YES")
