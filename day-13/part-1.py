import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


class Machine:
    def __init__(self, button_a: str, button_b: str, prize: str):
        self.a_x, self.a_y = self.__parse_button_str(button_a)
        self.b_x, self.b_y = self.__parse_button_str(button_b)
        self.p_x, self.p_y = self.__parse_prize_str(prize)
        self.a_cost = 3
        self.b_cost = 1
    

    def __parse_prize_str(self, prize_str: str):
        tokens = prize_str[7:].split(', ')
        tokens_clean = [int(token[2:]) for token in tokens]
        return tokens_clean
    

    def __parse_button_str(self, button_str: str) -> list:
        tokens = button_str[10:].split(', ')
        tokens_clean = [int(token[2:]) for token in tokens]
        return tokens_clean
    

    def calculate_tokens_required(self):
        denominator = self.a_x * self.b_y - self.a_y * self.b_x
        numerator = self.p_y * self.a_x - self.p_x * self.a_y
        button_b_presses = (numerator / denominator)
        if not button_b_presses.is_integer():
            return 0

        button_a_presses = (self.p_x - self.b_x * button_b_presses) / self.a_x
        if not button_a_presses.is_integer():
            return 0
        
        return int(self.a_cost * button_a_presses + self.b_cost * button_b_presses)
    

    def __repr__(self):
        return (
            f'A_X: {self.a_x}, A_Y: {self.a_y},'
            f'B_X: {self.b_x}, B_Y: {self.b_y},'
            f'P_X: {self.p_x}, P_Y: {self.p_y}'
        )
    

    def __str__(self):
        return self.__repr__()


def solution(lines: list[str]):
    machines = []
    for i in range(0, len(lines), 4):
        button_a = lines[i]
        button_b = lines[i+1]
        prize = lines[i+2]

        machines.append(Machine(button_a, button_b, prize))
    
    total_tokens = 0
    for machine in machines:
        tokens = machine.calculate_tokens_required()
        total_tokens += tokens
    
    print(total_tokens)


lines = read_input_file(file_path="input.txt")
solution(lines)