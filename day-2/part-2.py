import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


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


def is_safe(levels: list[int]):
    idx_map = {
        '+': [],
        '-': [],
        'o': []
    }

    max_diff = float('-inf')

    for i in range(len(levels)-1):
        diff = levels[i+1] - levels[i]

        if diff==0:
            idx_map['o'].append(i)
        elif diff > 0:
            idx_map['+'].append(i)
        else:
            idx_map['-'].append(i)

        if abs(diff) > max_diff:
            max_diff = abs(diff)
    
    # too many repetitions (Unsafe)
    if len(idx_map['o']) > 1:
        return False
    
    # exactly 1 repetition (Safe if No Deviations)
    if len(idx_map['o'])==1:
        if len(idx_map['+'])==len(levels)-2 or len(idx_map['-'])==len(levels)-2:
            return True if max_diff <= 3 else False
        else:
            return False
    
    # no repetitions (check sequence)

    # strictly increasing or decreasing
    if len(idx_map['+'])==len(levels)-1 or len(idx_map['-'])==len(levels)-1:
        return True if max_diff <= 3 else False
    
    # atmost 1 deviation (positive sequence)
    if len(idx_map['-'])==1:
        idx = idx_map['-'][0]

        if idx==0:
            return check_safety(levels[1:]) or check_safety(levels[:idx] + levels[idx+1:])
        elif idx==len(levels)-2:
            return check_safety(levels[:-1]) or check_safety(levels[:idx] + levels[idx+1:])
        else:
            return check_safety(levels[:idx+1] + levels[idx+2:]) or check_safety(levels[:idx] + levels[idx+1:])

    # atmost 1 deviation (negative sequence)
    if len(idx_map['+'])==1:
        idx = idx_map['+'][0]

        if idx==0:
            return check_safety(levels[1:]) or check_safety(levels[:idx] + levels[idx+1:])
        elif idx==len(levels)-2:
            return check_safety(levels[:-1]) or check_safety(levels[:idx] + levels[idx+1:])
        else:
            return check_safety(levels[:idx+1] + levels[idx+2:]) or check_safety(levels[:idx] + levels[idx+1:])
    
    return True if max_diff <=3 else False


def solution(lines: list[str]):
    safe_reports = 0

    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe(levels):
            print(levels)
            safe_reports += 1
        
    print(safe_reports)



lines = read_input_file(file_path="input.txt")
solution(lines)
