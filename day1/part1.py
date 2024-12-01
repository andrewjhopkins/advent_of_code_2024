import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])

    right = []
    left = []

    for line in lines:
        first_num, end_index = get_num(line, 0)
        while line[end_index] == " ":
            end_index += 1
        second_num, _ = get_num(line, end_index)
        right.append(int(first_num))
        left.append(int(second_num))

    right.sort()
    left.sort()

    output = 0
    for i in range(len(right)):
        output += abs(right[i] - left[i])
        
    print(output)

def get_num(line, start_index):
    end_index = start_index
    while end_index < len(line) and line[end_index] != " ":
        end_index += 1
    return line[start_index:end_index], end_index



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