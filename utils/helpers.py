# utils/helpers.py
# Reusable helper functions that any part of the project can import

import json
from pathlib import Path

def load_json(filepath: str) -> dict:
    """Load a JSON file and return its contents as a dictionary."""
    with open(filepath, "r") as file:
        return json.load(file)


def save_json(data: dict, filepath: str) -> None:
    """Save a dictionary to a SON file."""
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
        print(f"Saved to {filepath}")


def file_exists(filepath: str) -> bool:
    """Check if a file exists without crashing."""
    return Path(filepath).exists()


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average numbers of empty list.")
    return sum(numbers) / len(numbers)