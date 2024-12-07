import re
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    (rule_lines, lines) = get_input(sys.argv[1])

    rules = {}
    
    for line in rule_lines:
        line_split = line.split("|")

        val = int(line_split[1])
        key = int(line_split[0])

        if key not in rules:
            rules[key] = [val]
        else:
            rules[key].append(val)

    inputs = []

    for line in lines:
        line_split = line.split(",")
        input = []
        for l in line_split:
            input.append(int(l))

        inputs.append(input)

    output = 0

    for input in inputs:
        ans = correct(input, rules)
        if not ans:
            sort(input, rules)
            output += input[len(input) // 2]

    print(output)

def correct(input, rules):
    seen = set()
    incorrect = []

    for i in range(len(input)):
        num = input[i]
        if num in rules:
            for s in rules[num]:
                if s in seen:
                    incorrect.append((num, i))
        seen.add(num)

    return len(incorrect) == 0

def sort(input, rules):
    i = 0
    while i < len(input):
        good = True
        for j in range(i+1, len(input)):
            if greater(input[i], input[j], rules):
                input[i], input[j] = input[j], input[i]
                good = False
        if good:
            i += 1
    return

def greater(num1, num2, rules):
    if num1 in rules and num2 in rules[num1]:
        return False
    return True
    
def get_input(file_name):
    rule_lines = []
    lines = []

    break_found = False

    with open(file_name) as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.strip()
            if len(line) == 0:
                break_found = True
            elif not break_found:
                rule_lines.append(line)
            else:
                lines.append(line)

    return (rule_lines, lines)

if __name__ == "__main__":
    main()
