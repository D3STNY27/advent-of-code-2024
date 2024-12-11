import os
from copy import deepcopy

os.system('cls')


# ordered in 90 degree rotations
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [list(line.strip()) for line in lines]


# To-Do: Using Binary Search (Bisect) maybe...
def get_next_position(
    current_position: tuple,
    direction_index: int,
    row_map: dict[list[int]],
    column_map: dict[list[int]]
):
    row_curr, column_curr = current_position

    if direction_index==0:
        for row in column_map[column_curr][::-1]:
            if row < row_curr:
                return (row+1, column_curr)
    elif direction_index==1:
        for col in row_map[row_curr]:
            if col > column_curr:
                return (row_curr, col-1)
    elif direction_index==2:
        for row in column_map[column_curr]:
            if row > row_curr:
                return (row-1, column_curr)
    else:
        for col in row_map[row_curr][::-1]:
            if col < column_curr:
                return (row_curr, col+1)
    return None


def solution(lines: str):
    guard_position = None
    direction_idx = 0
    row_map, col_map = {}, {}

    # Pre-Processing
    for r in range(len(lines)):
        if r not in row_map:
            row_map[r] = []

        for c in range(len(lines[r])):
            if c not in col_map:
                col_map[c] = []

            if lines[r][c]=='#':
                row_map[r].append(c)
                col_map[c].append(r)
            elif lines[r][c]=='^':
                guard_position = (r, c)
            else:
                continue
    
    path = []
    position = guard_position

    path.append(position)
    while True:
        position = get_next_position(position, direction_idx, row_map, col_map)
        if position is None:
            break

        direction_idx = (direction_idx + 1) % len(DIRECTIONS)
        path.append(position)
    

    # Construct Path (Partial)
    full_path = set()
    for i in range(len(path)-1):
        node_c, node_n = path[i], path[i+1]
        if node_c[0]==node_n[0]:
            for x in range(min(node_c[1], node_n[1]), max(node_c[1], node_n[1])+1):
                full_path.add((node_c[0], x))
        else:
            for x in range(min(node_c[0], node_n[0]), max(node_c[0], node_n[0])+1):
                full_path.add((x, node_c[1]))
    

    # Remaining Path
    last_node = path[-1]
    if direction_idx==0:
        for x in range(0, last_node[0]):
            full_path.add((x, last_node[1]))
    elif direction_idx==1:
        for x in range(last_node[1]+1, len(lines[0])):
            full_path.add((last_node[0], x))
    elif direction_idx==2:
        for x in range(last_node[0]+1, len(lines)):
            full_path.add((x, last_node[1]))
    else:
        for x in range(0, last_node[1]):
            full_path.add((last_node[0], x))
    

    # Find Loops (Using Obstructions)

    # Further To-Do Optimization (skip obstructions for which guard does not reach the next obstruction
    # by checking row/column for the next path) -- but it does not reduce number of obstruction to check by a large factor
    loop_count = 0
    for r, c in full_path:
        if (r, c)==guard_position:
            continue

        row_map_mod = deepcopy(row_map)
        col_map_mod = deepcopy(col_map)

        row_map_mod[r].append(c)
        row_map_mod[r] = sorted(row_map_mod[r])

        col_map_mod[c].append(r)
        col_map_mod[c] = sorted(col_map_mod[c])
        
        position = guard_position
        direction_idx = 0
        visited = set()

        while True:
            position = get_next_position(position, direction_idx, row_map_mod, col_map_mod)
            if position is None:
                break

            if (*position, direction_idx) in visited:
                loop_count += 1
                break

            visited.add((*position, direction_idx))
            direction_idx = (direction_idx + 1) % len(DIRECTIONS)
    

    print(loop_count)


lines = read_input_file(file_path="input.txt")
solution(lines)
