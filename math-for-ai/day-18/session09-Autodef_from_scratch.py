"""
Lesson 5 — Clean Final Implementation

Minimal reverse-mode autograd engine + MLP + XOR training + gradient check.

This file is intentionally cleaner than the study-note files.
Use the numbered files for detailed explanations.
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

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"

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

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return other + (-self)

    def __pow__(self, n):
        out = Value(self.data ** n, (self,), f'**{n}')

        def _backward():
            self.grad += n * (self.data ** (n - 1)) * out.grad

        out._backward = _backward
        return out

    def __truediv__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return self * (other ** -1)

    def exp(self):
        e = math.exp(self.data)
        out = Value(e, (self,), 'exp')

        def _backward():
            self.grad += e * out.grad

        out._backward = _backward
        return out

    def log(self):
        out = Value(math.log(self.data), (self,), 'log')

        def _backward():
            self.grad += (1.0 / self.data) * out.grad

        out._backward = _backward
        return out

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), 'tanh')

        def _backward():
            self.grad += (1 - t ** 2) * out.grad

        out._backward = _backward
        return out

    def relu(self):
        out = Value(max(0, self.data), (self,), 'relu')

        def _backward():
            self.grad += (1.0 if out.data > 0 else 0.0) * out.grad

        out._backward = _backward
        return out

    def backward(self):
        topo = []
        visited = set()

        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for parent in v._prev:
                    build_topo(parent)
                topo.append(v)

        build_topo(self)

        self.grad = 1.0

        for v in reversed(topo):
            v._backward()


class Neuron:
    def __init__(self, n_inputs):
        self.w = [
            Value(random.uniform(-1, 1))
            for _ in range(n_inputs)
        ]
        self.b = Value(0.0)

    def __call__(self, x):
        act = sum(
            (wi * xi for wi, xi in zip(self.w, x)),
            self.b
        )
        return act.tanh()

    def parameters(self):
        return self.w + [self.b]


class Layer:
    def __init__(self, n_inputs, n_outputs):
        self.neurons = [
            Neuron(n_inputs)
            for _ in range(n_outputs)
        ]

    def __call__(self, x):
        return [n(x) for n in self.neurons]

    def parameters(self):
        return [
            p
            for n in self.neurons
            for p in n.parameters()
        ]


class MLP:
    def __init__(self, sizes):
        self.layers = [
            Layer(sizes[i], sizes[i + 1])
            for i in range(len(sizes) - 1)
        ]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x[0] if len(x) == 1 else x

    def parameters(self):
        return [
            p
            for layer in self.layers
            for p in layer.parameters()
        ]


def gradient_check(build_expr, x_val, h=1e-7):
    x = Value(x_val)
    y = build_expr(x)
    y.backward()

    autodiff_grad = x.grad

    y_plus = build_expr(Value(x_val + h)).data
    y_minus = build_expr(Value(x_val - h)).data

    numerical_grad = (y_plus - y_minus) / (2 * h)

    diff = abs(autodiff_grad - numerical_grad)

    return autodiff_grad, numerical_grad, diff


def train_xor(steps=100, lr=0.05, seed=42):
    random.seed(seed)

    model = MLP([2, 4, 1])

    xs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    ys = [-1, 1, 1, -1]

    for step in range(steps):
        preds = [model(x) for x in xs]

        loss = sum(
            (p - y) ** 2
            for p, y in zip(preds, ys)
        )

        for p in model.parameters():
            p.grad = 0.0

        loss.backward()

        for p in model.parameters():
            p.data -= lr * p.grad

        if step % 20 == 0:
            print(f"step {step:3d}  loss = {loss.data:.4f}")

    print("\nPredictions after training:")

    for x, target in zip(xs, ys):
        pred = model(x)
        print(
            f"input={x} "
            f"target={target:+d} "
            f"prediction={pred.data:+.3f}"
        )

    return model


if __name__ == "__main__":
    # XOR demo
    train_xor()

    # Gradient-check demo
    def expr(x):
        return (x ** 3 + 2 * x + 1).tanh()

    ad, num, diff = gradient_check(expr, 0.5)

    print("\nGradient check:")
    print(f"Autodiff:  {ad:.8f}")
    print(f"Numerical: {num:.8f}")
    print(f"Difference:{diff:.2e}")
