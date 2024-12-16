import os
os.system('cls')


DIRECTION_MAP = {
    '<': (0, -1),
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0)
}

class Box:
    def __init__(self, left_coord):
        left_r, left_c = left_coord
        
        self.left = left_coord
        self.right = (left_r, left_c+1)
    

    def update_position(self, direction: tuple):
        step_r, step_c = direction

        left_r, left_c = self.left
        right_r, right_c = self.right

        self.left = (left_r + step_r), (left_c + step_c)
        self.right = (right_r + step_r), (right_c + step_c)
    

    def __repr__(self):
        return f'[{self.left}, {self.right}]'


    def __str__(self):
        return self.__repr__()


class Grid:
    def __init__(self, grid: list[str]):
        self.height = len(grid)
        self.width = len(grid[0])

        self.walls, self.boxes = set(), {}
        self.robot_start_position = None

        for r in range(self.height):
            for c in range(self.width):
                if grid[r][c]=='#':
                    self.walls.add((r, c))

                if grid[r][c]=='[':
                    box = Box(left_coord=(r, c))
                    self.boxes[box.left] = box
                    self.boxes[box.right] = box
                
                if grid[r][c]=='@':
                    self.robot_start_position = (r, c)
    

    def do_movement(self, position: tuple, direction: tuple):
        if direction==(0, -1) or direction==(0, 1):
            is_valid_movement, boxes_to_move = self.__do_horizontal_movement(position, direction)
        else:
            is_valid_movement, boxes_to_move = self.__do_vertical_movement(position, direction)
    
        if not is_valid_movement:
            return False
        
        for box in boxes_to_move:
            del self.boxes[box.left]
            del self.boxes[box.right]
        
        for box in boxes_to_move:
            box.update_position(direction)
            self.boxes[box.left] = box
            self.boxes[box.right] = box

        return True
    
    
    def __do_horizontal_movement(self, position: tuple, direction: tuple):
        r, c = position
        step_r, step_c = direction

        r_n, c_n = (r + step_r), (c + step_c)

        if r_n < 0 or r_n >= self.height or c_n < 0 or c_n >= self.width:
            return False, set()

        if (r_n, c_n) in self.walls:
            return False, set()
        
        if (r_n, c_n) not in self.boxes:
            return True, set()

        boxes_to_move = set()
        is_valid_movement = False
        steps = 1

        while True:
            r_n, c_n = (r + step_r * steps), (c + step_c * steps)

            if r_n < 0 or r_n >= self.height or c_n < 0 or c_n >= self.width:
                break

            if (r_n, c_n) in self.walls:
                break

            if (r_n, c_n) in self.boxes:
                box = self.boxes[(r_n, c_n)]
                boxes_to_move.add(box)
                steps += 1
            else:
                is_valid_movement = True
                break
        
        return is_valid_movement, boxes_to_move


    def __do_vertical_movement(self, position: tuple, direction: tuple):
        r, c = position
        step_r, step_c = direction

        r_n, c_n = (r + step_r), (c + step_c)

        if r_n < 0 or r_n >= self.height or c_n < 0 or c_n >= self.width:
            return False, set()

        if (r_n, c_n) in self.walls:
            return False, set()
        
        if (r_n, c_n) not in self.boxes:
            return True, set()
        
        boxes_to_move = set()
        is_valid_movement = True

        initial_box = self.boxes[(r_n, c_n)]
        boxes_to_move.add(initial_box)

        queue = [self.boxes[(r_n, c_n)]]
        while queue:
            box = queue[0]
            queue = queue[1:]

            for (b_r, b_c) in [box.left, box.right]:
                b_rn, b_cn = (b_r + step_r), (b_c + step_c)

                if (b_rn, b_cn) in self.walls:
                    is_valid_movement = False
                    break

                if (b_rn, b_cn) in self.boxes:
                    queue.append(self.boxes[(b_rn, b_cn)])
                    boxes_to_move.add(self.boxes[(b_rn, b_cn)])

        return is_valid_movement, boxes_to_move


    def get_gps_sum(self):
        gps_sum = 0
        for box in set(self.boxes.values()):
            gps_sum += (100 * box.left[0] + box.left[1])
        return gps_sum
    

    def __repr__(self):
        all_rows = []
        for r in range(self.height):
            current_row = ''
            for c in range(self.width):
                if (r, c) in self.walls:
                    current_row += '#'

                elif (r, c) in self.boxes:
                    box = self.boxes[(r, c)]
                    if box.left == (r, c):
                        current_row += '['
                    else:
                        current_row += ']'

                else:
                    current_row += '.'

            all_rows.append(current_row)
        return '\n'.join(all_rows)


    def __str__(self):
        return self.__repr__()
    


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    divider = lines.index('')
    
    init_grid = lines[:divider]
    moves = ''.join(lines[divider+1:])

    exp_grid = []
    for r in range(len(init_grid)):
        current_row = ''
        for c in range(len(init_grid[r])):
            if init_grid[r][c]=='#':
                current_row += '##'
            elif init_grid[r][c]=='O':
                current_row += '[]'
            elif init_grid[r][c]=='.':
                current_row += '..'
            else:
                current_row += '@.'

        exp_grid.append(current_row)
    

    grid = Grid(exp_grid)
    current_robot_position = grid.robot_start_position
    print(current_robot_position)

    for move in moves:
        direction = DIRECTION_MAP[move]
        is_valid_move = grid.do_movement(current_robot_position, direction)
        if not is_valid_move:
            continue
        
        step_r, step_c = direction
        r, c = current_robot_position
        current_robot_position = (r + step_r, c + step_c)
    
    print(grid.boxes)
    print(grid.get_gps_sum())


lines = read_input_file(file_path="input.txt")
solution(lines)