import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part1.py input.txt")
        return

    lines = get_input(sys.argv[1])
    grid = []
    for line in lines:
        line_split = list(line)
        grid.append(line_split)
    
    starting = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                starting = (i, j)
    
    direction = (-1, 0)
    seen = set()

    i = starting[0]
    j = starting[1]

    seen.add((i, j))

    while i >= 0 and i <= len(grid) - 1 and j >= 0 and j <= len(grid[i]) - 1:
        new_position = (i + direction[0], j + direction[1])
        if new_position[0] < 0 or new_position[0] > len(grid) - 1 or new_position[1] < 0 or new_position[1] > len(grid[new_position[0]]) - 1:
            break
        else:
            if grid[new_position[0]][new_position[1]] == "#":
                if direction == (-1, 0):
                    direction = (0, 1)
                elif direction == (0, 1):
                    direction = (1, 0)
                elif direction == (1, 0):
                    direction = (0, -1)
                elif direction == (0, -1):
                    direction = (-1, 0)
            else:
                seen.add(new_position)
                i = new_position[0]
                j = new_position[1]
    
    print(len(seen))

def get_input(file_name):
    lines = []

    with open(file_name) as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.strip()
            lines.append(line)

    return lines

if __name__ == "__main__":
    main()
