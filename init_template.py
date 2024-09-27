import os
import fileinput
from datetime import datetime


def replace_in_file(file_path: str, old_string: str, new_string: str):
    try:
        with fileinput.input(file_path, inplace=True) as file:
            for line in file:
                print(line.replace(old_string, new_string), end='')
    except UnicodeDecodeError:
        print("Failed to replace in " + file_path)

def replace_in_directory(directory: str, old_string: str, new_string: str):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            exclude = ["__pycache__", ".git", "init_template.py", "env", "cache", "logs"]
            should_continue = False
            for ex in exclude:
                if ex in file_path:
                    should_continue = True
            if should_continue:
                continue
            replace_in_file(file_path, old_string, new_string)

def main() -> int:
    print("--- Python Module Templateifier ---")
    author_name = input("What is your full name? > ")
    author_email = input("What is your email? > ")
    module = input("What should this module be named? > ")
    year = str(datetime.now().year)
    print("Templatifing...")
    replace_in_directory(".", "{MODULE}", module)
    replace_in_directory(".", "{YEAR}", year)
    replace_in_directory(".", "{AUTHOR_EMAIL}", author_email)
    replace_in_directory(".", "{AUTHOR_NAME}", author_name)
    os.rename("newmodule", module)
    os.remove(os.path.abspath(__file__))
    print("This script has deleted itself, and your new module is ready for use!")
    return 0

if __name__ == "__main__":
    main()