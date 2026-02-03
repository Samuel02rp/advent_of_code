data = 'input.txt'

try:
    with open(data, 'r') as f:
        list1 = []
        list2 = []
        for line in f:
            line = line.strip().split()
            if len(line) == 2:
                list1.append(line[0])
                list2.append(line[1])
            else:
                print('Formato de datos no esperado')
        list1.sort()
        list2.sort()
        diff = 0
        for index in range(len(list1)):
            diff += abs(int(list1[index]) - int(list2[index]))
        print(diff)
except FileNotFoundError:
    print(f'Error: the file {data} was not found.')
