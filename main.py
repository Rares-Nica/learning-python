# main.py - the entry point of the project
# imports from our own utils module
from utils.helpers import load_json, save_json, file_exists, calculate_average
# Using our helper functions
scores = [88.0, 92.0, 79.0, 95.0, 85.0]
avg = calculate_average(scores)
print(f"Average score: {avg}")

# Check if our config exists before loading
if file_exists("config.json"):
    config = load_json("config.json")
    print(f"Found config for model: {config['model_name']}")
else:
    print("No config found!")

# Save some results
results = {
    "average_score": avg,
    "total_samples": len(scores),
    "highest": max(scores),
    "lowest": min(scores)
}

save_json(results, "data/results.json")