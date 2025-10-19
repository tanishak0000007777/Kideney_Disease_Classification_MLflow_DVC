import os
from pathlib import Path
import logging

# crate a logging string
# Sets up a simple logging format.
# Every time a directory or file is created, it prints the timestamp and a message.

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='cnnClassifier'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Different operating systems use different path separators:
# Windows: uses backslashes → \
# Linux / macOS: uses forward slashes → /

# filepath = Path(filepath)
# you’re converting the string path into a Path object from the pathlib module.

# That means:
# Python automatically chooses the correct separator for your OS.
# So "src/cnnClassifier/utils/__init__.py" will become:
# On Windows → src\cnnClassifier\utils\__init__.py
# On Linux/macOS → src/cnnClassifier/utils/__init__.py

for filepath in list_of_files:


    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"File {filepath} already exists")
