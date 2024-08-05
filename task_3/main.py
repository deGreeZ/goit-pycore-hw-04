import sys
from pathlib import Path
from colorama import Fore

def print_dir_contents(path: Path, level:int=0, max_levels:int=100):
    for child in path.iterdir():
        is_dir = Path.is_dir(child)
        object_name = child.name
        if is_dir:
            object_name = f"{object_name}/"
        color = Fore.BLUE
        if is_dir:
            color = Fore.YELLOW
        print(f"{"    " * level}{color}{object_name}{Fore.RESET}")
        if is_dir and level < max_levels:
            print_dir_contents(child, level + 1)

def main():
    if len(sys.argv) < 2:
        print("Please, provide dir path as first parameter")
        return
    path = Path(sys.argv[1].strip())
    if not Path.is_dir(path):
        print("Please, provide path to an existent directory")
        return
    print_dir_contents(path)

if __name__ == "__main__":
    main()
