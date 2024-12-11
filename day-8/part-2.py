import os
os.system('cls')


MAX_ANTENNAS_GENERATE = 100


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_antinode_positions(position_a: tuple, position_b: tuple):
    antinodes = []
    (r1, c1), (r2, c2) = position_a, position_b

    # Slope = Infinity
    if c1==c2:
        v_d = abs(r1 - r2)
        for step in range(0, MAX_ANTENNAS_GENERATE):
            antinodes.append((min(r1, r2) - step * v_d, c1))
            antinodes.append((max(r1, r2) + step * v_d, c1))
    # Slope = 0
    elif r1==r2:
        h_d = abs(c1 - c2)
        for step in range(0, MAX_ANTENNAS_GENERATE):
            antinodes.append((r1, min(c1, c2) - step * h_d))
            antinodes.append((r1, max(c1, c2) + step * h_d))
    else:
        slope = (r2 - r1) / (c2 - c1)
        v_d, h_d = abs(r1 - r2), abs(c1 - c2)

        for step in range(0, MAX_ANTENNAS_GENERATE):
            if slope < 0:
                antinodes.append((min(r1, r2) - step * v_d, max(c1, c2) + step * h_d))
                antinodes.append((max(r1, r2) + step * v_d, min(c1, c2) - step * h_d))
            else:
                antinodes.append((min(r1, r2) - step * v_d, min(c1, c2) - step * h_d))
                antinodes.append((max(r1, r2) + step * v_d, max(c1, c2) + step * h_d))
    
    return antinodes


def solution(lines: str):
    antenna_pos = {}
    antinode_set = set()

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == '.':
                continue

            if lines[r][c] not in antenna_pos:
                antenna_pos[lines[r][c]] = set()
            
            antenna_pos[lines[r][c]].add((r, c))
    
    for key in antenna_pos.keys():
        if key=='#':
            continue
        
        positions = list(antenna_pos[key])
        for i in range(len(positions)-1):
            for j in range(i+1, len(positions)):
                antinodes = get_antinode_positions(positions[i], positions[j])
                for (ar, ac) in antinodes:
                    if ar < 0 or ar >= len(lines) or ac < 0 or ac >= len(lines[0]):
                        continue
                    antinode_set.add((ar, ac))
    
    print(len(antinode_set))
                
                
lines = read_input_file(file_path="input.txt")
solution(lines)