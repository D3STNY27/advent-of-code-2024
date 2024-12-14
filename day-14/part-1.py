import os
os.system('cls')


SIMULATE_SECONDS = 100
MAX_H = 103
MAX_W = 101

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
    quadrant_counts = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    for line in lines:
        tokens = [tuple(map(int, token[2:].split(','))) for token in line.split(' ')]
        p, v = tokens
        
        p_x, p_y = p
        v_x, v_y = v

        p_xn = (p_x + (v_x * SIMULATE_SECONDS)) % MAX_W
        p_yn = (p_y + (v_y * SIMULATE_SECONDS)) % MAX_H

        quadrant = get_quadrant(p_xn, p_yn)
        if quadrant is None:
            continue

        quadrant_counts[quadrant] += 1
    
    safety_factor  = 1
    for value in quadrant_counts.values():
        safety_factor *= value

    print(safety_factor)


lines = read_input_file(file_path="input.txt")
solution(lines)