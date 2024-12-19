import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def is_possible_design(design: str, towels_map: dict):
    queue = [(0, [])]

    while queue:
        current_index, history = queue[-1]
        queue = queue[:-1]

        current_design = ''.join(history)
        if current_design == design:
            return True

        if current_index >= len(design):
            continue

        current_character = design[current_index]
        if current_character not in towels_map:
            continue

        for prefix in towels_map[current_character]:
            prefix_len = len(prefix)
            if design[current_index:current_index + prefix_len] != prefix:
                continue

            item = (current_index + len(prefix), history + [prefix])
            if item in queue:
                continue

            queue.append(item)
    
    return False


def solution(lines: list[str]):
    towels = [towel.strip() for towel in lines[0].split(',')]
    designs = lines[2:]

    towels_map = {}
    for towel in towels:
        first_character = towel[0]

        if first_character not in towels_map:
            towels_map[first_character] = []

        towels_map[first_character].append(towel)

    
    possible_designs = 0

    for design in designs:
        is_possible = is_possible_design(design, towels_map)

        if not is_possible:
            continue

        possible_designs += 1
    
    print(possible_designs)


lines = read_input_file(file_path="input.txt")
solution(lines)