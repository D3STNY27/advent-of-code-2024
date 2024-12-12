import os
os.system('cls')


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]
    

def get_turn_contribution_pairs(point: tuple, adjacent_nodes: list[tuple], nodes: set):
    (r_a, c_a), (r_b, c_b) = adjacent_nodes[0], adjacent_nodes[1]
    (r, c) = point

    if r_a==r_b or c_a==c_b:
        return 0

    if r_a==r and (r_b, c_a) in nodes:
        return 1

    if r_b==r and (r_a, c_b) in nodes:
        return 1

    if r_a==r and (r_b, c_a) not in nodes:
        return 2

    if r_b==r and (r_a, c_b) not in nodes:
        return 2
    
    return 0


# Ignore 1 Turn For Multiple Pairs
def get_turn_contribution_multiple_pairs(point: tuple, adjacent_nodes: list[tuple], nodes: set):
    (r_a, c_a), (r_b, c_b) = adjacent_nodes[0], adjacent_nodes[1]
    (r, c) = point

    if r_a==r_b or c_a==c_b:
        return 0

    if r_a==r and (r_b, c_a) in nodes:
        return 0

    if r_b==r and (r_a, c_b) in nodes:
        return 0

    if r_a==r and (r_b, c_a) not in nodes:
        return 1

    if r_b==r and (r_a, c_b) not in nodes:
        return 1
    
    return 0


def get_perimeter(nodes: list[tuple]):
    perimeter = 0

    for r, c in nodes:
        adj_nodes = []
        for direction in DIRECTIONS:
            step_r, step_c = direction
            r_n, c_n = (r + step_r, c + step_c)

            if (r_n, c_n) in nodes:
                adj_nodes.append((r_n, c_n))
        
        # Turns Contribution
        if len(adj_nodes)==0:
            perimeter += 4

        elif len(adj_nodes)==1:
            perimeter += 2

        elif len(adj_nodes)==2:
            perimeter += get_turn_contribution_pairs((r, c), adj_nodes, nodes)
        
        else:
            for i in range(len(adj_nodes)-1):
                for j in range(i, len(adj_nodes)):
                    perimeter += get_turn_contribution_multiple_pairs((r, c), [adj_nodes[i], adj_nodes[j]], nodes)
        
    return perimeter


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
        perimeter = get_perimeter(visited)
        
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