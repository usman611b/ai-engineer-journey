"""
Lesson 5: Chain Rule & Automatic Differentiation
================================================

Scope of these notes
------------------------------------------------
These notes cover everything learned from the start of Lesson 5 up to the
point just BEFORE topological sort implementation.

Covered topics:
1. Chain Rule intuition
2. Chain Rule with actual functions
3. Chain Rule inside a neural network
4. Computational graphs
5. Forward pass vs backward pass
6. Why gradients flow backward
7. Automatic differentiation: forward mode vs reverse mode
8. Building the Value class
9. Recording graph history with _prev and _op
10. Addition with operator overloading
11. Addition backward logic
12. Why gradients accumulate with +=
13. Multiplication and its backward rule
14. Combining operations manually
15. Why backward order matters

STOP POINT:
We do NOT implement topological sort in this file.
That is where the next study session should continue.

This file is intentionally very detailed and beginner-friendly.
You can run it directly with Python.
"""


# ============================================================
# 1. CHAIN RULE INTUITION
# ============================================================

"""
A derivative tells us how much an output changes when an input changes.

Example:
    y = x^2
    dy/dx = 2x

At x = 3:
    dy/dx = 6

Meaning:
    Around x = 3, a very small change in x produces roughly 6 times that
    change in y.

The chain rule is needed when one variable affects another variable through
intermediate steps.

Suppose:
    x -> a -> y

If:
    da/dx = 3
and:
    dy/da = 4

then:
    dy/dx = (dy/da) * (da/dx)
          = 4 * 3
          = 12

Mental model:
    If A affects B, and B affects C, multiply the local effects to get the
    total effect of A on C.
"""


def chain_rule_simple_demo():
    local_1 = 4
    local_2 = 3
    local_3 = 2
    total = local_1 * local_2 * local_3
    print("Chain rule simple demo:")
    print(f"4 * 3 * 2 = {total}")
    print()


# ============================================================
# 2. CHAIN RULE WITH ACTUAL FUNCTIONS
# ============================================================

"""
Example:
    y = (x^2 + 1)^2

Break it into smaller functions:
    a = x^2 + 1
    y = a^2

At x = 2:
    a = 2^2 + 1 = 5
    y = 5^2 = 25

Local derivatives:
    da/dx = 2x = 4
    dy/da = 2a = 10

Chain rule:
    dy/dx = (dy/da) * (da/dx)
          = 10 * 4
          = 40

Interpretation:
    Around x = 2, a tiny change in x changes y at roughly 40 times that rate.
"""


def chain_rule_function_demo(x=2.0):
    a = x ** 2 + 1
    y = a ** 2

    da_dx = 2 * x
    dy_da = 2 * a
    dy_dx = dy_da * da_dx

    print("Chain rule with actual functions:")
    print(f"x = {x}")
    print(f"a = x^2 + 1 = {a}")
    print(f"y = a^2 = {y}")
    print(f"da/dx = {da_dx}")
    print(f"dy/da = {dy_da}")
    print(f"dy/dx = {dy_dx}")
    print()


"""
Second worked example:
    a = x^2
    y = a^3
    x = 2

Forward:
    a = 4
    y = 64

Derivatives:
    da/dx = 2x = 4
    dy/da = 3a^2 = 3 * 16 = 48

Therefore:
    dy/dx = 48 * 4 = 192

Direct verification:
    y = (x^2)^3 = x^6
    dy/dx = 6x^5
    at x = 2 -> 6 * 32 = 192
"""


# ============================================================
# 3. CHAIN RULE INSIDE A NEURAL NETWORK
# ============================================================

