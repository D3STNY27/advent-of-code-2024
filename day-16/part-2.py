import os
from queue import PriorityQueue
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
    
    
    came_from = {}
    init_direction = (0, 1)
    g_score = {(start_position, init_direction): 0}
    points_path_map = {}

    queue = PriorityQueue()
    queue.put(item=(0, start_position, init_direction, [start_position]))

    while not queue.empty():
        points, current_position, current_direction, path = queue.get()
        if current_position == end_position:

            if points not in points_path_map:
                points_path_map[points] = []

            points_path_map[points].append(path)

        r, c = current_position
        for next_direction in DIRECTIONS:
            step_r, step_c = next_direction
            r_n, c_n = (r + step_r), (c + step_c)

            if r_n < 0 or r_n >= len(lines) or c_n < 0 or c_n >= len(lines[0]):
                continue

            if lines[r_n][c_n]=='#':
                continue

            if step_r * current_direction[0] + step_c * current_direction[1] < 0:
                continue

            cost = 1 if current_direction == next_direction else 1001
            tentative_g_score = g_score[(current_position, current_direction)] + cost

            if ((r_n, c_n), next_direction) not in g_score:
                g_score[((r_n, c_n), next_direction)] = float('inf')

            
            if tentative_g_score <= g_score[((r_n, c_n), next_direction)]:
                came_from[((r_n, c_n), next_direction)] = (current_position, current_direction)
                g_score[((r_n, c_n), next_direction)] = tentative_g_score
                queue.put(item=(points + cost, (r_n, c_n), next_direction, path + [(r_n, c_n)]))
    

    min_score = min(points_path_map.keys())
    paths = points_path_map[min_score]
    tiles = set()

    for path in paths:
        for tile in path:
            tiles.add(tile)
    
    print(len(tiles))


lines = read_input_file(file_path="input.txt")
solution(lines)