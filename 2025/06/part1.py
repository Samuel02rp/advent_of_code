data = 'input.txt'

try:
    with open(data) as f:
        ADD = '+'

        nums = []
        totals = []
        for line in f:
            if ADD in line:
                operators = line.strip().split()
            else:
                nums.append(list(map(int, line.strip().split())))
        for column, op in enumerate(operators):  # type: ignore
            total_sum = 0
            total_mult = 1
            for row in range(len(nums)):
                match op:
                    case '+':
                        total_sum += nums[row][column]
                    case '*':
                        total_mult *= nums[row][column]
            totals.append(total_sum if total_sum != 0 else total_mult)
        print(sum(totals))
except FileNotFoundError:
    print(f'Error: file {data} not found.')
