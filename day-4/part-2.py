import os
os.system('cls')


# Order Matters
PATTERN_POS = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]

# Patterns
XMAS_SET = {'MSAMS', 'SSAMM', 'SMASM', 'MMASS'}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def is_mas_pattern(position: tuple, lines: list[str]):
    r, c = position
    R, C = len(lines), len(lines[0])

    pattern = ''
    for step in PATTERN_POS:
        x, y = (r + step[0]), (c + step[1])
        if x < 0 or x >= R or y < 0 or y >= C:
            return False

        pattern += lines[x][y]
    
    return True if pattern in XMAS_SET else False


def solution(lines: str):
    total_count = 0
    m_positions = []

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] in {'M', 'S'}:
                m_positions.append((r, c))
    
    for pos in m_positions:
        if not is_mas_pattern(pos, lines):
            continue

        total_count += 1
    
    print(total_count)


lines = read_input_file(file_path="input.txt")
solution(lines)