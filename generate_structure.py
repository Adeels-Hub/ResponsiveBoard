import os
import json

def generate_structure_json(root_dir):
    structure = {}
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):
            structure[folder] = [
                file for file in os.listdir(folder_path) if file.endswith(('.md', '.html'))
            ]

    with open(os.path.join(root_dir, "structure.json"), "w") as f:
        json.dump(structure, f, indent=4)

if __name__ == "__main__":
    generate_structure_json(".")  # Replace "." with your root folder path if different
