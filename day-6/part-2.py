import os
os.system('cls')


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: str):
    lines = [list(line) for line in lines]

    guard_pos = None
    visited = set()
    direction_idx = 0
    R, C = len(lines), len(lines[0])

    for r in range(len(lines)):
        try:
            c = lines[r].index('^')
            guard_pos = (r, c)
            break
        except ValueError as e:
            continue

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
    
    loop_count = 0
    for r, c in visited:
        if (r, c)==guard_pos:
            continue

        previous_char = lines[r][c]
        lines[r][c] = '#'
        loop = set()
        direction_idx = 0

        queue = [guard_pos]
        while queue:
            (rs, cs) = queue[-1]
            queue = queue[:-1]

            if (rs, cs, direction_idx) in loop:
                loop_count += 1
                break

            loop.add((rs, cs, direction_idx))

            for idx in range(direction_idx, direction_idx+4):
                x, y = DIRECTIONS[idx  % len(DIRECTIONS)]
                rn, cn = (rs + x), (cs + y)

                if rn < 0 or rn >= R or cn < 0 or cn >= C:
                    break

                if lines[rn][cn]=='#':
                    continue

                queue.append((rn, cn))
                direction_idx = (idx % len(DIRECTIONS))
                break

        lines[r][c] = previous_char
    
    print(loop_count)


lines = read_input_file(file_path="input.txt")
solution(lines)