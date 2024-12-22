import os
from collections import deque
from functools import cache

os.system('cls')

def read_input_file(file_path: str) -> list[str]:
  with open(file=file_path, mode="r") as input_file:
      lines = input_file.readlines()
      return [line.strip() for line in lines]


@cache
def mix_and_prune_secret_number(result: int, secret_number: int):
    return (secret_number ^ result) % 16777216


@cache
def get_next_secret_number(secret_number: int):
    result = secret_number * 64
    secret_number = mix_and_prune_secret_number(secret_number, result)
    result = secret_number // 32
    secret_number = mix_and_prune_secret_number(secret_number, result)
    result = secret_number * 2048
    secret_number = mix_and_prune_secret_number(secret_number, result)
    return secret_number


def solution(lines: list[str]):
    buying_options = {}

    for line in lines:
        current_secret_number = int(line)
        previous_price = line[-1]
        difference_sequence = deque()

        for _ in range(2000):
            next_secret_number = get_next_secret_number(current_secret_number)
            price = str(next_secret_number)[-1]
            current_secret_number = next_secret_number
            
            difference = (int(price) - int(previous_price))
            
            if len(difference_sequence)==4:
                difference_sequence.popleft()
                difference_sequence.append(difference)

                if tuple(difference_sequence) not in buying_options:
                    buying_options[tuple(difference_sequence)] = {}
                
                if line not in buying_options[tuple(difference_sequence)]:
                    buying_options[tuple(difference_sequence)][line] = []

                buying_options[tuple(difference_sequence)][line].append(int(price))
            else:
                difference_sequence.append(difference)

            previous_price = price
    
    # Calculate Max Bananas
    max_sum = float('-inf')
    for buyers in buying_options.values():
        total_sum = 0
        for prices in buyers.values():
            if prices:
                total_sum += prices[0]
        
        if total_sum > max_sum:
            max_sum = total_sum

    print(max_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)
print(mix_and_prune_secret_number.cache_info())
print(get_next_secret_number.cache_info())