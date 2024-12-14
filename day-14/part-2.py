import os
from time import sleep

os.system('cls')


# Simulate Periodicity (Patterns Repeat After This)
MAX_SIMULATE_SECONDS = 10404
MAX_H = 103
MAX_W = 101

# MAX_H = 7
# MAX_W = 11

MID_H = MAX_H // 2
MID_W = MAX_W // 2


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_quadrant(x: int, y: int):
    if x == MID_W:
        return
    
    if y == MID_H:
        return
    
    if y < MID_H:
        if x < MID_H:
            return 1
        else:
            return 2
    else:
        if x < MID_H:
            return 3
        else:
            return 4


def solution(lines: list[str]):
    patterns = []

    for simulate_seconds in range(1, MAX_SIMULATE_SECONDS+1):
        robot_positions = set()
        for line in lines:
            tokens = [tuple(map(int, token[2:].split(','))) for token in line.split(' ')]
            p, v = tokens
            
            p_x, p_y = p
            v_x, v_y = v

            p_xn = (p_x + (v_x * simulate_seconds)) % MAX_W
            p_yn = (p_y + (v_y * simulate_seconds)) % MAX_H

            robot_positions.add((p_xn, p_yn))
        
        out_str = ''
        for x in range(MAX_W):
            for y in range(MAX_H):
                if (x, y) in robot_positions:
                    out_str += '#'
                else:
                    out_str += '.'
            out_str += '\n'
        
        patterns.append((simulate_seconds, out_str))
    
    with open('patterns.txt', 'w') as out_file:
        for pattern in patterns:
            time, out_str = pattern
            out_file.write(f'{time}\n')
            out_file.write(f'{out_str}\n')


lines = read_input_file(file_path="input.txt")
solution(lines)