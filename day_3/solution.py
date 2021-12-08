import os

from collections import Counter


def part_1(data):

    gamma_list = []
    epsilon_list = []

    data_matrix = [list(line) for line in data]

    for i in range(len(data_matrix[0])):
        col = [item[i] for item in data_matrix]
        most_common = Counter(col).most_common(1)[0][0]
        gamma_list.append(most_common)
        epsilon_list.append('0' if (most_common == '1') else '1')

    g = "".join(gamma_list)
    e = "".join(epsilon_list)

    print("Gamma: " + g)
    print("Epsilon: " + e)

    return int(g, 2) * int(e, 2)


def part_2(data):
    pass


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input_data.txt"), "r") as file:
        data = [i.strip() for i in file.readlines()]

    print("Part 1: " + str(part_1(data)))
    print("Part 2: " + str(part_2(data)))
