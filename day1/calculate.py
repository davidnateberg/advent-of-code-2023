with open('calibrations.txt') as calibrations:
    data = calibrations.read().splitlines()
    total = 0
    for line in data:
        num_in_line = list(filter(lambda x: x.isdigit(), line))
        first_num = num_in_line[0]
        last_num = num_in_line[-1]
        if len(num_in_line) >= 2:
            sum = first_num + last_num
            total = int(sum) + total
        else:
            sum = first_num + first_num
            total = int(sum) + total
    print(f'The total is {total}')
