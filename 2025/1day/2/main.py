data = 'input.txt'

try:
    with open(data, 'r', encoding='utf-8-sig') as f:
        password = 0
        dial = 50
        for line in f:
            line = line.strip()
            if 'L' in line:
                for _ in range(int(line[1:])):
                    dial = (dial - 1) % 100
                    if dial == 0:
                        password += 1
            elif 'R' in line:
                for _ in range(int(line[1:])):
                    dial = (dial + 1) % 100
                    if dial == 0:
                        password += 1
            else:
                print('Data format error')
        print(password)
except FileNotFoundError:
    print(f'Error: the file {data} was not found.')
