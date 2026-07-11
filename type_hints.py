# Type hints - telling Python and your editor what types to expect
# Python doesn't enforce these at runtime but they make code
# readable and help VS Code catch bugs before you run anything

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def load_config(filepath: str) -> dict:
    import json
    with open(filepath, "r") as file:
        return json.load(file)

# Notice VS Code will now warn you if you pass the wrong type
print(greet("Rares", 19))
print(calculate_average([85.0, 92.0, 78.0, 95.0]))

# Load the config we saved yesterday
config = load_config("config.json")
print(f"Loaded model: {config['model_name']}")