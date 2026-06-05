data = 'input.txt'


def accessible_rolls(
    *,
    f,
    top_row: str | None,
    current_row: str,
    next_row: str | None,
) -> int:
    pos_idx = -1
    total = 0
    all_adjacent_pos = ''
    data_to_write = current_row
    for pos in current_row:
        pos_idx += 1
        if pos == EMPTY:
            continue
        if next_row:
            all_adjacent_pos = f'{next_row[pos_idx]}'
            if pos_idx == 0:
                all_adjacent_pos += (
                    f'{current_row[pos_idx + 1]}' + f'{next_row[pos_idx + 1]}'
                )
                if top_row is not None:
                    all_adjacent_pos += f'{top_row[pos_idx]}{top_row[pos_idx + 1]}'
            elif pos_idx == len(current_row) - 1:
                all_adjacent_pos += (
                    f'{current_row[pos_idx - 1]}' + f'{next_row[pos_idx - 1]}'
                )
                if top_row is not None:
                    all_adjacent_pos += f'{top_row[pos_idx - 1]}{top_row[pos_idx]}'
            else:
                all_adjacent_pos += (
                    f'{current_row[pos_idx - 1]}{current_row[pos_idx + 1]}'
                    + f'{next_row[pos_idx - 1]}{next_row[pos_idx + 1]}'
                )
                if top_row is not None:
                    all_adjacent_pos += f'{top_row[pos_idx - 1]}{top_row[pos_idx]}{top_row[pos_idx + 1]}'
        elif top_row is not None:
            all_adjacent_pos = f'{top_row[pos_idx]}'
            if pos_idx == 0:
                all_adjacent_pos += (
                    f'{current_row[pos_idx + 1]}' + f'{top_row[pos_idx + 1]}'
                )
            elif pos_idx == len(current_row) - 1:
                all_adjacent_pos += (
                    f'{current_row[pos_idx - 1]}' + f'{top_row[pos_idx - 1]}'
                )
            else:
                all_adjacent_pos += (
                    f'{current_row[pos_idx - 1]}{current_row[pos_idx + 1]}'
                    + f'{top_row[pos_idx - 1]}{top_row[pos_idx + 1]}'
                )
        total += (
            is_accessible := sum(pos != EMPTY for pos in all_adjacent_pos)
            < MAX_ADJACENT
        )
        if is_accessible:
            data_to_write = data_to_write[:pos_idx] + EMPTY + current_row[pos_idx + 1 :]
    f.write(f'{data_to_write}\n')
    return total


def iter_file(*, to_read, to_write):
    to_read.seek(0)
    to_write.seek(0)
    total = 0
    top_row = next_row = None
    current_row = to_read.readline().strip()
    for row in to_read:
        next_row = row.strip()
        total += accessible_rolls(
            f=to_write,
            top_row=top_row,
            current_row=current_row,
            next_row=next_row,
        )
        top_row = current_row
        current_row = next_row
    total += accessible_rolls(
        f=to_write,
        top_row=top_row,
        current_row=current_row,
        next_row='',
    )
    return total


try:
    with open(data) as f, open(f'1{data}.temp', 'w+') as f1, open(
        f'2{data}.temp', 'w+'
    ) as f2:
        ROLL = '@'
        EMPTY = '.'
        MAX_ADJACENT = 4
        total = iter_file(to_read=f, to_write=f1)
        last_total = 0
        while total != last_total:
            last_total = total
            total += iter_file(to_read=f1, to_write=f2)
            f1, f2 = f2, f1
            print(last_total, total)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
