"""
LESSON 5 — PART 07
MORE OPERATIONS: NEGATION, SUBTRACTION, POWER, DIVISION, EXP, LOG

============================================================
BIG IDEA: COMPOSITION
============================================================

Autodiff becomes powerful because many operations can be built from
simpler operations we already know.

Then the chain rule automatically gives the correct gradient.

============================================================
NEGATION
============================================================

    -x = x * (-1)

So we can implement negation using multiplication.

Derivative:

    d(-x)/dx = -1

No special new autograd machinery is needed.

============================================================
SUBTRACTION
============================================================

    x - y = x + (-y)

So subtraction can reuse:

- addition
- negation

Derivative:

    d(x-y)/dx = +1
    d(x-y)/dy = -1

============================================================
POWER
============================================================

For:

    y = x^n

power rule:

    dy/dx = n*x^(n-1)

In autograd:

    x.grad += n*x^(n-1) * y.grad

Important distinction:

Forward value:
    x^n

Backward local derivative:
    n*x^(n-1)

Do not confuse them.

============================================================
DIVISION
============================================================

We can rewrite:

    x / y
      =
    x * y^(-1)

So division reuses:

- multiplication
- power

Example:

    z = x/y

Gradients:

    dz/dx = 1/y
    dz/dy = -x/y^2

============================================================
EXPONENTIAL
============================================================

    y = e^x

Special derivative:

    dy/dx = e^x

The function is its own derivative.

AI relevance:
exp appears in softmax and probability-related computations.

============================================================
LOGARITHM
============================================================

Natural log:

    y = log(x)

Derivative:

    dy/dx = 1/x

exp and log are inverse operations:

    log(e^x) = x
    e^(log x) = x

AI relevance:
log appears in:

- negative log-likelihood
- cross entropy
- probability losses
- language-model training objectives

Example intuition:

If correct-class probability is high:
    -log(p) is small

If correct-class probability is tiny:
    -log(p) is large

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
        out = Value(self.data**n, (self,), f'**{n}')

        def _backward():
            self.grad += n * self.data**(n-1) * out.grad

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
            self.grad += (1/self.data) * out.grad

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


x = Value(8.0)
y = Value(4.0)
z = x / y
z.backward()

print("Division:")
print("z =", z.data)
print("x.grad =", x.grad)
print("y.grad =", y.grad)
