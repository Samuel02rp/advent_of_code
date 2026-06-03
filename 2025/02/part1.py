data = 'input.txt'

try:
    with open(data, 'r') as f:
        ranges = f.readline().strip().split(',')
        total = 0
        for scope in ranges:
            start, end = scope.split('-')
            for num in range(int(start), int(end) + 1):
                id_value = str(num)
                if id_value[: len(id_value) // 2] == id_value[len(id_value) // 2 :]:
                    total += num
        print(total)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
