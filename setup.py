from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "Chest-Cancer-Classification"  # Adjusted to a more conventional package name (no spaces)
VERSION = "0.0.1"
AUTHOR = "Viketan"
DESCRIPTION = (
    "The Chest-Cancer-Classification project is an advanced machine learning application designed to aid in the early detection and diagnosis of chest cancer through the analysis of medical imaging data. This project leverages deep learning techniques, specifically Convolutional Neural Networks (CNNs), to accurately classify chest images into various categories of cancerous and non-cancerous findings."
)
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Reads the requirements from the requirements.txt file.

    Returns:
        List[str]: A list of package names specified in requirements.txt.
    """
    try:
        with open(REQUIREMENT_FILE_NAME) as requirement_file:
            # Read lines and clean up whitespace
            requirement_list = [line.strip() for line in requirement_file.readlines()]
            # Remove editable installation if present
            if HYPHEN_E_DOT in requirement_list:
                requirement_list.remove(HYPHEN_E_DOT)
            return requirement_list
    except FileNotFoundError:
        print(f"Warning: {REQUIREMENT_FILE_NAME} not found. Please ensure it exists.")
        return []  # Return an empty list if requirements.txt is not found

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=get_requirements_list(),  # Install required packages
    python_requires='>=3.8',  # Specify the minimum Python version required
    classifiers=[  # Classifiers to help others find your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
