import os
from time import perf_counter
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
    
    
    path, index_map = [], {}
    queue = [(start_position, 0)]

    while queue:
        position, index = queue.pop()

        index_map[position] = index
        path.append(position)

        if position == end_position:
            break

        r, c = position

        for direction in DIRECTIONS:
            step_r, step_c = direction
            r_n, c_n = (r + step_r), (c + step_c)

            if r_n < 0 or r_n >= len(lines) or c_n < 0 or c_n >= len(lines[0]):
                continue

            if lines[r_n][c_n]=='#':
                continue

            if (r_n, c_n) in index_map:
                continue

            queue.append(((r_n, c_n), index + 1))
    

    total_picoseconds = len(path) - 1


    # Find Cheats
    total_count = 0

    for i in range(len(path)-1):
        for j in range(i+1, len(path)):
            node_a, node_b = path[i], path[j]
            distance = abs(node_a[0] - node_b[0]) + abs(node_a[1] - node_b[1])

            if distance > 20:
                continue
            
            cheat_picoseconds = (i + 1) + distance + (total_picoseconds - j - 1)
            saved_picoseconds = (total_picoseconds - cheat_picoseconds)

            if saved_picoseconds < 100:
                continue

            total_count += 1
    
    print(total_count)


lines = read_input_file(file_path="input.txt")
solution(lines)