data = 'input.txt'

try:
    with open(data, 'r') as f:
        TARGET_LEN = 12
        output_joltaje = 0
        for line in f:
            bank = line.strip()
            bank_output_joltaje = ''
            for idx in range(TARGET_LEN - 1, 0, -1):
                num = max(bank[:-idx])
                bank_output_joltaje += str(num)
                num_idx = bank.index(num)
                bank = bank[num_idx + 1 :]
            num = max(bank)
            bank_output_joltaje += str(num)
            output_joltaje += int(bank_output_joltaje)
        print(output_joltaje)
except FileNotFoundError:
    print(f'Error: file {data} not found.')
