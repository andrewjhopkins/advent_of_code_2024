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
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                directions = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, -1), (-1, 0)]
                for d in directions:
                    found = dfs(grid, i, j, 0, "XMAS", d[0], d[1])
                    if found:
                        output += 1

    print(output)

def dfs(grid, i, j, index, target, i_change, j_change):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return False
    if index == len(target) - 1 and target[index] == grid[i][j]:
        return True
    if target[index] != grid[i][j]:
        return False
    
    return dfs(grid, i + i_change, j + j_change, index + 1, target, i_change, j_change)
    
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
