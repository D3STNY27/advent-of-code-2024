def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    left_list, right_list = [], []
    for line in lines:
        l, r = tuple(map(int, line.split()))
        left_list.append(l)
        right_list.append(r)
    
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for i in range(len(left_list)):
        l, r = left_list[i], right_list[i]
        total_distance += abs(l - r)
    
    print(total_distance)


lines = read_input_file(file_path="input.txt")
solution(lines)