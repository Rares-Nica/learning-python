# Classes in Python - same concept as C++ but cleaner syntax
class Model:

    def __init__(self, name, base_model, learning_rate):
        self.name = name
        self.base_model = base_model
        self.learning_rate = learning_rate
        self.is_trained = False

    def train(self):
        print(f"Training {self.name} based on {self.base_model}...")
        self.is_trained = True
        print("Training complete!")

    def predict(self, input_text):
        if not self.is_trained:
            raise RuntimeError("Model must be trained before predicting!")
        return f"{self.name} response to '{input_text}': [generated response]"

    def __str__(self):
        status = "trained" if self.is_trained else "not trained"
        return f"Model '{self.name}' ({self.base_model}) - {status}"


my_model = Model("LocalAI", "llama3", 0.001)
print(my_model)

my_model.train()
print(my_model)

print(my_model.predict("What is machine learning?"))

untrained = Model("Untrained", "mistral", 0.001)
try:
    print(untrained.predict("Hello?"))
except RuntimeError as e:
    print(f"Caught error: {e}")