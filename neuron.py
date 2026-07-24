import math


def sigmoid(x: float) -> float:
    """Activation function - squishes any number into range (0, 1)."""
    return 1 / (1 + math.exp(-x))


class Neuron:
    def __init__(self, weights: list[float], bias: float):
        """
        A single artificial neuron.
        weights: how important each input is
        bias: baseline offset, shifts the activation threshold
        """
        self.weights = weights
        self.bias = bias

    def forward(self, inputs: list[float]) -> float:
        """
        Forward pass - compute the neuron's output.
        Multiply each input by its weight, sum them, add bias,
        then pass through activation function.
        """
        if len(inputs) != len(self.weights):
            raise ValueError(
                f"Expected {len(self.weights)} inputs, got {len(inputs)}"
            )

        # Step 1: weighted sum
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))

        # Step 2: add bias
        raw_output = weighted_sum + self.bias

        # Step 3: activation function
        output = sigmoid(raw_output)

        return output


# Create a neuron with 3 inputs
# Imagine inputs are: [study_hours, sleep_hours, practice_projects]
# And we're predicting: probability of understanding ML concepts
neuron = Neuron(
    weights=[0.8, 0.4, 0.9],   # practice matters most, sleep second
    bias=-0.5                  # slightly harder to activate
)

# Test with different scenarios
scenarios = [
    ([0.8, 0.7, 0.3], "studied hard, slept well, built projects"),
    ([0.1, 0.4, 0.0], "barely studied, tired, no projects"),
    ([8.0, 5.0, 1.0], "moderate study, great sleep, one project"),
]

print("="*55)
print("  Neuron Output — Probability of Understanding ML")
print("="*55)

for inputs, description in scenarios:
    output = neuron.forward(inputs)
    print(f"\n  Scenario: {description}")
    print(f"  Inputs:   {inputs}")
    print(f"  Output:   {output:.4f} ({output*100:.1f}% probability)")

print("\n" + "="*55)