import os
os.system('cls')


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    start_position, end_position = None, None

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c]=='S':
                start_position = (r, c)
            
            if lines[r][c]=='E':
                end_position = (r, c)
    
    
    path, visited = [], set()
    queue = [start_position]

    while queue:
        position = queue.pop()

        visited.add(position)
        path.append(position)

        r, c = position

        for direction in DIRECTIONS:
            step_r, step_c = direction
            r_n, c_n = (r + step_r), (c + step_c)

            if r_n < 0 or r_n >= len(lines) or c_n < 0 or c_n >= len(lines[0]):
                continue

            if lines[r_n][c_n]=='#':
                continue

            if (r_n, c_n) in visited:
                continue

            queue.append((r_n, c_n))
    

    total_picoseconds = len(path) - 1
    saved_picoseconds_map = {}

    # Find Cheats
    for i in range(len(path)):
        cheat_rs, cheat_cs = path[i]

        for direction in DIRECTIONS:
            step_r, step_c = direction

            cheat_rm, cheat_cm = (cheat_rs + step_r), (cheat_cs + step_c)
            if cheat_rm < 0 or cheat_rm >= len(lines) or cheat_cm < 0 or cheat_cm >= len(lines[0]):
                continue

            if lines[cheat_rm][cheat_cm] == '.':
                continue

            cheat_re, cheat_ce = (cheat_rm + step_r), (cheat_cm + step_c)
            if cheat_re < 0 or cheat_re >= len(lines) or cheat_ce < 0 or cheat_ce >= len(lines[0]):
                continue

            if lines[cheat_re][cheat_ce] == '#':
                continue

            if (cheat_re, cheat_ce) not in visited:
                continue

            end_index = path.index((cheat_re, cheat_ce))
            if end_index < i:
                continue

            cheat_picoseconds = (i + 1) + 1 + (total_picoseconds - end_index)
            saved_picoseconds = (total_picoseconds - cheat_picoseconds)

            if saved_picoseconds not in saved_picoseconds_map:
                saved_picoseconds_map[saved_picoseconds] = 0

            saved_picoseconds_map[saved_picoseconds] += 1
    

    # Save Atleast 100 Picoseconds
    total_count = 0
    for key, value in saved_picoseconds_map.items():
        if key >= 100:
            total_count += value
    
    print(total_count)


lines = read_input_file(file_path="input.txt")
solution(lines)