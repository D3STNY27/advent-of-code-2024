import os
os.system('cls')


MAX_GRID = 71
SIMULATE_BYTES = 1024
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    falling_bytes = [tuple(map(int, byte.split(','))) for byte in lines]
    corrupted_bytes = set(falling_bytes[:SIMULATE_BYTES])

    start_position = (0, 0)
    end_position = (MAX_GRID-1, MAX_GRID-1)

    visited = set()
    queue = [(start_position, (1, 0), 0), (start_position, (0, 1), 0)]

    while queue:
        current_position, current_direction, steps = queue.pop(0)
        visited.add(current_position)

        if current_position==end_position:
            print(steps)
            break

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

            queue.append(item)


lines = read_input_file(file_path="input.txt")
solution(lines)