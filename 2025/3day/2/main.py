data = 'input.txt'

try:
    # TODO
    with open(data, 'r') as file:
        TARGET_LEN = 12
        output_joltaje = 0
        for line in file:
            bank = list(line.strip())
            bank_output_joltaje = ''
            n_num = last_num = bank[0]
            n_num_idx = aux_idx = 0
            for n in range(TARGET_LEN):
                if n != TARGET_LEN - 1:
                    for num in bank[n_num_idx + 1 : 1 + n - 12]:
                        aux_idx += 1
                        if int(num) > int(n_num):
                            n_num = last_num = num
                else:
                    for num in bank[n_num_idx + 1 :]:
                        if int(num) > int(n_num):
                            n_num = num
                bank_output_joltaje += bank.pop()
            output_joltaje += int(bank_output_joltaje)
        print(output_joltaje)
except FileNotFoundError:
    print(f'Error: the file {data} was not found.')
