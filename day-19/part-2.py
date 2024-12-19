import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_possible_designs(design: str, towels_map: dict, cache: dict):
    if design=='':
        return 1
    
    first_character = design[0]
    if first_character not in towels_map:
        return 0
    
    possible_prefixes = towels_map[first_character]
    number_of_ways = 0

    for prefix in possible_prefixes:
        if prefix != design[:len(prefix)]:
            continue

        remaining_design = design[len(prefix):]
        if remaining_design not in cache:
            cache[remaining_design] = get_possible_designs(remaining_design, towels_map, cache)
        
        number_of_ways += cache[remaining_design]
    
    return number_of_ways


def solution(lines: list[str]):
    towels = [towel.strip() for towel in lines[0].split(',')]
    designs = lines[2:]

    towels_map = {}
    for towel in towels:
        first_character = towel[0]

        if first_character not in towels_map:
            towels_map[first_character] = []

        towels_map[first_character].append(towel)

    
    different_ways = 0

    for design in designs:
        number_of_ways = get_possible_designs(design, towels_map, {})
        different_ways += number_of_ways

    
    print(different_ways)


lines = read_input_file(file_path="input.txt")
solution(lines)