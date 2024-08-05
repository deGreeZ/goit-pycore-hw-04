from pathlib import Path

def get_cats_info(path: str) -> list:
    file_path = Path(path)
    cat_data_keys = ["id", "name", "age"]
    try:
        with open(file_path.absolute()) as file:
            cats_data = [dict(zip(cat_data_keys, line.strip().split(",")[:3])) for line in file.readlines()]
    except FileNotFoundError:
        return []
    if len(cats_data[0].keys()) != 3: # expecting number of columns to be consistent within file
        return []
    return cats_data

# Usage examples

cats_info = get_cats_info("task_2.csv")
print("When everything is OK:", cats_info)

cats_info = get_cats_info("task_2_invalid_separator.csv")
print("When separator is invalid:", cats_info)

cats_info = get_cats_info("task_2_invalid_data.csv")
print("When data is invalid:", cats_info)
