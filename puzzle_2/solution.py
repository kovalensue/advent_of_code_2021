import os


def part_1(data):

    horizontal_pos = 0
    depth = 0

    for d in data:
        direction, value = d.split(" ")
        match direction:
            case "forward":
                horizontal_pos += int(value)
            case "up":
                depth -= int(value)
            case "down":
                depth += int(value)
            case _:
                print(f"Unknown direction - {direction}")

    print(horizontal_pos * depth)


def part_2(data):

    horizontal_pos = 0
    depth = 0
    aim = 0

    for d in data:
        direction, value = d.split(" ")
        match direction:
            case "forward":
                horizontal_pos += int(value)
                depth = depth + (aim * int(value))
            case "up":
                aim -= int(value)
            case "down":
                aim += int(value)
            case _:
                print(f"Unknown direction - {direction}")

    print(horizontal_pos * depth)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input_data.txt"), "r") as file:
        data = [i for i in file.readlines()]

    part_1(data)
    part_2(data)
