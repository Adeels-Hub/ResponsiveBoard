import os
import json

skip_folders = ["dashboard"]
skip_folders = [name.lower() for name in skip_folders]

def generate_structure_json(root_dir):
    structure = {}
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)

        # Normalize for comparison
        if os.path.isdir(folder_path):
            folder_name_normalized = folder.lower().strip()

            if folder_name_normalized in skip_folders:
                print(f"Skipping folder: {folder}")
                continue

            files = [
                file for file in os.listdir(folder_path)
                if file.endswith(('.md', '.html'))
            ]

            # Only include folders with matching files
            if files:
                structure[folder] = files

    with open(os.path.join(root_dir, "structure.json"), "w") as f:
        json.dump(structure, f, indent=4)

if __name__ == "__main__":
    generate_structure_json(".")