"""
A tiny neuron can be written as:
    z = w*x + b
    a = activation(z)
    L = loss(a, target)

For a simple identity activation a = z and squared loss:
    L = (a - y)^2

The weight w does not directly touch the loss.
Its path is:
    w -> z -> a -> L

So:
    dL/dw = (dL/da) * (da/dz) * (dz/dw)

This is the chain rule inside neural-network training.

Example:
    x = 2
    w = 3
    b = 1
    a = z
    target y = 5

Forward:
    z = 3*2 + 1 = 7
    a = 7
    L = (7 - 5)^2 = 4

Backward:
    dL/da = 2(a-y) = 4
    da/dz = 1
    dz/dw = x = 2

So:
    dL/dw = 4 * 1 * 2 = 8

Gradient descent then uses this gradient:
    w_new = w_old - learning_rate * dL/dw

Important distinction:
    Gradient = information about how loss changes with a parameter.
    Gradient descent = the optimization rule that USES that gradient.
"""


def tiny_neuron_demo():
    x = 2.0
    w = 3.0
    b = 1.0
    target = 5.0

    z = w * x + b
    a = z
    loss = (a - target) ** 2

    dL_da = 2 * (a - target)
    da_dz = 1.0
    dz_dw = x
    dL_dw = dL_da * da_dz * dz_dw

    lr = 0.01
    w_new = w - lr * dL_dw

    print("Chain rule inside a tiny neuron:")
    print(f"z = {z}")
    print(f"loss = {loss}")
    print(f"dL/dw = {dL_dw}")
    print(f"updated w with lr={lr}: {w_new}")
    print()


# ============================================================
# 4. COMPUTATIONAL GRAPHS
# ============================================================

"""
A computational graph breaks a larger expression into small operations.

Example:
    y = x1*x2 + 1

Break into:
    a = x1*x2
    y = a + 1

Graph:

    x1 ----\
            (*) ---> a ----\
    x2 ----/           (+) ---> y
                     1 ----/

Forward direction:
    inputs -> intermediate values -> output

Backward direction:
    output -> intermediate gradients -> input gradients

Why record the graph?
A normal Python float only stores its final number.
It does not remember:
    - which values created it
    - which operation created it
    - how to propagate gradients backward

Autograd systems therefore wrap numbers in richer objects.
"""


# ============================================================
# 5. FORWARD PASS VS BACKWARD PASS
# ============================================================

"""
Forward pass:
    Calculates values, predictions, and loss.

Backward pass:
    Calculates gradients.

Training loop conceptually:
    1. Clear old gradients
    2. Forward pass
    3. Compute loss
    4. Backward pass
    5. Update parameters
    6. Repeat

Important:
    backward() does NOT update weights.
    backward() only computes gradients.

The optimizer/update rule uses those gradients afterward.
"""


# ============================================================
# 6. WHY GRADIENTS FLOW BACKWARD
# ============================================================

"""
Neural networks often have many parameters and one scalar loss.

Example:
    w1, w2, ..., wn -> network -> L

We want:
    dL/dw1, dL/dw2, ..., dL/dwn

Reverse-mode differentiation starts from:
    dL/dL = 1

and propagates gradient information backward.

At every node:
    parent_gradient += local_derivative * upstream_gradient

Mental model:
    Each node receives a gradient message from later in the graph,
    multiplies it by its local derivative, then passes the result backward.
"""


# ============================================================
# 7. FORWARD-MODE VS REVERSE-MODE AUTODIFF
# ============================================================

"""
Automatic differentiation (autodiff):
    Automatically applies derivative rules and the chain rule through a
    computational graph.

It is NOT the same as finite differences.

Finite differences:
    Approximate derivative by perturbing x.

Autodiff:
    Uses exact local derivative formulas and chain-rule composition.

Forward mode:
    Seed input derivative:
        dx/dx = 1
    Push derivatives forward.
    Best when there are few inputs and many outputs.

Reverse mode:
    Seed output gradient:
        dL/dL = 1
    Pull gradients backward.
    Best when there are many inputs/parameters and few outputs.

Neural-network training is usually:
    many parameters -> one scalar loss

So reverse-mode autodiff is the natural fit.
"""


# ============================================================
# 8. BUILDING THE VALUE CLASS
# ============================================================

