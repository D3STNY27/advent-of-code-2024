import os
os.system('cls')


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
XMAS_TOKENS = ['X', 'M', 'A', 'S']


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_xmas_count(position: tuple, lines: list[str]):
    count = 0
    r, c = position
    R, C = len(lines), len(lines[0])

    for dir in DIRECTIONS:
        x_dir, y_dir = dir

        for step in range(0, len(XMAS_TOKENS)):
            x, y = (r + step*x_dir), (c + step*y_dir)
            if x < 0 or x >= R or y < 0 or y >= C:
                break

            if XMAS_TOKENS[step] != lines[x][y]:
                break

            if step==len(XMAS_TOKENS)-1:
                count += 1

    return count


def solution(lines: str):
    total_count = 0
    x_positions = []

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c]=='X':
                x_positions.append((r, c))
    
    for pos in x_positions:
        total_count += get_xmas_count(pos, lines)
    
    print(total_count)


lines = read_input_file(file_path="input.txt")
solution(lines)