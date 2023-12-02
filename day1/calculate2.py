import re

with open('calibrations.txt') as calibrations:
    data = calibrations.read().splitlines()
    total = 0
    num = 1
    nums_to_replace = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'}
    for line in data:

        print(f'Old line: {line}')
        
        for key, value in nums_to_replace.items():
            line = line.replace(key, value)
        
        print(f'Converted: {line}')
        
        nums_in_line = list(filter(lambda x: x.isdigit(), line))
        first_num = nums_in_line[0]
        last_num = nums_in_line[-1]

        print(f'numbers in line {nums_in_line}')
                
        if len(nums_in_line) >= 2:
            sum = first_num + last_num
            total = int(sum) + total
            print(f'calibration: {sum}')
        else:
            sum = first_num + first_num
            total = int(sum) + total
            print(f'calibration: {sum}')

    print(f'The total is {total}')
