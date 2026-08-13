"""
Lesson 4: Backpropagation — Understand It From Start to End
============================================================

Read this file from top to bottom. It focuses on meaning first, formulas
second. Run it to see the examples.

The one sentence definition
---------------------------
Backpropagation calculates how each weight affects the final loss, then gives
each weight an instruction for how to change so loss becomes smaller.

The whole training loop
-----------------------
    1. Forward pass: make a prediction.
    2. Loss: measure how wrong the prediction is.
    3. Backward pass / backpropagation: calculate a gradient for every weight.
    4. Update: change every weight a small amount using its gradient.
    5. Repeat.

What is a gradient here?
-------------------------
The gradient is an instruction for ONE weight:

    - sign: should this weight go up or down?
    - size: how strongly does this weight affect loss right now?

The update always has this form:

    weight = weight - learning_rate * weight_gradient

Therefore:
    negative gradient -> subtracting it increases the weight
    positive gradient -> subtracting it decreases the weight

Learning rate controls the size of the adjustment. We use a small one to make
steady improvements instead of jumping past the best values.
"""


# ---------------------------------------------------------------------------
# PART 1 — ONE INPUT, ONE WEIGHT: THE CORE IDEA
# ---------------------------------------------------------------------------
#
# Model:
#     prediction = w * x
#     error = prediction - target
#     loss = error**2
#
# Example A: prediction too low
#     x = 3, w = 2, target = 10
#     prediction = 2*3 = 6
#     error = 6 - 10 = -4
#     loss = (-4)**2 = 16
#
# If w increases by 1, prediction increases by x=3:
#     w=3 -> prediction=3*3=9
# Thus increasing w makes prediction closer to 10 and lowers loss.
#
# Backpropagation calculates the exact instruction:
#     loss signal = d_loss/d_prediction = 2 * error
#     effect of w on prediction = d_prediction/dw = x
#     weight gradient = d_loss/dw = (2*error) * x
#
# Example A:
#     loss signal = 2*(-4) = -8
#     weight gradient = -8*3 = -24
#
# -24 means: increasing w reduces loss. The update subtracts -24, so w goes up.
#
# Example B: prediction too high
#     x = 3, w = 4, target = 10
#     prediction = 12
#     error = +2
#     loss signal = +4
#     weight gradient = +4*3 = +12
#
# +12 means: increasing w increases loss. The update subtracts +12, so w goes
# down. That decreases the too-high prediction.


def one_weight_step(x: float, w: float, target: float, learning_rate: float) -> tuple:
    """Perform one full learning step for prediction = w*x.

    Returns values from BEFORE the update, plus the updated weight.
    """
    prediction = w * x
    error = prediction - target
    loss = error**2

    # Backpropagation: loss signal times the effect of w on prediction.
    loss_signal = 2 * error
    weight_gradient = loss_signal * x

    new_w = w - learning_rate * weight_gradient
    return prediction, error, loss, weight_gradient, new_w


# ---------------------------------------------------------------------------
# PART 2 — BIAS: A KNOB THAT ALWAYS CHANGES PREDICTION BY 1
# ---------------------------------------------------------------------------
#
# Model:
#     prediction = w*x + b
#
# A +1 change in w changes prediction by x.
# A +1 change in b changes prediction by 1.
#
# So:
#     weight_gradient = loss_signal * x
#     bias_gradient   = loss_signal * 1
#
# Example: x=3, w=2, b=1, target=10
#     prediction = 2*3 + 1 = 7
#     error = -3
#     loss signal = 2*(-3) = -6
#     weight gradient = -6*3 = -18
#     bias gradient = -6*1 = -6
#
# Both gradients are negative: both w and b should increase because the
# prediction is too low. Weight has a larger gradient because it affects the
# prediction by 3, while bias affects it by only 1.


def one_neuron_step(
    x: float, w: float, b: float, target: float, learning_rate: float
) -> tuple:
    """Perform one forward pass, backward pass, and update for w*x+b."""
    prediction = w * x + b
    error = prediction - target
    loss = error**2

    loss_signal = 2 * error
    weight_gradient = loss_signal * x
    bias_gradient = loss_signal

    new_w = w - learning_rate * weight_gradient
    new_b = b - learning_rate * bias_gradient
    return prediction, error, loss, weight_gradient, bias_gradient, new_w, new_b


def train_one_neuron(
    x: float, w: float, b: float, target: float, learning_rate: float, steps: int
) -> tuple[float, float]:
    """Train w*x+b repeatedly and print progress."""
    for step in range(1, steps + 1):
        prediction, error, loss, wg, bg, w, b = one_neuron_step(
            x, w, b, target, learning_rate
        )
        print(
            f"  step {step}: prediction={prediction:.4f}, error={error:.4f}, "
            f"loss={loss:.4f}, w={w:.4f}, b={b:.4f}"
        )
    return w, b


