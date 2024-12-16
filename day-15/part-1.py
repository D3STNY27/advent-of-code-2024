import os
os.system('cls')


DIRECTION_MAP = {
    '<': (0, -1),
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0)
}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    divider = lines.index('')
    
    grid = lines[:divider]
    moves = ''.join(lines[divider+1:])

    robot_position, grid_map = None, {}

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c]=='@':
                robot_position = (r, c)
                grid_map[(r, c)] = '.'
            else:
                grid_map[(r, c)] = grid[r][c]
    
    for move in moves:
        step_r, step_c = DIRECTION_MAP[move]
        r, c = robot_position

        r_n, c_n = (r + step_r), (c + step_c)
        if r_n < 0 or r_n >= len(grid) or c_n < 0 or c_n >= len(grid[0]):
            continue

        if grid_map[(r_n, c_n)]=='#':
            continue

        if grid_map[(r_n, c_n)]=='.':
            robot_position = (r_n, c_n)
            continue

        boxes, steps = [], 0
        position_found = False
        while True:
            r_s, c_s = (r_n + step_r * steps), (c_n + step_c * steps)

            if r_s < 0  or r_s >= len(grid) or c_s < 0 or c_s >= len(grid[0]):
                break

            if grid_map[(r_s, c_s)]=='.':
                position_found = True
                break

            if grid_map[(r_s, c_s)]=='#':
                break

            boxes.append((r_s, c_s))
            steps += 1
        
        if not position_found:
            continue

        for (r_b, c_b) in boxes:
            grid_map[(r_b, c_b)] = '.'

        for (r_b, c_b) in boxes:
            grid_map[(r_b + step_r, c_b + step_c)] = 'O'
        
        robot_position = (r_n, c_n)

    
    gps_sum = 0
    for key, val in grid_map.items():
        if val!='O':
            continue

        r, c = key
        gps_sum += ((100 * r) + c)
    
    print(gps_sum)
    

lines = read_input_file(file_path="input.txt")
solution(lines)