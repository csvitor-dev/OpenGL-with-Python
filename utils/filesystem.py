from pathlib import Path
from os import path

def read_file(filename: str) -> str:
    abs_path = path.abspath(filename)
    target_path = Path(abs_path)

    if target_path.exists() is False:
        raise FileExistsError
    return target_path.read_text()
