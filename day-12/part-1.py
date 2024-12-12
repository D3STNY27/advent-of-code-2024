import os
os.system('cls')


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
PERIMETER_ADJACENT_MAP = {
    0: 4,
    1: 3,
    2: 2,
    3: 1,
    4: 0
}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_perimeter_count(adjacent_count: int):
    return PERIMETER_ADJACENT_MAP[adjacent_count]


def solution(lines: list[str]):
    plant_set = set()

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            plant_set.add((r, c))
    
    
    total_price = 0

    while plant_set:
        search_plant = plant_set.pop()
        queue = [search_plant]
        visited = set()

        # DFS (Find All Adjacent Nodes)
        while queue:
            r, c = queue[-1]
            queue = queue[:-1]
            plant = lines[r][c]

            visited.add((r, c))

            for direction in DIRECTIONS:
                step_r, step_c = direction
                r_n, c_n = (r + step_r, c + step_c)

                if r_n < 0 or r_n >= len(lines) or c_n < 0 or c_n >= len(lines[0]):
                    continue

                if lines[r_n][c_n] != plant:
                    continue

                if (r_n, c_n) in visited:
                    continue

                queue.append((r_n, c_n))
        

        # Calculate Boundry
        area = len(visited)
        perimeter = 0

        for r, c in visited:
            adj_count = 0
            for direction in DIRECTIONS:
                step_r, step_c = direction
                r_n, c_n = (r + step_r, c + step_c)

                if (r_n, c_n) in visited:
                    adj_count += 1
            
            perimeter += get_perimeter_count(adj_count)
        
        
        # Calculate Price
        total_price += (area * perimeter)
    
        
        # Remove Region From Search Set
        for plant in list(visited):
            if plant==search_plant:
                continue

            plant_set.remove(plant)
        

    print(total_price)


lines = read_input_file(file_path="input.txt")
solution(lines)