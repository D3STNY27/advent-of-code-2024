import os
os.system('cls')


BLINKS = 25


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        line = input_file.read()
        return line


def solution(line: str):
    stones = [stone for stone in line.split()]

    for _ in range(BLINKS):
        stones_temp = []
        for stone in stones:
            if stone=='0':
                stones_temp.append('1')
            else:
                length = len(stone)
                half_length = len(stone) // 2

                if length % 2 == 0:
                    stones_temp.append(str(int(stone[:half_length])))
                    stones_temp.append(str(int(stone[half_length:])))
                else:
                    stones_temp.append(str(int(stone) * 2024))

        stones = stones_temp

    print(len(stones))


lines = read_input_file(file_path="input.txt")
solution(lines)