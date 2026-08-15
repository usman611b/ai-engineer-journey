"""
LESSON 5 — PART 09
NEURON → LAYER → MLP

============================================================
ONE ARTIFICIAL NEURON
============================================================

A neuron receives inputs:

    x1, x2, ...

Each input has a weight:

    w1, w2, ...

The neuron computes:

    a = w1*x1 + w2*x2 + ... + b

Then applies activation:

    y = tanh(a)

============================================================
WHAT IS A WEIGHT?
============================================================

A weight is a learnable number controlling how strongly an input influences
the neuron.

Positive weight:
    pushes raw activation in positive direction

Negative weight:
    pushes it in negative direction

The correct weights are not known initially.

We start randomly and training adjusts them.

============================================================
WHAT IS BIAS?
============================================================

Bias is another learnable parameter.

It lets the neuron shift its activation independently of the weighted inputs.

Weights + bias are the parameters the network learns.

============================================================
WHY ARE WEIGHTS Value OBJECTS?
============================================================

Because each weight needs:

    data = current parameter value
    grad = dLoss/dWeight

Then gradient descent can update:

    weight.data -= learning_rate * weight.grad

============================================================
WHY RANDOM INITIALIZATION?
============================================================

The network starts without knowing the correct solution.

Random values provide a starting point.

Training repeatedly:

    predicts
    calculates loss
    computes gradients
    updates weights

============================================================
WHAT IS A LAYER?
============================================================

A layer is just multiple neurons receiving the SAME input.

Example:

    input [x1,x2]
       ↓
    neuron 1 -> h1
    neuron 2 -> h2
    neuron 3 -> h3
    neuron 4 -> h4

Output:

    [h1,h2,h3,h4]

Each neuron has its own weights and bias.

============================================================
WHY MULTIPLE NEURONS?
============================================================

Different neurons can learn different useful nonlinear responses/features
from the same input.

The next layer can combine those learned responses.

============================================================
WHAT IS AN MLP?
============================================================

MLP = Multi-Layer Perceptron

An MLP stacks layers.

Example:

    MLP([2,4,1])

means:

    2 input values
        ↓
    4 hidden neurons
        ↓
    1 output neuron

Equivalent layers:

    Layer(2,4)
    Layer(4,1)

============================================================
HOW DATA FLOWS THROUGH AN MLP
============================================================

Suppose:

    MLP([2,4,2,1])

Then number of values changes:

    2 values
      ↓ Layer(2,4)
    4 values
      ↓ Layer(4,2)
    2 values
      ↓ Layer(2,1)
    1 value

Each layer's outputs become the next layer's inputs.

============================================================
UNDERSTANDING THE CODE
============================================================

This compact code:

    Layer(sizes[i], sizes[i+1])

just takes neighboring architecture numbers.

For:

    sizes = [3,5,4,1]

it creates:

    Layer(3,5)
    Layer(5,4)
    Layer(4,1)

And this:

    for layer in self.layers:
        x = layer(x)

means:

    "pass the current values through the next layer,
     then replace x with that layer's outputs"

============================================================
PARAMETER COUNT
============================================================

For Layer(n_inputs, n_outputs):

Each neuron has:

    n_inputs weights + 1 bias

So total parameters:

    (n_inputs + 1) * n_outputs

For MLP([2,4,1]):

Layer(2,4):
    (2+1)*4 = 12

Layer(4,1):
    (4+1)*1 = 5

Total:
    17 parameters
"""

import math
import random

class Value:
    def __init__(self, data, children=(), op=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(children)
        self._op = op

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), 'tanh')

        def _backward():
            self.grad += (1-t**2)*out.grad

        out._backward = _backward
        return out


class Neuron:
    def __init__(self, n_inputs):
        self.w = [Value(random.uniform(-1,1)) for _ in range(n_inputs)]
        self.b = Value(0.0)

    def __call__(self, x):
        act = sum((wi*xi for wi,xi in zip(self.w,x)), self.b)
        return act.tanh()

    def parameters(self):
        return self.w + [self.b]


class Layer:
    def __init__(self, n_inputs, n_outputs):
        self.neurons = [Neuron(n_inputs) for _ in range(n_outputs)]

    def __call__(self, x):
        return [n(x) for n in self.neurons]

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]


class MLP:
    def __init__(self, sizes):
        self.layers = [
            Layer(sizes[i], sizes[i+1])
            for i in range(len(sizes)-1)
        ]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x[0] if len(x)==1 else x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]


random.seed(42)
model = MLP([2,4,1])
print("Total parameters:", len(model.parameters()))
