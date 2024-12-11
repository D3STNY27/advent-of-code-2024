import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]



def is_valid_update(update: list[str], rule_set: set):
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if (update[j], update[i]) in rule_set:
                return False
    return True


def solution(lines: str):
    break_idx = lines.index('')
    
    rule_set = set()
    total_sum = 0

    rules, updates = lines[:break_idx], lines[break_idx+1:]
    
    for rule in rules:
        rule_set.add(tuple(rule.split('|')))
    
    for update in updates:
        update = update.split(',')

        if not is_valid_update(update, rule_set):
            continue

        total_sum += int(update[len(update) // 2])
    
    print(total_sum)



lines = read_input_file(file_path="input.txt")
solution(lines)