data = 'input.txt'

try:
    with open(data, 'r', encoding='utf-8-sig') as f:
        dial = 50
        password = 0
        for line in f:
            line.strip()
            if 'L' in line:
                dial = (dial - int(line[1:])) % 100
            elif 'R' in line:
                dial = (dial + int(line[1:])) % 100
            else:
                print('Data format error')
            if dial == 0:
                password += 1
        print(password)
except FileNotFoundError:
    print(f'Error: the file {data} was not found.')