"""
A Value object needs to store at least:

    data
        The numeric value from the forward pass.

    grad
        The derivative of the final output/loss with respect to this Value.
        For a weight w:
            w.grad = dL/dw

Initially grad = 0.0 because backpropagation has not run yet.
"""


class Value:
    def __init__(self, data, children=(), op=''):
        self.data = data
        self.grad = 0.0

        # Default backward function for leaf/original values.
        # It does nothing because an original value has no previous operation
        # to propagate through.
        self._backward = lambda: None

        # Previous Values used to create this Value.
        self._prev = set(children)

        # Operation that created this Value, for example '+' or '*'.
        self._op = op

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    # ========================================================
    # 9. ADDITION WITH GRAPH RECORDING
    # ========================================================
    def __add__(self, other):
        # Allow expressions like Value(2.0) + 3
        other = other if isinstance(other, Value) else Value(other)

        # Forward pass:
        # calculate the numeric result and record graph history.
        out = Value(
            self.data + other.data,
            (self, other),
            '+'
        )

        # Backward rule for addition:
        # If out = self + other, then:
        #   dout/dself = 1
        #   dout/dother = 1
        #
        # By chain rule:
        #   dL/dself  += dL/dout * 1
        #   dL/dother += dL/dout * 1
        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        # Attach the local backward logic to the output node.
        out._backward = _backward

        return out

    # Lets normal numbers work on the left side, e.g. 3 + value
    def __radd__(self, other):
        return self + other

    # ========================================================
    # 10. MULTIPLICATION WITH GRAPH RECORDING
    # ========================================================
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)

        # Forward pass
        out = Value(
            self.data * other.data,
            (self, other),
            '*'
        )

        # Backward rule for multiplication:
        # If out = self * other, then:
        #   dout/dself  = other.data
        #   dout/dother = self.data
        #
        # Chain rule:
        #   dL/dself  += other.data * dL/dout
        #   dL/dother += self.data  * dL/dout
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward

        return out

    # Lets normal numbers work on the left side, e.g. 3 * value
    def __rmul__(self, other):
        return self * other


# ==================================================================
# 11. WHY _prev AND _op MATTER
# ===============================================================

"""
Suppose:
    x = Value(4)
    y = Value(3)
    a = x * y
    b = a + 5

Then conceptually:

    a.data  = 12
    a._prev = {x, y}
    a._op   = '*'

    b.data  = 17
    b._prev = {a, Value(5)}
    b._op   = '+'

This is how the computational graph is stored inside the objects themselves.
"""


# ============================================================
# 12. WHY GRADIENTS USE += INSTEAD OF =
# ============================================================

"""
A variable can influence the final output through more than one path.

Example:
    y = x + x + x

Mathematically:
    y = 3x
    dy/dx = 3

Each path contributes gradient 1.
So x must accumulate:
    1 + 1 + 1 = 3

That is why backward rules use:
    x.grad += contribution

instead of:
    x.grad = contribution

Using '=' would overwrite previous gradient contributions and produce wrong
results when a node is reused in multiple places.
"""


# ============================================================
# 13. MANUAL BACKWARD EXAMPLES
# ============================================================


def addition_backward_demo():
    a = Value(4.0)
    b = Value(6.0)
    c = a + b

    # Seed the output gradient.
    # dc/dc = 1
    c.grad = 1.0

    # Manually run c's local backward rule.
    c._backward()

    print("Addition backward demo:")
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("c._prev:", c._prev)
    print("c._op:", c._op)
    print()



def repeated_addition_demo():
    x = Value(5.0)

    # Python groups this as:
    #   a = x + x
    #   z = a + x
    a = x + x
    z = a + x

    # Seed final output gradient.
    z.grad = 1.0

    # IMPORTANT:
    # We still do backward manually because automatic graph traversal has not
    # been implemented yet.
    z._backward()
    a._backward()

    print("Repeated addition demo: y = x + x + x")
    print("x.grad should be 3.0")
    print("x:", x)
    print("a:", a)
    print("z:", z)
    print()



