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
        if ans:
            output += input[len(input) // 2]

    print(output)


def correct(input, rules):
    seen = set()
    ans = True
    incorrect = []

    for i in range(len(input)):
        num = input[i]
        if num in rules:
            for s in rules[num]:
                if s in seen:
                    incorrect.append((num, i))
        seen.add(num)

    print(incorrect)
    return len(incorrect) == 0
    
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
