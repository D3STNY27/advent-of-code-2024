import os
os.system('cls')


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def check_validity(test_value: int, values: list[int], current_eval: int, index: int):
    if index==len(values)-1:
        return test_value==current_eval

    if current_eval > test_value:
        return False
    
    valid_add = check_validity(test_value, values, current_eval + values[index+1], index+1)
    valid_mul = check_validity(test_value, values, current_eval * values[index+1], index+1)
    return valid_add or valid_mul


def solution(lines: str):
    total_sum = 0

    for line in lines:
        test_value, raw_equation = line.split(':')

        test_value = int(test_value)
        values = list(map(int, raw_equation.split()))
        
        valid = check_validity(test_value, values, values[0], 0)
        if not valid:
            continue

        total_sum += test_value

    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)