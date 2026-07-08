# My name, age, and why I want to learn Python
name = "Rares"
age = 19
goal = "I want to be able to build a fully local AI assistant"

print(f"My name is {name}, I am {age} years old.")
print(f"My goal is: {goal}")

# A simple list - very different from C++ arrays
tools = ["Python", "PyTorch", "MLX", "Ollama"]

for tool in tools:
    print(f"I will learn {tool} to achieve my ultimate goal")

# Python has better ways of indexing than manual C++ approach
# enumerate() gives you both the index AND the value
print("\n--- enumerate ---")
for index, tool in enumerate(tools):
    print(f"{index+1}. {tool}")

# zip() lets you loop over two lists simultaneously
difficulty = ["Beginner", "Intermediate", "Advanced", "Expert"]
print("\n--- zip ---")
for tool, level in zip(tools, difficulty):
    print(f"{tool} - {level}")

# List comprehension - Python's most powerful one-liner
print("\n--- list comprehension ---")
upper_tools = [tool.upper() for tool in tools]
print(upper_tools)