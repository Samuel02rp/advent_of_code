data = 'input.txt'

try:
    with open(data) as f:
        ADD = '+'
        MULT = '*'
        EMPTY = ' '

        nums = []
        totals = []
        for line in f:
            if ADD in line:
                operators = line
            else:
                nums.append(line)
        currnt_op = operators[0]  # type: ignore
        num_lenght = 1
        for column, op in enumerate(operators[1:], 1):  # type: ignore
            to_operate = []
            if op == EMPTY:
                num_lenght += 1
            else:
                for num_idx, order in enumerate(
                    range(column - 1, column - num_lenght - 1, -1)
                ):
                    char = ''
                    for row in range(len(nums)):
                        num = nums[row][order]
                        char += num if num != EMPTY else ''
                    if char.isdigit():
                        to_operate.append(char)
                total_sum = 0
                total_mult = 1
                match currnt_op:
                    case '+':
                        total_sum = sum(map(int, to_operate))
                    case '*':
                        for n in to_operate:
                            total_mult *= int(n)
                totals.append(total_sum if total_sum != 0 else total_mult)
                num_lenght = 1
                currnt_op = op
            print(to_operate)
        print(sum(totals))
except FileNotFoundError:
    print(f'Error: file {data} not found.')
