from pathlib import Path

def total_salary(path: str) -> tuple[int|None]:
    file_path = Path(path)
    try:
        with open(file_path.absolute()) as file:
            salaries = [int(line.strip().split(",")[1]) for line in file.readlines()]
    except FileNotFoundError:
        return (None, None)
    except IndexError: # file content formatting is incorrect
        return (None, None)
    except ValueError: # second row contains non-int value
        return (None, None)

    total = sum(salaries)
    return (total, total // len(salaries))

# Usage examples

total, average = total_salary("task_1.csv")
print(f"Total salary: {total}\nAverage salary: {average}")

result = total_salary("nonexisting_task_1.csv")
total, average = result # showd that unpacking is working
print(f"When file not found the result is: {result}")

result = total_salary("task_1_invalid_separator.csv")
total, average = result # showd that unpacking is working
print(f"When file uses invalid separator the result is: {result}")

result = total_salary("task_1_invalid_value.csv")
total, average = result # showd that unpacking is working
print(f"When file contains invalid data type the result is: {result}")
