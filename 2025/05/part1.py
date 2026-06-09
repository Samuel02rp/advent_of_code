data = 'input.txt'

try:
    with open(data) as f:
        SEP = '-'
        ranges = []
        num_fresh = 0
        for line in f:
            if SEP in line:
                floor, ceiling = map(int, line.strip().split(SEP))
                ranges.append(range(floor, ceiling + 1))
            else:
                if line.strip():
                    num_fresh += any(int(line.strip()) in r for r in ranges)
        print(num_fresh)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
