import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part2.py input.txt")
        return

    lines = get_input(sys.argv[1])
    output = 0

    for line in lines:
        line_split = line.split()
        for i in range(len(line_split)):
            line_split[i] = int(line_split[i])
        result = safe(line_split)

        if not result:
            for i in range(len(line_split)):
                new_result = safe(line_split[:i] + line_split[i+1:])
                if new_result:
                    result = True
                    break
            
            
        if result:
            output += 1
    
    print(output)
    return output

def safe(line_split):
    i = 1
    increase = line_split[0] < line_split[-1]

    for i in range(1, len(line_split)):
        i = i if i >= 1 else 1

        if increase and line_split[i] < line_split[i - 1]:
            return False

        elif not increase and line_split[i] > line_split[i - 1]:
            return False

        if abs(line_split[i] - line_split[i - 1]) < 1 or abs(line_split[i] - line_split[i - 1]) > 3:
            return False

    return True

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