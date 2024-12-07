import re
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])
    outs = []
    ins = []

    for line in lines:
        split_index = line.index(":")
        outs.append(int(line[:split_index]))

        split_ins = line[split_index+1:].strip()
        str_nums = split_ins.split(" ")

        inputs = []
        for num in str_nums:
            inputs.append(int(num))

        ins.append(inputs)

    output = 0

    for i in range(len(ins)):
        if (solve(outs[i], ins[i]) > 0):
            output += outs[i]


    print(output)

def solve(out, inputs):
    return helper(out, 0, inputs)

def helper(target, current, ins):

    if len(ins) == 0 and current == target:
        return 1

    if len(ins) == 0 or current > target:
        return 0

    return helper(target, current + ins[0], ins[1:]) + helper(target, current * ins[0], ins[1:])

    
def get_input(file_name):
    lines = []
    with open(file_name) as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.strip()
            if len(line) != 0:
                lines.append(line)

    return lines

if __name__ == "__main__":
    main()
