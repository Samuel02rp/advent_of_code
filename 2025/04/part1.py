data = 'input.txt'


def accessible_rolls(*, top_row, current_row, next_row):
    pos_idx = -1
    total = 0
    all_adjacent_pos = ''
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
        total += sum(pos == ROLL for pos in all_adjacent_pos) < MAX_ADJACENT
    return total


try:
    with open(data, 'r') as f:
        ROLL = '@'
        EMPTY = '.'
        MAX_ADJACENT = 4

        top_row = None
        current_row = f.readline().strip()
        next_row = None
        total = 0
        for row in f:
            next_row = row.strip()
            total += accessible_rolls(
                top_row=top_row, current_row=current_row, next_row=next_row
            )
            top_row = current_row
            current_row = next_row
        total += accessible_rolls(top_row=top_row, current_row=current_row, next_row='')
        print(total)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
