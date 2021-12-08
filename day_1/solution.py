import os


def part_1(data):
    prev_val = None
    cnt_increased = 0
    cnt_decreased = 0

    for val in data:
        if prev_val is None:
            pass
        elif val > prev_val:
            # print(str(val) + " (increased)")
            cnt_increased += 1
        elif val < prev_val:
            # print(str(val) + " (decreased)")
            cnt_decreased += 1
        else:
            pass
        prev_val = val

    print("Results:")
    print("cnt_decreased = " + str(cnt_decreased))
    print("cnt_increased = " + str(cnt_increased))


def part_2(data, window_size):

    windows = []

    for i in range(len(data) - window_size + 1):
        # print(data[i: i + window_size])
        windows.append(data[i: i + window_size])

    windows_sum = [sum(i) for i in windows]
    part_1(windows_sum)


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input_data.txt"), "r") as file:
        data = [int(i) for i in file.readlines()]

    print("Part one:")
    part_1(data)

    print("\nPart two:")
    part_2(data, 3)
