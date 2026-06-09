data = 'input.txt'


def merge_ranges(ranges: list) -> list:
    ranges.sort(key=lambda r: r.start)
    merged = [ranges[0]]
    for r in ranges[1:]:
        last = merged[-1]
        if r.start < last.stop:
            merged[-1] = range(last.start, max(last.stop, r.stop))
        else:
            merged.append(r)
    return merged


try:
    with open(data) as f:
        SEP = '-'
        ranges = []
        for line in f:
            if SEP in line:
                floor, ceiling = map(int, line.strip().split(SEP))
                ranges.append(range(floor, ceiling + 1))
            else:
                break
        ranges = merge_ranges(ranges)
        num_fresh_ids = sum(len(r) for r in ranges)
        print(num_fresh_ids)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
