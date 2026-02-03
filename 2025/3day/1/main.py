data = 'input.txt'

try:
    with open(data, 'r') as file:
        output_joltaje = 0
        for line in file:
            bank = line.strip()
            first_num = bank[0]
            for num in bank[1:-1]:
                if int(num) > int(first_num):
                    first_num = num
            first_num_idx = bank.index(first_num)
            second_num = bank[first_num_idx + 1]
            for num in bank[first_num_idx + 1 :]:
                if int(num) > int(second_num):
                    second_num = num
            output_joltaje += int(first_num + second_num)
        print(output_joltaje)
except FileNotFoundError:
    print(f'Error: the file {data} was not found.')
