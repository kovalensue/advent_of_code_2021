import os

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input_data.txt"), "r") as file:
        data = [i.strip() for i in file.readlines()]
