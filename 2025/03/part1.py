data = 'input.txt'

try:
    with open(data, 'r') as f:
        output_joltaje = 0
        for line in f:
            bank = line.strip()
            first_num = max(bank[:-1])
            first_num_idx = bank.index(first_num)
            second_num = max(bank[first_num_idx + 1 :])
            output_joltaje += int(first_num + second_num)
        print(output_joltaje)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
