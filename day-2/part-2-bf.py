import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def generate_possible_series(levels: list[int]):
    series = [levels]
    for i in range(len(levels)):
        series.append((levels[:i] + levels[i+1:]))
    return series


def check_safety(series: list[int]) -> bool:
    dir = series[1] - series[0]
    if dir==0 or abs(dir) < 1 or abs(dir) > 3:
        return False

    for i in range(1, len(series)-1):
        if (series[i+1] - series[i]) * dir < 0:
            return False

        diff = (series[i+1] - series[i])
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    
    return True


def solution(lines: list[str]):
    safe_reports = 0

    for line in lines:
        levels = list(map(int, line.split()))
        all_series = generate_possible_series(levels)
        if any([check_safety(series) for series in all_series]):
            safe_reports += 1
            print(levels)

    print(safe_reports)


lines = read_input_file(file_path="input.txt")
solution(lines)