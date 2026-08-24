"""
DAY 21 — SESSION 16: MOMENTUM ON THE ROSENBROCK VALLEY
======================================================

LEARNING GOALS
--------------
This session applies momentum to the Rosenbrock function. It explains velocity,
state persistence, accumulation and cancellation, the interaction of momentum
with learning rate, and a complete stateful optimization run.

1. WHY VANILLA GD ZIGZAGS
-------------------------
Rosenbrock has steep valley walls and a gentle curved direction toward (1,1).
The current gradient may be dominated by a wall-normal component. Vanilla GD
can cross the valley, see a gradient pointing back, cross again, and make only
slow forward progress.

Vanilla update:

    params_new = params - lr*current_gradient

There is no memory of which direction remained useful across earlier steps.

2. MOMENTUM EQUATIONS USED BY THE ROADMAP
-----------------------------------------

    velocity_t = beta*velocity_(t-1) + gradient_t
    params_t   = params_(t-1) - lr*velocity_t

beta is usually near 0.9. velocity has one entry per parameter:

    params   = [x, y]
    grads    = [df/dx, df/dy]
    velocity = [v_x, v_y]

3. BALL-ROLLING INTUITION
-------------------------
A real ball retains motion. When slopes repeatedly agree, it builds speed.
When slopes alternate, the old velocity resists an immediate full reversal.

Consistent gradients with beta=0.9:

    g1=2 -> v1=2
    g2=2 -> v2=0.9(2)+2=3.8
    g3=2 -> v3=0.9(3.8)+2=5.42

Alternating gradients:

    g1= 4 -> v1= 4
    g2=-4 -> v2=-0.4
    g3= 4 -> v3= 3.64
    g4=-4 -> v4=-0.724

The raw gradients reverse between plus and minus four. Velocity's reversed
magnitude is much smaller because history partially cancels the change.

4. WHAT beta MEANS
------------------
beta determines how much old velocity survives:

    beta=0   -> no history; this convention reduces to vanilla GD
    beta=0.5 -> shorter memory
    beta=0.9 -> common long memory
    beta=0.99 -> very long memory, potentially slow to change direction

High beta can smooth movement but can also overshoot because large stored
velocity continues after the gradient changes.

5. FIRST ROSENBROCK STEP
------------------------
At params=[-1.5,1.5], the gradient is [-455,-150]. If velocity begins [0,0],
beta=0.9, and lr=0.0001:

    velocity = [-455,-150]
    x_new = -1.5 - 0.0001(-455) = -1.4545
    y_new =  1.5 - 0.0001(-150) =  1.515

The first momentum step matches vanilla GD at the same learning rate because
there is no previous velocity yet.

6. THE DIFFERENCE BEGINS AT STEP TWO
------------------------------------
At the new point, the gradient is recalculated. Momentum combines that new
gradient with 90 percent of [-455,-150]. Thus the second movement depends on
both the new landscape slope and the previous step.

7. STATE MUST PERSIST
---------------------
velocity is optimizer state. Create the optimizer once, outside the loop:

    optimizer = Momentum(...)
    for step in range(...):
        params = optimizer.step(params, grads)

Creating a new optimizer inside the loop resets velocity to zero every time.
Then velocity_t=gradient_t and the benefit of momentum disappears.

8. LEARNING RATE AND MOMENTUM INTERACT
--------------------------------------
Repeated same-sign gradients can make velocity much larger than the current
gradient. Therefore a rate suitable for vanilla GD may overshoot with this raw
accumulation convention. The roadmap uses a conservative momentum rate:

    lr=0.0001, beta=0.9

Another common convention includes (1-beta)*gradient in the velocity average.
Its numerical scale differs. When reading code, inspect the exact equation
before comparing learning rates.

9. MOMENTUM DOES NOT ALWAYS HELP
--------------------------------
Momentum can overshoot a rapidly changing target, retain stale direction, or
perform poorly with unsuitable lr and beta. It helps when gradients contain a
consistent useful component and oscillating nuisance components.

10. MOMENTUM AT AN EXACT SADDLE
-------------------------------
If current gradient and stored velocity are both exactly zero, momentum cannot
move. If gradient is zero but stored velocity is nonzero, it can continue:

    v_new=beta*v_old

The movement comes from history, not from information in the zero gradient.
"""

