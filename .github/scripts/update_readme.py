import os
import re

folder_path = "2024"
total_writeup_2023 = 527

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    first_level_subfolders = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
    total_second_level_subfolder_count = 0

    for subfolder in first_level_subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        second_level_subfolders = [name for name in os.listdir(subfolder_path) if os.path.isdir(os.path.join(subfolder_path, name))]
        total_second_level_subfolder_count += len(second_level_subfolders)

    # Update the README.md file
    readme_file = os.path.join(".", "README.md")
    print(readme_file)
    if os.path.isfile(readme_file):
        with open(readme_file, 'r') as file:
            content = file.read()

        pattern = r"(There are __)(\d+)(__ CTF writeups that have been made in this repository)"

        replacement = f"There are __{total_second_level_subfolder_count + total_writeup_2023}__ CTF writeups that have been made in this repository"
        content = re.sub(pattern, replacement, content)

        with open(readme_file, 'w') as file:
            file.write(content)
