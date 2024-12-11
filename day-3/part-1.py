import os
import re
os.system('cls')


MUL_REGEX = r"mul\([0-9]+,[0-9]+\)"


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        line = input_file.read()
        return line


def solution(line: str):
    groups = re.findall(MUL_REGEX, line)
    
    total_sum = 0
    for group in groups:
        print(group)
        X, Y = tuple(map(int, group[4:-1].split(',')))
        total_sum += (X * Y)
    
    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)