from math import isfinite, sqrt


def rosenbrock(params):
    x, y = params
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def rosenbrock_gradient(params):
    x, y = params
    error = y - x ** 2
    return [-2 * (1 - x) - 400 * x * error, 200 * error]


class SGDMomentum:
    """The exact list-based momentum algorithm from the roadmap."""

    def __init__(self, lr=0.001, momentum=0.9):
        if lr <= 0:
            raise ValueError("learning rate must be positive")
        if not 0 <= momentum < 1:
            raise ValueError("momentum must be in [0,1)")
        self.lr = lr
        self.momentum = momentum
        self.velocity = None

    def step(self, params, grads):
        if len(params) != len(grads):
            raise ValueError("params and grads must have equal lengths")
        if self.velocity is None:
            self.velocity = [0.0] * len(params)
        elif len(self.velocity) != len(params):
            raise ValueError("parameter count changed")

        self.velocity = [
            self.momentum * velocity + gradient
            for velocity, gradient in zip(self.velocity, grads)
        ]
        return [
            parameter - self.lr * velocity
            for parameter, velocity in zip(params, self.velocity)
        ]

    def state(self):
        return None if self.velocity is None else self.velocity[:]


def vector_norm(values):
    return sqrt(sum(value ** 2 for value in values))


def optimize_momentum(start=(-1.5, 1.5), lr=0.0001, beta=0.9, steps=20_000):
    optimizer = SGDMomentum(lr=lr, momentum=beta)
    params = [float(value) for value in start]
    history = []

    for step in range(steps + 1):
        loss = rosenbrock(params)
        grads = rosenbrock_gradient(params)
        velocity = optimizer.state()
        history.append(
            {
                "step": step,
                "params": params[:],
                "loss": loss,
                "grads": grads[:],
                "gradient_norm": vector_norm(grads),
                "velocity": velocity,
            }
        )

        if not isfinite(loss) or loss > 1e100:
            return {"status": "diverged", "history": history, "params": params}
        if step < steps:
            params = optimizer.step(params, grads)

    return {"status": "maximum_steps", "history": history, "params": params}


def first_step_dry_run():
    params = [-1.5, 1.5]
    grads = rosenbrock_gradient(params)
    optimizer = SGDMomentum(lr=0.0001, momentum=0.9)
    updated = optimizer.step(params, grads)

    print("Momentum first-step dry run")
    print("params:      ", params)
    print("grads:       ", grads)
    print("new velocity:", optimizer.state())
    print("new params:  ", updated)

    assert grads == [-455.0, -150.0]
    assert optimizer.state() == grads
    assert all(
        abs(actual - expected) < 1e-12
        for actual, expected in zip(updated, [-1.4545, 1.515])
    )


def complete_run():
    result = optimize_momentum()
    print("\nSelected momentum checkpoints")
    for record in result["history"]:
        if record["step"] % 4000 == 0:
            x, y = record["params"]
            velocity_norm = (
                0.0 if record["velocity"] is None else vector_norm(record["velocity"])
            )
            print(
                f"step={record['step']:5d} loss={record['loss']:.10f} "
                f"x={x:.6f} y={y:.6f} |v|={velocity_norm:.6f}"
            )

    final_loss = rosenbrock(result["params"])
    print("status:", result["status"])
    print("final params:", result["params"])
    print("final loss:", final_loss)
    return result, final_loss


if __name__ == "__main__":
    first_step_dry_run()
    run, loss = complete_run()
    assert run["status"] != "diverged"
    assert loss < 1e-6

