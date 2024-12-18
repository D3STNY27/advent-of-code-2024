import os
os.system('cls')


MAX_GRID = 71
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def construct_path(came_from: dict, position: tuple, direction: tuple):
    path = [position]

    while True:
        if (position, direction) not in came_from:
            break

        position, direction = came_from[(position, direction)]
        path.insert(0, position)

    return path



def find_minimum_steps_path(corrupted_bytes: set):
    start_position = (0, 0)
    end_position = (MAX_GRID-1, MAX_GRID-1)

    visited = set()
    came_from = {}
    queue = [(start_position, (1, 0), 0), (start_position, (0, 1), 0)]

    while queue:
        current_position, current_direction, steps = queue.pop(0)
        visited.add(current_position)

        if current_position==end_position:
            return True, construct_path(
                came_from=came_from,
                position=current_position,
                direction=current_direction
            )

        x, y = current_position

        for direction in DIRECTIONS:
            step_x, step_y = direction
            x_n, y_n = (x + step_x), (y + step_y)

            if x_n < 0 or x_n >= MAX_GRID or y_n < 0 or y_n >= MAX_GRID:
                continue

            if current_direction[0] * step_x + current_direction[1] * step_y < 0:
                continue

            if (x_n, y_n) in visited:
                continue

            if (x_n, y_n) in corrupted_bytes:
                continue

            item = ((x_n, y_n), direction, steps + 1)
            if item in queue:
                continue

            came_from[((x_n, y_n), direction)] = (current_position, current_direction)
            queue.append(item)
    
    return False, []


def solution(lines: list[str]):
    falling_bytes = [tuple(map(int, byte.split(','))) for byte in lines]
    previous_path = set()

    for simulate_bytes in range(1, len(falling_bytes)+1):
        corrupted_bytes = set(falling_bytes[:simulate_bytes])
        added_byte = falling_bytes[simulate_bytes-1]
        
        if len(previous_path)==0:
            is_valid, path = find_minimum_steps_path(corrupted_bytes=corrupted_bytes)
            if not is_valid:
                continue

            previous_path = set(path)
        else:
            if added_byte not in previous_path:
                continue

            is_valid, path = find_minimum_steps_path(corrupted_bytes=corrupted_bytes)
            if not is_valid:
                print(added_byte)
                break

            previous_path = set(path)


lines = read_input_file(file_path="input.txt")
solution(lines)