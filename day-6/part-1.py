import os
os.system('cls')


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: str):
    guard_pos = None
    visited = set()
    direction_idx = 0
    R, C = len(lines), len(lines[0])

    for r in range(len(lines)):
        c = lines[r].find('^')
        if c == -1:
            continue

        guard_pos = (r, c)
    
    
    queue = [guard_pos]
    while queue:
        (r, c) = queue[-1]
        queue = queue[:-1]

        visited.add((r, c))
        for idx in range(direction_idx, direction_idx+4):
            x, y = DIRECTIONS[idx  % len(DIRECTIONS)]
            rn, cn = (r + x), (c + y)

            if rn < 0 or rn >= R or cn < 0 or cn >= C:
                break

            if lines[rn][cn]=='#':
                continue

            queue.append((rn, cn))
            direction_idx = (idx % len(DIRECTIONS))
            break
    
    print(len(visited))


lines = read_input_file(file_path="input.txt")
solution(lines)