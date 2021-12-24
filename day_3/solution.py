import os

from collections import Counter


def part_1(data):

    gamma_list = []
    epsilon_list = []

    for i in range(len(data[0])):
        col = [item[i] for item in data]
        most_common = Counter(col).most_common(1)[0][0]
        gamma_list.append(most_common)
        epsilon_list.append('0' if (most_common == '1') else '1')

    g = "".join(gamma_list)
    e = "".join(epsilon_list)

    return int(g, 2) * int(e, 2)


def process_data(data, idx, correction, search_most):
    if idx < len(data[0]):
        col = [item[idx] for item in data]
        cnt = Counter(col).most_common()
        if len(cnt) == 2 and cnt[0][1] == cnt[1][1]:
            cnt = correction
        else:
            cnt = cnt[0 if search_most else 1][0]
        res = [item for item in data if item[idx] == cnt]
    else:
        raise IndexError("Bad index value. Max index value allowed - " + str(len(data[0]) - 1) + ".")

    if len(res) == 1:
        return "".join(res[0])
    else:
        return process_data(res, idx + 1, correction, search_most)


def part_2(data):

    oxygen = int(process_data(data, 0, "1", True), 2)
    co2 = int(process_data(data, 0, "0", False), 2)
    return oxygen * co2


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input_data.txt"), "r") as file:
        data = [i.strip() for i in file.readlines()]

    print("Part 1: " + str(part_1([list(line) for line in data])))
    print("Part 2: " + str(part_2([list(line) for line in data])))
