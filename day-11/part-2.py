import os
from functools import cache

os.system('cls')


BLINKS = 75


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        line = input_file.read()
        return line
    

@cache
def get_number_of_stones(stone: int, num_blinks: int):
    if num_blinks==0:
        return 1
    
    if stone==0:
        return get_number_of_stones(1, num_blinks-1)
    
    stone_str = str(stone)
    stone_len = len(stone_str)
    stone_len_half = stone_len // 2

    if stone_len % 2 == 0:
        return (
            get_number_of_stones(int(stone_str[:stone_len_half]), num_blinks-1) +
            get_number_of_stones(int(stone_str[stone_len_half:]), num_blinks-1)
        )
    
    return get_number_of_stones(stone * 2024, num_blinks-1)



def solution(line: str):
    stones = [stone for stone in line.split()]
    total_stones = sum([get_number_of_stones(int(stone), BLINKS) for stone in stones])
    print(total_stones)


lines = read_input_file(file_path="input.txt")
solution(lines)

print(get_number_of_stones.cache_info())