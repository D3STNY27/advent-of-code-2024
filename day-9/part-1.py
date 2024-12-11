import os
from collections import deque

os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        line = input_file.read()
        return line


def solution(line: str):
    block_queue = deque()
    space_queue = deque()

    node_id, idx, start_idx = 0, 0, 0
    while True:
        node_size = int(line[idx])
        if idx % 2 == 0:
            block_queue.append((node_id, start_idx, node_size))
            node_id += 1
        else:
            if node_size > 0:
                space_queue.appendleft((start_idx, node_size))

        start_idx += int(line[idx])

        idx += 1
        if idx >= len(line):
            break


    while space_queue:
        space_start, space_size = space_queue.pop()
        block_id, block_start, block_size = block_queue.pop()
        if block_start < space_start:
            block_queue.append((block_id, block_start, block_size))
            break
        
        if block_size <= space_size:
            block_queue.appendleft((block_id, space_start, block_size))
            if (space_size - block_size)!=0:
                space_queue.append((space_start + block_size, (space_size - block_size)))
        else:
            block_queue.appendleft((block_id, space_start, space_size))
            block_queue.append((block_id, block_start, (block_size - space_size)))


    check_sum = 0
    while block_queue:
        block_id, block_start, block_size = block_queue.pop()
        ap_sum = (block_start * block_size) + ((block_size) * (block_size-1) // 2)
        check_sum += block_id * ap_sum
    
    print(check_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)