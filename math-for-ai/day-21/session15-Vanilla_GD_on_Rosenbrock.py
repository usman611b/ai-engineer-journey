"""
DAY 21 — SESSION 15: VANILLA GRADIENT DESCENT ON ROSENBROCK
===========================================================

LEARNING GOALS
--------------
This session combines the Rosenbrock loss, analytical gradient, a reusable
GradientDescent class, a complete optimization loop, history tracking,
divergence checks, and a first-step dry run.

1. THE UPDATE RULE
------------------
For each parameter p_i with gradient g_i:

    p_i,new = p_i,old - learning_rate*g_i

For Rosenbrock:

    x_new = x - lr*df/dx
    y_new = y - lr*df/dy

The two updates use matching entries. params=[x,y] and grads=[df/dx,df/dy].

2. WHAT THE OPTIMIZER KNOWS
---------------------------
The GradientDescent class does not know the Rosenbrock equation, the minimum
(1,1), or what x and y mean. It receives parameter and gradient lists and
performs the update rule. This separation lets the same optimizer work with a
different differentiable loss.

3. ONE FIRST-STEP DRY RUN
-------------------------
Start at:

    params=[-1.5,1.5]

The loss is:

    (1-(-1.5))^2 + 100*(1.5-(-1.5)^2)^2
    = 6.25 + 100*(-0.75)^2
    = 62.5

The gradient is:

    df/dx=-455
    df/dy=-150

With lr=0.0005:

    x_new=-1.5-0.0005*(-455)=-1.2725
    y_new= 1.5-0.0005*(-150)= 1.575

Negative gradients cause increases because subtracting a negative value adds.

4. ORDER OF OPERATIONS
----------------------
Each iteration performs:

    loss  = loss_function(current_params)
    grads = gradient_function(current_params)
    new_params = optimizer.step(current_params, grads)

At the next iteration, both loss and gradient are recalculated at the new
location. Reusing an old gradient would pretend the slope never changes.

5. WHY ASSIGN THE RETURN VALUE?
-------------------------------
This educational optimizer returns a new list. Therefore:

    params = optimizer.step(params, grads)

is essential. Calling step without assignment calculates values and discards
them, leaving params unchanged.

6. HISTORY
----------
history stores parameter snapshots and losses. It answers questions that final
loss cannot:

* Did loss decrease smoothly?
* Did parameters zigzag?
* Did training stall?
* How many steps were required?
* Did the optimizer diverge before returning a finite value?

Because this implementation creates new parameter lists, list(params) is still
used explicitly to document that each entry is an independent snapshot.

7. CONVERGENCE
--------------
Convergence does not usually mean parameters equal the mathematical minimum
exactly. Floating-point updates approach a region where improvements become
very small. We can stop after a fixed number of steps or use criteria such as:

    gradient norm < tolerance
    absolute loss change < tolerance
    maximum number of steps reached

This file uses a maximum step count and optional gradient-norm tolerance.

8. DIVERGENCE
-------------
Large updates can leave the narrow valley, create larger gradients, and then
create even larger updates. We guard against non-finite loss and a configurable
loss limit. A divergence guard is a diagnostic; it does not repair the run.

9. VANILLA GD LIMITATION ON ROSENBROCK
--------------------------------------
Vanilla GD uses only the current gradient. In a narrow valley, the largest
gradient component may point across a wall. Updates can alternate between
walls, while movement along the curved valley remains slow.

10. ROADMAP CONNECTION
----------------------
The roadmap class is one list comprehension. This file keeps that exact idea
and adds validation, history, stopping, and reporting around it. The core
algorithm remains:

    return [p - lr*g for p,g in zip(params,grads)]
"""

from math import isfinite, sqrt


def rosenbrock(params):
    x, y = params
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def rosenbrock_gradient(params):
    x, y = params
    valley_error = y - x ** 2
    return [
        -2 * (1 - x) - 400 * x * valley_error,
        200 * valley_error,
    ]


class GradientDescent:
    """Roadmap vanilla GD with input validation."""

    def __init__(self, lr=0.001):
        if lr <= 0:
            raise ValueError("learning rate must be positive")
        self.lr = lr

    def step(self, params, grads):
        if len(params) != len(grads):
            raise ValueError("params and grads must have equal lengths")
        return [p - self.lr * g for p, g in zip(params, grads)]


def vector_norm(values):
    return sqrt(sum(value ** 2 for value in values))


def optimize(
    optimizer,
    function,
    gradient_function,
    start,
    steps=10_000,
    gradient_tolerance=None,
    divergence_limit=1e100,
):
    """Generic, educational optimization loop returning rich history."""
    params = [float(value) for value in start]
    history = []
    status = "maximum_steps"

    for step in range(steps + 1):
        loss = function(params)
        grads = gradient_function(params)
        grad_norm = vector_norm(grads)

        history.append(
            {
                "step": step,
                "params": params[:],
                "loss": loss,
                "grads": grads[:],
                "gradient_norm": grad_norm,
                "lr": optimizer.lr,
            }
        )

        if not isfinite(loss) or loss > divergence_limit:
            status = "diverged"
            break
        if gradient_tolerance is not None and grad_norm < gradient_tolerance:
            status = "gradient_tolerance"
            break
        if step == steps:
            break

        params = optimizer.step(params, grads)

    return {
        "status": status,
        "params": params,
        "loss": function(params),
        "history": history,
    }


def first_step_dry_run():
    params = [-1.5, 1.5]
    optimizer = GradientDescent(lr=0.0005)
    loss = rosenbrock(params)
    grads = rosenbrock_gradient(params)
    new_params = optimizer.step(params, grads)

    print("First-step dry run")
    print("old params:", params)
    print("old loss:  ", loss)
    print("gradients: ", grads)
    print("new params:", new_params)

    assert loss == 62.5
    assert grads == [-455.0, -150.0]
    assert all(
        abs(actual - expected) < 1e-12
        for actual, expected in zip(new_params, [-1.2725, 1.575])
    )


def complete_roadmap_run():
    result = optimize(
        GradientDescent(lr=0.0005),
        rosenbrock,
        rosenbrock_gradient,
        start=[-1.5, 1.5],
        steps=10_000,
    )

    print("\nSelected checkpoints")
    for record in result["history"]:
        if record["step"] % 2000 == 0:
            x, y = record["params"]
            print(
                f"step={record['step']:5d} loss={record['loss']:.8f} "
                f"x={x:.6f} y={y:.6f} |g|={record['gradient_norm']:.6f}"
            )

    print("status:", result["status"])
    print("final params:", result["params"])
    print("final loss:", result["loss"])
    return result


if __name__ == "__main__":
    first_step_dry_run()
    run = complete_roadmap_run()
    assert run["loss"] < 0.01

