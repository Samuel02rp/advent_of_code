data = 'input.txt'

try:
    with open(data, 'r') as f:
        LEFT = 'L'
        MAX = 100
        dial = 50
        password = 0
        for line in f:
            line.strip()
            if LEFT in line:
                idx = int(line.index(LEFT)) + 1
                dial = (dial - int(line[idx:])) % MAX
            else:
                dial = (dial + int(line[1:])) % MAX
            if dial == 0:
                password += 1
        print(password)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
