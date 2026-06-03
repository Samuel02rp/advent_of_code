data = 'input.txt'

try:
    with open(data, 'r') as f:
        ranges = f.readline().strip().split(',')
        total = 0
        for scope in ranges:
            start, end = scope.split('-')
            for num in range(int(start), int(end) + 1):
                id_value = str(num)
                length = len(id_value)
                for chopped_len in range(1, length // 2 + 1):
                    if length % chopped_len == 0:
                        chopped = id_value[:chopped_len]
                        if id_value == (length // chopped_len * chopped):
                            total += num
                            break
        print(total)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
