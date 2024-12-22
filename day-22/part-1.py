
from functools import cache

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
    total_sum = 0

    for line in lines:
        current_secret_number = int(line)
        for _ in range(2000):
            current_secret_number = get_next_secret_number(current_secret_number)
        
        total_sum += current_secret_number
    
    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)
print(mix_and_prune_secret_number.cache_info())
print(get_next_secret_number.cache_info())