with open('calibrations.txt') as calibrations:
    data = calibrations.read().splitlines()
    total = 0
    data_cleaned = []

    nums_to_replace = {
        'one': 'o1e', 
        'two': 't2o', 
        'three': '3', 
        'four': '4', 
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    line_number = 1
    for line in data:
        
        for key, value in nums_to_replace.items():
            line = line.replace(key, value)
    
        line_number = line_number + 1
        print(f'line number {line_number}')    
        only_numbers = list(filter(lambda x: x.isdigit(), line))
        data_cleaned.append(only_numbers)

    print(data_cleaned)

    line_number = 1
    for line in data_cleaned:
        print(f'--line number {line_number}--')
        
        first_num = line[0]
        last_num = line[-1]
                
        if len(line) >= 2:
            sum = first_num + last_num
            total = int(sum) + total
            print(line)
            print(f'calibration: {sum}')
            line_number = line_number + 1
        else:
            sum = first_num + first_num
            total = int(sum) + total
            print(f'calibration: {sum}')
            line_number = line_number + 1

    print(f'The total is {total}')
