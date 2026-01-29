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
        if id_[: len(id_) // 2] == id_[len(id_) // 2 :]:
            add_up += id
print(add_up)
