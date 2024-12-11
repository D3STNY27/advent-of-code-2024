import os
os.system('cls')


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]



def is_valid_update(update: list[str], reverse_rule_map: dict[set]):
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if (update[i] in reverse_rule_map) and (update[j] in reverse_rule_map[update[i]]):
                return False
    return True


def solution(lines: str):
    break_idx = lines.index('')
    
    rule_map, reverse_rule_map = {}, {} 
    total_sum = 0

    rules, updates = lines[:break_idx], lines[break_idx+1:]
    
    for rule in rules:
        left_page, right_page = rule.split('|')

        if left_page not in rule_map:
            rule_map[left_page] = set()
        
        if right_page not in reverse_rule_map:
            reverse_rule_map[right_page] = set()
        
        rule_map[left_page].add(right_page)
        reverse_rule_map[right_page].add(left_page)
    
    
    for update in updates:
        update = update.split(',')
    
        if is_valid_update(update, reverse_rule_map):
            continue
    
        update_set = set(update)

        # To-Do: No Need To Store Tuples of Page and Counts
        rule_count_order = []

        for page in update_set:
            if page not in rule_map:
                rule_count_order.append((page, 0))
                continue

            filter_rules = rule_map[page]
            filter_count = len(filter_rules.intersection(update_set))
            rule_count_order.append((page, filter_count))

            # Optimization (Break Early - Middle Element)
            if filter_count == int(len(update) // 2):
                total_sum += int(page)
                break
        
    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)