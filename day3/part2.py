import re
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part2.py input.txt")
        return

    line = get_input(sys.argv[1])

    output = 0

    mul_pattern = r'mul\(\s*(-?\d+(\.\d*)?)\s*,\s*(-?\d+(\.\d*)?)\s*\)'
    matches = parse(line, mul_pattern, True)

    do_pattern = r'do\(\)'
    dos = parse(line, do_pattern)

    dont_pattern = r"don't\(\)"
    donts = parse(line, dont_pattern)

    combine = matches + dos + donts
    combine.sort(key = lambda x: x[-1])

    do = True
    for c in combine:
        if c[0][0] == "m":
            if not do:
                continue
            output += int(c[1]) * int(c[2])

        elif c[0][0] == "d" and len(c[0]) > 4: # don't
            do = False

        else:
            do = True
        
    print(output)
    
def parse(line, pattern, has_value=False):
    
    matches = []

    for match in re.finditer(pattern, line):
        match_text = match.group(0)  # The full match string
        start_index = match.start()  # The starting index of the match

        if has_value:
            first_value = match.group(1)
            second_value = match.group(3)
            matches.append((match_text, first_value, second_value, start_index))
        else:
            matches.append((match_text, start_index))

    return matches

def get_input(file_name):
    with open(file_name) as file:
        file_line = file.read()
    return file_line

if __name__ == "__main__":
    main()