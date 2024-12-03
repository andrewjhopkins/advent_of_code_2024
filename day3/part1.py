import re
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])

    output = 0

    for line in lines:
        matches = parse_muls(line)
        for match in matches:
            output += (int(match[0]) * int(match[2]))
    
    print(output)


def parse_muls(line):
    pattern = r'mul\(\s*(-?\d+(\.\d*)?)\s*,\s*(-?\d+(\.\d*)?)\s*\)'
    matches = re.findall(pattern, line)
    return matches

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