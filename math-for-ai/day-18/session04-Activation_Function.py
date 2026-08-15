"""
LESSON 5 — PART 08
ACTIVATION FUNCTIONS: WHY THEY EXIST, TANH, RELU

============================================================
THE MOST IMPORTANT QUESTION:
WHY DO NEURAL NETWORKS NEED ACTIVATION FUNCTIONS?
============================================================

A neuron first computes a weighted sum:

    a = w1*x1 + w2*x2 + ... + b

This is the RAW / PRE-ACTIVATION value.

If we stop there, the neuron is linear.

Now imagine stacking linear layers:

    a = W1*x + b1
    y = W2*a + b2

Substitute a:

    y = W2*(W1*x + b1) + b2

This simplifies to another linear transformation:

    y = W*x + B

So even many linear layers can collapse into one linear function.

That means the network cannot represent sufficiently complex nonlinear patterns.

ACTIVATION FUNCTIONS solve this by introducing NON-LINEARITY.

============================================================
TANH
============================================================

tanh maps any real input into approximately:

    (-1, +1)

Examples:

    tanh(-5) ≈ -1
    tanh(0)  = 0
    tanh(5)  ≈ +1

Main reason we use it here:
    NON-LINEARITY

The bounded range is useful too, but it is not the fundamental reason.

Our XOR targets use -1/+1, which fits naturally with tanh.

============================================================
TANH DERIVATIVE
============================================================

If:

    y = tanh(x)

then:

    dy/dx = 1 - tanh^2(x)

Since y = tanh(x), we can also write:

    dy/dx = 1 - y^2

That is why the backward code uses:

    1 - t**2

where t is the already-computed tanh output.

============================================================
WHY TANH DERIVATIVE MATTERS
============================================================

Forward:
    tanh introduces non-linearity

Backward:
    tanh derivative allows gradients to pass through the activation

Example:
    x=1
    tanh(1)≈0.7616

local derivative:
    1 - 0.7616^2 ≈ 0.42

If upstream gradient is 2:

    input gradient = 0.42 × 2 = 0.84

============================================================
TANH SATURATION / VANISHING GRADIENT INTUITION
============================================================

Near x=0:
    tanh(0)=0
    derivative=1
    gradient passes strongly

For large |x|:
    tanh(x) approaches ±1
    derivative approaches 0
    gradient becomes tiny

Repeated tiny derivatives through deep networks can contribute to
vanishing-gradient problems.

============================================================
RELU
============================================================

ReLU:

    ReLU(x) = max(0,x)

Meaning:

    negative input -> 0
    positive input -> unchanged

Derivative:

    0 for negative input
    1 for positive input

So:

positive input:
    gradient passes

negative input:
    gradient is blocked

ReLU also introduces non-linearity.

============================================================
CODE
============================================================
"""

import math

class Value:
    def __init__(self, data, children=(), op=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(children)
        self._op = op

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), 'tanh')

        def _backward():
            self.grad += (1 - t**2) * out.grad

        out._backward = _backward
        return out

    def relu(self):
        out = Value(max(0, self.data), (self,), 'relu')

        def _backward():
            local = 1.0 if out.data > 0 else 0.0
            self.grad += local * out.grad

        out._backward = _backward
        return out


x = Value(1.0)
y = x.tanh()
y.grad = 1.0
y._backward()

print("tanh output:", y.data)
print("tanh input grad:", x.grad)

x = Value(-4.0)
y = x.relu()
y.grad = 3.0
y._backward()

print("ReLU negative input grad:", x.grad)
