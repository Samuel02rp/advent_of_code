data = 'input.txt'

try:
    with open(data, 'r') as f:
        LEFT = 'L'
        MAX = 100
        password = 0
        dial = 50
        for line in f:
            line = line.strip()
            if LEFT in line:
                idx = int(line.index(LEFT)) + 1
                if (move := int(line[idx:])) >= dial and dial != 0:
                    password += abs((dial - move)) // MAX + 1
                if dial == 0:
                    password += move // MAX
                dial = (dial - move) % MAX
            else:
                password += (dial + (move := int(line[1:]))) // MAX
                dial = (dial + move) % MAX
        print(password)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
