import os
os.system('cls')


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    start_positions = []
    rating_map = {}

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c]=='9':
                start_positions.append((r, c))
            if lines[r][c]=='0':
                rating_map[(r, c)] = []
    
    for start_position in start_positions:
        queue = [(start_position, [])]

        while queue:
            (r, c), path = queue[-1]
            queue = queue[:-1]

            if lines[r][c]=='0':
                rating_map[(r, c)].append(path)
                continue
        
            for direction in DIRECTIONS:
                step_r, step_c = direction
                r_n, c_n = (r + step_r, c + step_c)

                if r_n < 0 or r_n >= len(lines) or c_n < 0 or c_n >= len(lines[0]):
                    continue

                if int(lines[r_n][c_n]) != int(lines[r][c])-1:
                    continue

                queue.append(((r_n, c_n), path + [(r_n, c_n)]))
    
    total_rating = 0
    for _, value in rating_map.items():
        total_rating += len(value)
    
    print(total_rating)


lines = read_input_file(file_path="input.txt")
solution(lines)