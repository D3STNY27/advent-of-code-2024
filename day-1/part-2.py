def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    left_list, right_count = [], {}
    for line in lines:
        l, r = tuple(map(int, line.split()))
        left_list.append(l)
        
        if r in right_count:
            right_count[r] += 1
        else:
            right_count[r] = 1

    similarity_score = 0
    for i in range(len(left_list)):
        l = left_list[i]
        count = 0 if l not in right_count else right_count[l]
        similarity_score += (l * count)
    
    print(similarity_score)


lines = read_input_file(file_path="input.txt")
solution(lines)