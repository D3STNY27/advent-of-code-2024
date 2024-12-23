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


    seen_sets = set()
    max_length = float('-inf')
    max_length_set = None
    

    for computer in computers:
        queue = [(1, computer, [computer])]

        while queue:
            num_connections, node, connections = queue.pop(-1)
            seen_sets.add(tuple(sorted(connections)))

            if len(connections) > max_length:
                max_length = len(connections)
                max_length_set = connections

            for neighbour in lan_connections[node]:
                is_connected_to_all = True

                for connection in connections:
                    if neighbour not in lan_connections[connection]:
                        is_connected_to_all = False
                        break

                if is_connected_to_all:
                    if tuple(sorted(connections + [neighbour])) in seen_sets:
                        continue

                    queue.append((num_connections + 1, neighbour, connections + [neighbour]))
    
    print(','.join(sorted(max_length_set)))


lines = read_input_file(file_path="input.txt")
solution(lines)