# Writing to a file
with open("my_notes.txt", "w") as file:
    file.write("Day 1: Learned about lists and loops\n")
    file.write("Day 2: Learned about dictionaries and functions\n")
    file.write("Day 3: Learned about error handling and files\n")

print("File written successfully!")

# Reading the whole file
with open("my_notes.txt", "r") as file:
    content = file.read()
    print("\n--- Full file contents ---")
    print(content)

# Reading line by line
with open("my_notes.txt", "r") as file:
    print("--- Line by line ---")
    for line in file:
        print(line.strip()) #strip() removes the \n at the end of each line

import json

# Saving a dictionary as JSON - extremely common in ML for configs and results
model_config = {
    "model_name": "my_local_ai",
    "base_model": "llama3",
    "learning_rate": 0.001,
    "epochs": 10,
    "parameters": ["LoRA", "quantization"]
}

with open("config.json", "w") as file:
    json.dump(model_config, file, indent=4)  # indent=4 makes it human-readable

print("Config saved!")

# Reading it back
with open("config.json", "r") as file:
    loaded_config = json.load(file)

print(f"\nModel name: {loaded_config['model_name']}")
print(f"Learning rate: {loaded_config['learning_rate']}")
print(f"Parameters: {loaded_config['parameters']}")