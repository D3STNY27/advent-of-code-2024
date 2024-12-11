import os
import re
os.system('cls')


MAX_MUL_LEN = 12


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        line = input_file.read()
        return line


def check_and_get_mul(group: str):
    if group[:4] != 'mul(':
        return False, None, None

    comma_idx = group.find(',')
    close_bracket_idx = group.find(')')

    if comma_idx==-1 or close_bracket_idx==-1:
        return False, None, None

    X, Y = group[4:comma_idx], group[comma_idx+1:close_bracket_idx]
    if not X.isdigit() or not Y.isdigit():
        return False, None, None
    
    return True, len(group[:close_bracket_idx+1]), (int(X), int(Y))


def solution(line: str):
    idx = 0
    total_sum = 0
    mul_enable = True

    while idx < len(line):
        if line[idx]=='m':
            status, shift, nums = check_and_get_mul(line[idx:idx+MAX_MUL_LEN])
            if status:
                X, Y = nums
                if mul_enable:
                    total_sum += (X * Y)
                idx += shift
                continue
        elif line[idx]=='d':
            if line[idx:idx+4]=='do()':
                mul_enable = True
                idx += 4
                continue
            elif line[idx:idx+7]=="don't()":
                mul_enable = False
                idx += 7
                continue
        idx += 1

    print(total_sum)

lines = read_input_file(file_path="input.txt")
solution(lines)