def multiplication_backward_demo():
    x = Value(3.0)
    y = Value(5.0)
    z = x * y

    # In this example we intentionally set an upstream gradient of 2.
    z.grad = 2.0
    z._backward()

    print("Multiplication backward demo:")
    print("Expected x.grad = 5 * 2 = 10")
    print("Expected y.grad = 3 * 2 = 6")
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("z._prev:", z._prev)
    print("z._op:", z._op)
    print()


# ============================================================
# 14. COMBINING OPERATIONS MANUALLY
# ============================================================

"""
Consider:
    a = x * y
    z = a + x

With:
    x = 2
    y = 3

Forward:
    a = 6
    z = 8

Graph:

    x=2 ----\
             (*) ---> a=6 ----\
    y=3 ----/                  (+) ---> z=8
    x=2 ----------------------/

Backward:
    z.grad = 1

First run z._backward():
    a.grad += 1
    x.grad += 1

Then run a._backward():
    x.grad += y.data * a.grad = 3 * 1 = 3
    y.grad += x.data * a.grad = 2 * 1 = 2

Final:
    x.grad = 1 + 3 = 4
    y.grad = 2

Manual derivative check:
    z = x*y + x
    dz/dx = y + 1 = 3 + 1 = 4
    dz/dy = x = 2
"""


def combined_graph_demo_correct_order():
    x = Value(2.0)
    y = Value(3.0)

    a = x * y
    z = a + x

    z.grad = 1.0

    # Correct manual backward order:
    # final output first, then earlier node.
    z._backward()
    a._backward()

    print("Combined graph with correct manual backward order:")
    print("x.grad expected 4.0 ->", x.grad)
    print("y.grad expected 2.0 ->", y.grad)
    print("a.grad expected 1.0 ->", a.grad)
    print("z.grad expected 1.0 ->", z.grad)
    print()


# ============================================================
# 15. WHY BACKWARD ORDER MATTERS
# ============================================================

"""
This is the final concept before topological sort.

Suppose:
    a = x * y
    z = a + x

Initially:
    z.grad = 1
    a.grad = 0
    x.grad = 0
    y.grad = 0

Correct order:
    1. z._backward()
       -> gives a.grad = 1
    2. a._backward()
       -> now multiplication has the correct upstream gradient to use

Wrong order:
    1. a._backward()
       -> a.grad is still 0
       -> so it sends zero to x and y
    2. z._backward()
       -> only afterward does a.grad become 1
       -> too late, because a._backward() already ran

Core rule:
    A node must receive its COMPLETE gradient before it propagates that
    gradient farther backward.

For a chain:
    x -> a -> b -> L

Backward must be:
    L -> b -> a -> x

NOT:
    x -> a -> b -> L

This ordering problem becomes harder when graphs branch and reuse nodes.
That is exactly why the next topic is TOPOLOGICAL SORT.

STOP HERE FOR TODAY.
"""


def wrong_backward_order_demo():
    x = Value(2.0)
    y = Value(3.0)

    a = x * y
    z = a + x

    z.grad = 1.0

    # WRONG ORDER ON PURPOSE
    a._backward()  # a.grad is still 0 here
    z._backward()  # a.grad becomes 1 only after this

    print("Wrong backward order demo:")
    print("These gradients are incomplete/wrong because a._backward() ran too early.")
    print("x:", x)
    print("y:", y)
    print("a:", a)
    print("z:", z)
    print()


# ============================================================
# RUN ALL DEMOS
# ============================================================


if __name__ == "__main__":
    print("=" * 70)
    print("LESSON 5 NOTES: CHAIN RULE & AUTODIFF — BEFORE TOPOLOGICAL SORT")
    print("=" * 70)
    print()

    chain_rule_simple_demo()
    chain_rule_function_demo()
    tiny_neuron_demo()
    addition_backward_demo()
    repeated_addition_demo()
    multiplication_backward_demo()
    combined_graph_demo_correct_order()
    wrong_backward_order_demo()

    print("Next study session:")
    print("Topological Sort -> automatic backward() traversal")
