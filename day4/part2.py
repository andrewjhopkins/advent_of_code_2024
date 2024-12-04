import re
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])
    output = 0
    grid = []

    for line in lines:
        line_split = list(line)
        grid.append(line_split)
    
    good = ["M", "S"]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                if i - 1 >= 0 and j - 1 >= 0 and i + 1 <= len(grid) - 1 and j + 1 <= len(grid[i]) - 1:
                    if grid[i - 1][j - 1] != grid[i + 1][j + 1] and grid[i - 1][j + 1] != grid[i + 1][j - 1]:
                        if grid[i - 1][j - 1] in good and grid[i + 1][j + 1] in good and grid[i - 1][j + 1] in good and grid[i + 1][j - 1] in good:
                            output += 1

    print(output)
    
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
