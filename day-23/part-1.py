import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    lan_connections = {}
    computers = set()

    for connection in lines:
        computer_a, computer_b = connection.split('-')
        
        if computer_a not in lan_connections:
            lan_connections[computer_a] = set()

        if computer_b not in lan_connections:
            lan_connections[computer_b] = set()
        
        lan_connections[computer_b].add(computer_a)
        lan_connections[computer_a].add(computer_b)

        computers.add(computer_a)
        computers.add(computer_b)

    
    three_sets = set()
    
    for computer in computers:
        queue = [(computer, set())]

        while queue:
            node, visited = queue.pop(-1)
            visited.add(node)

            if len(visited) > 3:
                continue

            for neighbour in lan_connections[node]:
                if neighbour in visited:
                    if len(visited)==3 and neighbour==computer:
                        sorted_names = sorted(visited)
                        contains_cheif = False

                        for name in sorted_names:
                            if name[0]=='t':
                                contains_cheif = True
                                break
                        
                        if contains_cheif:
                            three_sets.add(tuple(sorted_names))
                    continue

                queue.append((neighbour, visited.copy()))
    
    print(len(three_sets))


lines = read_input_file(file_path="input.txt")
solution(lines)