# ---------------------------------------------------------------------------
# PART 3 — TWO INPUTS, TWO WEIGHTS: EACH WEIGHT GETS ITS OWN INSTRUCTION
# ---------------------------------------------------------------------------
#
# Model:
#     prediction = w1*x1 + w2*x2 + b
#
# Same loss signal goes backward to all weights. But each weight's gradient is
# scaled by its own input:
#
#     w1_gradient = loss_signal * x1
#     w2_gradient = loss_signal * x2
#     b_gradient  = loss_signal
#
# Example:
#     x1=2, x2=4, w1=1, w2=1, b=0, target=10
#     prediction = 2 + 4 = 6, so error=-4 and loss signal=-8.
#
#     w1_gradient = -8*2 = -16
#     w2_gradient = -8*4 = -32
#
# Both weights increase because prediction is too low. w2 gets a bigger update
# because changing w2 changes prediction by 4, while changing w1 changes it by 2.
#
# Mental model:
#     gradient for a weight = how wrong the prediction is
#                             * how strongly that weight affects prediction


def two_input_step(
    x1: float,
    x2: float,
    w1: float,
    w2: float,
    b: float,
    target: float,
    learning_rate: float,
) -> tuple:
    """One learning step for prediction = w1*x1 + w2*x2 + b."""
    prediction = w1 * x1 + w2 * x2 + b
    error = prediction - target
    loss = error**2

    loss_signal = 2 * error
    w1_gradient = loss_signal * x1
    w2_gradient = loss_signal * x2
    b_gradient = loss_signal

    w1 -= learning_rate * w1_gradient
    w2 -= learning_rate * w2_gradient
    b -= learning_rate * b_gradient

    return prediction, loss, w1_gradient, w2_gradient, b_gradient, w1, w2, b


# ---------------------------------------------------------------------------
# PART 4 — WHY IT IS CALLED "BACKPROPAGATION"
# ---------------------------------------------------------------------------
#
# The forward pass flows left to right:
#
#     input -> intermediate value -> prediction -> loss
#
# The learning instruction flows backward, from loss to earlier weights:
#
#     loss -> prediction -> intermediate value -> earlier weight
#
# At each backward connection we multiply by the local derivative / effect.
# This is the chain rule in action.


# ---------------------------------------------------------------------------
# PART 5 — A TINY HIDDEN-LAYER CHAIN
# ---------------------------------------------------------------------------
#
# This has two layers but only one value in each layer:
#
#     h = w*x                 # hidden value
#     prediction = v*h        # output value
#     loss = (prediction-target)**2
#
# Example:
#     x=3, w=2 -> h=6
#     v=2 -> prediction=12
#     target=10 -> error=+2
#     loss signal = 2*error = +4
#
# To find the gradient for EARLIER weight w, ask three effect questions:
#
#     1. d_loss/d_prediction = +4
#        How does prediction affect loss? This is the loss signal.
#
#     2. d_prediction/dh = v = 2
#        If h rises by 1, prediction rises by 2.
#
#     3. dh/dw = x = 3
#        If w rises by 1, h rises by 3.
#
# Chain rule:
#
#     d_loss/dw
#     = d_loss/d_prediction * d_prediction/dh * dh/dw
#     = 4 * 2 * 3
#     = 24
#
# Positive 24 means increasing w increases loss. Therefore the update decreases w.
#
# Important: this is not a new rule. It is the same question repeated:
# "How much does this earlier thing affect the next thing?"


def two_layer_chain_step(
    x: float, w: float, v: float, target: float, learning_rate: float
) -> tuple:
    """One learning step through h=w*x then prediction=v*h.

    There are no biases or activations here, so the chain rule is easy to see.
    """
    # Forward pass
    h = w * x
    prediction = v * h
    error = prediction - target
    loss = error**2

    # Backward pass: work from loss back toward each weight.
    loss_signal = 2 * error                 # d_loss/d_prediction
    v_gradient = loss_signal * h             # d_loss/dv
    h_signal = loss_signal * v               # d_loss/dh
    w_gradient = h_signal * x                # d_loss/dw

    # Update both weights after ALL gradients have been calculated.
    new_w = w - learning_rate * w_gradient
    new_v = v - learning_rate * v_gradient

    return h, prediction, loss, v_gradient, w_gradient, new_w, new_v


# ---------------------------------------------------------------------------
# PART 6 — ACTIVATIONS: ONE EXTRA EFFECT IN THE CHAIN
# ---------------------------------------------------------------------------
#
# A real hidden neuron usually applies an activation, for example:
#
#     z = w*x + b
#     a = sigmoid(z)
#
# Backpropagation is still unchanged in spirit. There is only one more local
# effect to multiply by:
#
#     d_loss/dz = d_loss/da * da/dz
#
# For sigmoid:
#     da/dz = a * (1-a)
#
# You do not need to memorize its derivation now. The key idea:
#     every operation contributes its own local "how much does input change
#     output?" value, and backpropagation multiplies these values backward.
#
# Modern neural networks often use ReLU in hidden layers. Libraries calculate
# all these derivatives automatically.


