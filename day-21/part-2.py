import os
from functools import cache
from queue import PriorityQueue

os.system('cls')


DIRECTIONS_SYMBOL_MAP = {
    (0, 1): '>',
    (0, -1): '<',
    (1, 0): 'v',
    (-1, 0): '^'
}

NUM_ROBOTS = 25
ROBOT_MOVE_MAP = {
    'A': {
        'A': 'A',
        '^': '<A',
        '<': 'v<<A',
        '>': 'vA',
        'v': '<vA'
    },
    '^': {
        'A': '>A',
        '^': 'A',
        '<': 'v<A',
        '>': 'v>A',
        'v': 'vA'
    },
    '<': {
        'A': '>>^A',
        '^': '>^A',
        '<': 'A',
        '>': '>>A',
        'v': '>A'
    },
    'v': {
        'A': '^>A',
        '^': '^A',
        '<': '<A',
        '>': '>A',
        'v': 'A'
    },
    '>': {
        'A': '^A',
        '^': '<^A',
        '<': '<<A',
        '>': 'A',
        'v': '<A'
    }
}


class NumericKeypad:
    def __init__(self):
        self.keypad_map = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '0': (3, 1),
            'A': (3, 2)
        }
        
        self.reverse_keypad_map = {value: key for key, value in self.keypad_map.items()}
        self.current_arm_position = (3, 2)
        self.max_height = 4
        self.max_width = 3
    

    def get_manhattan_distance_from_arm(self, target_position: tuple):
        rs, cs = target_position
        re, ce = self.current_arm_position
        return abs(rs - re) + abs(cs - ce)


    def process_code(self, code: str):
        move_list = [self.find_shortest_sequence(button) for button in code]

        all_sequences = []
        queue = [('', -1)]

        while queue:
            current_moves, index = queue.pop(0)

            if index + 1 >= len(move_list):
                all_sequences.append(current_moves)
                continue

            for move in move_list[index + 1]:
                queue.append((current_moves + move, index + 1))
        
        return all_sequences

    
    def find_shortest_sequence(self, button: str):
        queue = PriorityQueue()
        button_position = self.keypad_map[button]
        button_distance = self.get_manhattan_distance_from_arm(button_position)

        item = (button_distance, self.current_arm_position, '', set())
        queue.put(item)
        move_list = []

        while not queue.empty():
            _, position, moves, visited = queue.get()
            visited.add(position)

            if position == button_position:
                self.current_arm_position = position

                if len(moves) == button_distance:
                    move_list.append(moves + 'A')

                continue
            
            r, c = position
            for direction, symbol in DIRECTIONS_SYMBOL_MAP.items():
                step_r, step_c = direction
                r_n, c_n = (r + step_r), (c + step_c)

                if (r_n, c_n) not in self.reverse_keypad_map:
                    continue

                if (r_n, c_n) in visited:
                    continue

                new_distance = abs(r_n - button_position[0]) + abs(c_n - button_position[1])
                item = (new_distance, (r_n, c_n), moves + symbol, visited.copy())
                queue.put(item)
        
        return move_list


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_consecutive_count(sequence: str):
    count = 0
    previous_char = None

    for button in sequence:
        if previous_char is not None:
            if button == previous_char:
                count += 1

        previous_char = button

    return count


def get_max_consecutive_sequences(sequence_list: list[str]):
    sequence_count_map = {}
    max_consecutive_count = float('-inf')

    for sequence in sequence_list:
        consecutive_count = get_consecutive_count(sequence)
        
        if consecutive_count not in sequence_count_map:
            sequence_count_map[consecutive_count] = []
        
        sequence_count_map[consecutive_count].append(sequence)

        if consecutive_count > max_consecutive_count:
            max_consecutive_count = consecutive_count
    
    return sequence_count_map[max_consecutive_count]


@cache
def find_sequence_length_recursive(previous_button: str, current_button: str, robot_num: int):
    if robot_num == NUM_ROBOTS:
        return len(ROBOT_MOVE_MAP[previous_button][current_button])
    
    total_len = 0
    
    next_move_previous_button = 'A'
    for button in ROBOT_MOVE_MAP[previous_button][current_button]:
        total_len += find_sequence_length_recursive(next_move_previous_button, current_button=button, robot_num=robot_num+1)
        next_move_previous_button = button
    
    return total_len


def find_sequence_length(sequence: str):
    total_len = 0
    previous_button = 'A'

    for current_button in sequence:
        total_len += find_sequence_length_recursive(previous_button, current_button, 1)
        previous_button = current_button
    
    return total_len



def solution(lines: list[str]):
    total_sum = 0

    for line in lines:
        door = NumericKeypad()
        all_sequences = door.process_code(code=line)
        max_consecutive_sequences = get_max_consecutive_sequences(all_sequences)

        min_length = float('inf')
        
        for sequence in max_consecutive_sequences:
            sequence_length = find_sequence_length(sequence)
            if sequence_length < min_length:
                min_length = sequence_length
        
        code = int(line[:-1])
        total_sum += (code * min_length)

    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)
print(find_sequence_length_recursive.cache_info())