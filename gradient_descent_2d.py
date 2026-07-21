import numpy as np

# Two weights instead of one
# Loss function: loss = w1² + w2²
# This is a bowl shape in 3D space - minimum at (0, 0)

w1 = 10.0
w2 = -8.0
learning_rate = 0.1

print(f"{'Step':<6} {'w1':>10} {'w2':>10} {'loss':>10}")
print("-" * 40)

for step in range(20):
    loss = w1**2 + w2**2

    # Partial derivatives
    grad_w1 = 2 * w1
    grad_w2 = 2 * w2

    # Update both weights simultaneously
    w1 = w1 - learning_rate * grad_w1
    w2 = w2 - learning_rate * grad_w2

    if step % 2 == 0: # print every other step
        print(f"{step:<6} {w1:>10.4f} {w2:>10.4f} {loss:>10.4f}")

print(f"\nFinal: w1={w1: .6f}, w2={w2: .6f}, loss={loss: .6f}")