# ---------------------------------------------------------------------------
# PART 7 — JACOBIAN: THE MANY-INPUT, MANY-OUTPUT VERSION
# ---------------------------------------------------------------------------
#
# A normal derivative asks:
#     "How does one output change when one input changes?"
#
# A Jacobian is a table of all such effects when there are many inputs and many
# outputs:
#
#               x1       x2
#     y1     dy1/dx1  dy1/dx2
#     y2     dy2/dx1  dy2/dx2
#
# What it is: a table (matrix) of partial derivatives.
# Why it matters: a neural-network layer often maps many input values to many
# output values.
# Practical use: PyTorch handles it. For now, remember the concept only.


# ---------------------------------------------------------------------------
# COMMON MISTAKES TO AVOID
# ---------------------------------------------------------------------------
#
# 1. Error order matters:
#       error = prediction - target
#    Negative error means prediction is too low.
#    Positive error means prediction is too high.
#
# 2. A negative gradient is not bad.
#    It means increasing that parameter reduces loss because updates subtract
#    the gradient.
#
# 3. Do not update a weight before calculating the other gradients for the same
#    pass. Calculate all gradients using the old values, then update together.
#
# 4. A larger gradient does not mean "better." It means the loss is more
#    sensitive to that parameter at this moment. Learning rate keeps changes safe.
#
# 5. Backpropagation does not update weights by itself.
#    Backpropagation CALCULATES gradients. Gradient descent, Adam, or another
#    optimizer USES those gradients to update parameters.


def print_examples() -> None:
    """Run the examples from this lesson."""
    print("EXAMPLE 1: one weight, prediction too low")
    prediction, error, loss, gradient, new_w = one_weight_step(3, 2, 10, 0.01)
    print(f"  prediction={prediction}, error={error}, loss={loss}")
    print(f"  gradient={gradient}; w changes from 2 to {new_w:.2f}\n")

    print("EXAMPLE 2: one weight, prediction too high")
    prediction, error, loss, gradient, new_w = one_weight_step(3, 4, 10, 0.01)
    print(f"  prediction={prediction}, error={error}, loss={loss}")
    print(f"  gradient={gradient}; w changes from 4 to {new_w:.2f}\n")

    print("EXAMPLE 3: train one neuron: prediction = w*x+b")
    train_one_neuron(3, 2.0, 1.0, 10, 0.01, 5)
    print()

    print("EXAMPLE 4: two inputs")
    result = two_input_step(2, 4, 1.0, 1.0, 0.0, 10, 0.01)
    prediction, loss, g1, g2, gb, w1, w2, b = result
    print(f"  prediction={prediction}, loss={loss}")
    print(f"  gradients: w1={g1}, w2={g2}, b={gb}")
    print(f"  updated: w1={w1:.2f}, w2={w2:.2f}, b={b:.2f}\n")

    print("EXAMPLE 5: two-layer chain")
    h, prediction, loss, gv, gw, new_w, new_v = two_layer_chain_step(
        3, 2.0, 2.0, 10, 0.01
    )
    print(f"  h={h}, prediction={prediction}, loss={loss}")
    print(f"  v gradient={gv}, earlier w gradient={gw}")
    print(f"  updated: w={new_w:.2f}, v={new_v:.2f}")


if __name__ == "__main__":
    print_examples()


# FINAL SUMMARY TO REMEMBER
# -------------------------
#
# Backpropagation asks:
#     "How much did each weight contribute to the final loss?"
#
# Gradient answers for each weight:
#     "Move this weight up/down, and this is how strongly."
#
# Update applies the instruction slowly:
#     weight = weight - learning_rate * gradient
#
# One-layer gradient:
#     gradient = loss signal * input
#
# Earlier-layer gradient:
#     gradient = loss signal * every effect along the path back to that weight
#
# This is why the process is called back-propagation: the learning instruction
# travels backward through the calculation graph.


#Why this matters for a neural network

import random

random.seed(42)

w = random.gauss(0, 1)
b = random.gauss(0, 1)
lr = 0.01

xs = [1.0, 2.0, 3.0, 4.0, 5.0]
ys = [3.0, 5.0, 7.0, 9.0, 11.0]

for epoch in range(200):
    total_loss = 0
    dw = 0
    db = 0
    for x, y in zip(xs, ys):
        pred = w * x + b
        error = pred - y
        total_loss += error ** 2
        dw += 2 * error * x
        db += 2 * error
    dw /= len(xs)
    db /= len(xs)
    total_loss /= len(xs)
    w -= lr * dw
    b -= lr * db
    if epoch % 40 == 0 or epoch == 199:
        if epoch < 5 or epoch % 40 == 0 or epoch == 199:
            print(f"epoch {epoch:3d}  w={w:.4f}  b={b:.4f}  loss={total_loss:.6f}")

print(f"\nLearned: y = {w:.2f}x + {b:.2f}")
print(f"Actual:  y = 2x + 1")