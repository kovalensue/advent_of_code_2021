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


def process_data(data, idx, corr, search_most):
    if idx < len(data[0]):
        col = [item[idx] for item in data]
        most_common = Counter(col).most_common()
        if len(most_common) == 2 and most_common[0][1] == most_common[1][1]:
            most_common = corr
        else:
            most_common = most_common[0 if search_most else 1][0]
        result = [item for item in data if item[idx] == most_common]
    else:
        raise IndexError("Bad index value. Max index value allowed - " + str(len(data[0]) - 1) + ".")

    if len(result) == 1:
        return "".join(result[0])
    else:
        return process_data(result, idx + 1, corr, search_most)


def part_2(data):

    oxygen = int(process_data(data, 0, "1", True), 2)
    co2 = int(process_data(data, 0, "0", False), 2)
    return oxygen * co2


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input_data.txt"), "r") as file:
        data = [i.strip() for i in file.readlines()]

    print("Part 1: " + str(part_1([list(line) for line in data])))
    print("Part 2: " + str(part_2([list(line) for line in data])))
