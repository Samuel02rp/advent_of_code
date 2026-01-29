data = 'input.txt'

try:
    with open(data, 'r') as file:
        rotations = []
        for line in file:
            if 'L' in line:
                pos_L = line.index('L')
                rotations.append(line[pos_L:])
            elif 'R' in line:
                pos_R = line.index('R')
                rotations.append(line[pos_R:])
            else:
                print('Data format error')
except FileNotFoundError:
    print(f'Error: the file {data} was not found.')

dial = 50
password = 0
for instruction in rotations:
    if 'L' in instruction:
        dial = (dial - int(instruction[1:])) % 100
    elif 'R' in instruction:
        dial = (dial + int(instruction[1:])) % 100
    if dial == 0:
        password += 1
print(password)
