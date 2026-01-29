data = 'input.txt'

try:
    with open(data, 'r') as file:
        ranges = file.readline().strip().split(',')
except FileNotFoundError:
    print(f'Error: the file {data} was not found.')

add_up = 0
for range_ in ranges:
    start, end = range_.split('-')
    for id in range(int(start), int(end) + 1):
        id_ = str(id)
        length = len(id_)
        for chopped_len in range(1, length // 2 + 1):
            if length % chopped_len == 0:
                chopped = id_[:chopped_len]
                if id_ == length // chopped_len * chopped:
                    add_up += id
                    break
print(add_up)
