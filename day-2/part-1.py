import os
os.system('cls')

def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    safe_reports = 0

    for line in lines:
        levels = list(map(int, line.split()))
        dir = levels[1] - levels[0]
        if dir==0 or abs(dir) < 1 or abs(dir) > 3:
            continue

        safe = True
        for i in range(1, len(levels)-1):
            if (levels[i+1] - levels[i]) * dir < 0:
                safe = False
                break

            diff = (levels[i+1] - levels[i])
            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break
        
        print(levels, safe)
        if not safe:
            continue

        safe_reports += 1

    print(safe_reports)



lines = read_input_file(file_path="input.txt")
solution(lines)