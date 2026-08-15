"""
LESSON 5 — PART 11
GRADIENT CHECKING

============================================================
WHY GRADIENT CHECKING?
============================================================

We wrote our own backward rules.

But how do we know they are correct?

A bug in a derivative can cause:

    forward pass correct
         ↓
    backward gradients wrong
         ↓
    wrong parameter updates
         ↓
    training failure

Gradient checking compares TWO independent derivative calculations:

1. AUTODIFF gradient
2. NUMERICAL finite-difference gradient

============================================================
NUMERICAL DERIVATIVE
============================================================

Central difference:

    f'(x)
      ≈
    [f(x+h) - f(x-h)] / (2h)

This is an approximation.

============================================================
AUTODIFF VS NUMERICAL
============================================================

Autodiff uses known derivative rules + chain rule.

Numerical differentiation perturbs x and measures output change.

If both answers are extremely close,
our backward implementation is likely correct.

============================================================
DO THEY HAVE TO BE EXACTLY IDENTICAL?
============================================================

NO.

Example:

    autodiff = 4.000001
    numerical = 3.999999

Difference:

    0.000002 = 2e-6

This is tiny.

Floating-point arithmetic and finite-difference approximation cause small differences.

So we usually ask:

    Is the difference SMALL ENOUGH?

For this lesson:

    difference < 1e-5

is a reasonable simple check.

============================================================
EXAMPLE: x^2 at x=3
============================================================

Exact derivative:

    d(x^2)/dx = 2x
    = 6

Numerical derivative will produce approximately 6.

============================================================
COMPLEX EXAMPLE
============================================================

    y = tanh(x^3 + 2x + 1)

At x=2:

inner:
    8 + 4 + 1 = 13

tanh(13) ≈ 1

Derivative of tanh:
    1 - tanh^2(13)

This is extremely close to 0 because tanh is saturated.

Inner derivative:
    3x^2 + 2
    at x=2:
    14

Total derivative:
    [1 - tanh^2(13)] * 14

which is extremely tiny.

This also demonstrates vanishing-gradient intuition.
"""
"""
Lesson 5 — Gradient Checking

Question:
How do we know our homemade backward rules are correct?

Answer:
Compare autodiff gradients against numerical finite differences.

Autodiff:
    exact derivative rules + chain rule

Numerical derivative:
    approximation by perturbing the input

Central-difference formula:

    f'(x) ≈ [f(x+h) - f(x-h)] / (2h)

The two values do NOT need to be exactly identical.
They should be extremely close.
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
        return f"Value(data={self.data:.8f}, grad={self.grad:.8f})"

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

    def __pow__(self, n):
        out = Value(self.data ** n, (self,), f'**{n}')

        def _backward():
            self.grad += n * (self.data ** (n - 1)) * out.grad

        out._backward = _backward
        return out

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), 'tanh')

        def _backward():
            self.grad += (1 - t ** 2) * out.grad

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


def gradient_check(build_expr, x_val, h=1e-7):
    # 1. Autodiff gradient
    x = Value(x_val)
    y = build_expr(x)
    y.backward()

    autodiff_grad = x.grad

    # 2. Numerical gradient
    y_plus = build_expr(Value(x_val + h)).data
    y_minus = build_expr(Value(x_val - h)).data

    numerical_grad = (y_plus - y_minus) / (2 * h)

    # 3. Difference
    diff = abs(autodiff_grad - numerical_grad)

    return autodiff_grad, numerical_grad, diff


# ------------------------------------------------------------
# Simple example: x^2 at x=3
# ------------------------------------------------------------

def square(x):
    return x ** 2

ad, num, diff = gradient_check(square, 3.0)

print("x^2 at x=3")
print(f"Autodiff:  {ad:.8f}")
print(f"Numerical: {num:.8f}")
print(f"Difference:{diff:.2e}")

# ------------------------------------------------------------
# More complex expression
# ------------------------------------------------------------

# y = tanh(x^3 + 2x + 1)

def expr(x):
    return (x ** 3 + 2 * x + 1).tanh()

ad, num, diff = gradient_check(expr, 0.5)

print("\nComplex expression at x=0.5")
print(f"Autodiff:  {ad:.8f}")
print(f"Numerical: {num:.8f}")
print(f"Difference:{diff:.2e}")

# ------------------------------------------------------------
# Same expression at x=2
# ------------------------------------------------------------

# At x=2:
# inner = x^3 + 2x + 1 = 13
#
# tanh(13) is almost 1, so:
# tanh'(13) = 1 - tanh(13)^2
# is extremely small.
#
# This naturally demonstrates tanh saturation / vanishing-gradient intuition.

ad, num, diff = gradient_check(expr, 2.0)

print("\nComplex expression at x=2")
print(f"Autodiff:  {ad:.12e}")
print(f"Numerical: {num:.12e}")
print(f"Difference:{diff:.2e}")

# Practical rule from this lesson:
# If the difference is very small, e.g. < 1e-5,
# the backward implementation is likely correct.


import math

def numerical_derivative(f, x, h=1e-7):
    return (f(x+h) - f(x-h)) / (2*h)

def f(x):
    return x**2

print("Numerical derivative x^2 at 3:", numerical_derivative(f,3.0))

def expr(x):
    return math.tanh(x**3 + 2*x + 1)

print("Numerical complex grad at 2:", numerical_derivative(expr,2.0))


