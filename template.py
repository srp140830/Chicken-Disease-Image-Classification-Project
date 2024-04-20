# This is to create folder structure for the project in a pythonic way and avoiding manual creation.
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "cnnClassifier"

# List of files you want to create for this project
list_of_files = [
    ".github/workflows/.gitkeep",  #for ci/cd deployment
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", # components will be local package folder.
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml", 
    "dvc.yaml", # integrating mlops tool
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "notebooks/experiments.ipynb"

]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file: {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")
    



