from pathlib import Path

BASE_PATH = Path(__file__).parent
DATA_FOLDER_PATH = BASE_PATH / "../data"


def get_lines(filename: str) -> list:
    file_path = (DATA_FOLDER_PATH / filename).resolve()
    with open(file_path, mode="rt") as file:
        lines = file.read().split("\n")

    return lines
