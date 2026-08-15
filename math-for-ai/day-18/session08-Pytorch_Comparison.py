"""
Lesson 5 — Comparing Our Autograd Idea with PyTorch

Goal:
Show that our tiny Value engine and PyTorch autograd follow the same
fundamental mathematics:
- operations build a computation graph
- backward traverses it in reverse
- chain rule computes gradients

This file requires PyTorch to be installed.
"""

try:
    import torch
except ImportError:
    torch = None


if torch is None:
    print("PyTorch is not installed in this environment.")
    print("Install it separately if you want to run this comparison.")
else:
    # Example:
    #
    # y = ReLU(x1*x2 + 1)
    #
    # x1 = 2
    # x2 = 3
    #
    # Expected:
    # dy/dx1 = x2 = 3
    # dy/dx2 = x1 = 2
    #
    # because x1*x2 + 1 = 7 > 0,
    # so ReLU is locally the identity.

    x1 = torch.tensor(2.0, requires_grad=True)
    x2 = torch.tensor(3.0, requires_grad=True)

    a = x1 * x2
    b = a + 1.0
    y = torch.relu(b)

    y.backward()

    print("PyTorch gradients:")
    print("dy/dx1 =", x1.grad.item())
    print("dy/dx2 =", x2.grad.item())

    # requires_grad=True means:
    # Track operations involving this tensor because we may later
    # ask for gradients.

    print("\nComputation graph functions:")
    print("a.grad_fn =", a.grad_fn)
    print("b.grad_fn =", b.grad_fn)
    print("y.grad_fn =", y.grad_fn)

    # You may see names similar to:
    # MulBackward0
    # AddBackward0
    # ReluBackward0
    #
    # That is PyTorch's autograd graph showing through.
