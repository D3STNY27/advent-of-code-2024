import os

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        line = input_file.read()
        return line


def solution(line: str):
    blocks, space_queue = [], []

    node_id, idx, start_idx = 0, 0, 0
    while True:
        node_size = int(line[idx])
        if idx % 2 == 0:
            blocks.append((node_id, start_idx, node_size))
            node_id += 1
        else:
            if node_size > 0:
                space_queue.append((start_idx, node_size))

        start_idx += int(line[idx])

        idx += 1
        if idx >= len(line):
            break

    arranged_blocks = []
    for i in range(len(blocks)-1, -1, -1):
        block_id, block_start, block_size = blocks[i]
        free_space_idx = -1

        if not space_queue:
            break

        for j in range(len(space_queue)):
            _, space_size = space_queue[j]
            if space_size >= block_size:
                free_space_idx = j
                break
        
        if free_space_idx==-1:
            arranged_blocks.append((block_id, block_start, block_size))
            continue

        space_start, space_size = space_queue[free_space_idx]

        # Important Condition (Do Not Move Blocks Right)
        if space_start > block_start:
            arranged_blocks.append((block_id, block_start, block_size))
            continue

        arranged_blocks.append((block_id, space_start, block_size))
        space_queue.pop(free_space_idx)
        
        if space_size > block_size:
            space_queue.insert(free_space_idx, (space_start + block_size, space_size - block_size))
    

    check_sum = 0
    for block in arranged_blocks:
        block_id, block_start, block_size = block
        ap_sum = (block_start * block_size) + ((block_size) * (block_size-1) // 2)
        check_sum += block_id * ap_sum
    
    print(check_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)