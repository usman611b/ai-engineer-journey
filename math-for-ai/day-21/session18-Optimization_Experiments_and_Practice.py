"""
DAY 21 — SESSION 18: OPTIMIZATION EXPERIMENTS AND PRACTICE LAB
==============================================================

PURPOSE
-------
This final Day 21 file turns the theory into controlled experiments. It is not
only a summary: it supplies four complete problems, predictions, implementations,
measurements, interpretation guidance, and answer checks.

EXPERIMENT 1: LEARNING-RATE SWEEP
-------------------------------------------------
Question: how does vanilla GD behave on Rosenbrock with rates:

    [0.0001, 0.0005, 0.001, 0.005, 0.01]

Keep start and step budget fixed. This isolates learning rate as the independent
variable. A very small rate should be stable but slow. A moderate rate should
make faster progress. A sufficiently large rate can overshoot and diverge.

Do not assume numerical order alone proves the outcome; run the experiment.
The largest stable rate depends on the start, loss geometry, and step budget.

EXPERIMENT 2: MOMENTUM SWEEP
----------------------------
Compare beta values:

    [0.0, 0.5, 0.9, 0.99]

beta=0 removes history under the roadmap convention. Increasing beta retains
more velocity. Moderate momentum may reduce oscillation; too much can carry
stale movement and overshoot. Learning rate and beta must be interpreted
together.

EXPERIMENT 3: SADDLE ESCAPE
---------------------------
Use:

    f(x,y)=x^2-y^2
    gradient=[2x,-2y]

Start slightly away from the exact saddle at [0.01,0.01]. Vanilla GD shrinks x
and expands |y|. Momentum can accumulate motion. Adam normalizes its two
coordinate histories. Loss becomes increasingly negative because the function
is unbounded below in the y direction; this experiment studies escape, not
convergence to a finite minimum.

At exact [0,0] with all states zero, all deterministic implementations remain
there. The slight nonzero start is essential.

EXPERIMENT 4: EXPONENTIAL DECAY
-------------------------------
Use:

    lr_t=lr_0*gamma^t

Compare fixed GD with scheduled GD from the same start. Decay can combine
larger early movement with smaller late refinement, but overly aggressive
gamma can freeze training early.

PRACTICE QUESTIONS WITH ANSWERS
-------------------------------
1. What does a gradient provide?
   It gives the direction of steepest local increase and a slope magnitude.
   Gradient descent uses the negative direction.

2. Why can a large learning rate diverge?
   It can jump across the minimum or valley, reach a steeper region, and create
   even larger later updates.

3. Why create momentum outside the training loop?
   Its velocity must persist. Recreating the object resets history.

4. Why does Adam keep m and v?
   m estimates recent signed direction; v estimates recent squared magnitude.
   Their ratio creates per-parameter adaptive scaling.

5. Does gradient=0 guarantee a minimum?
   No. It identifies a stationary point, which may be a minimum, maximum,
   saddle, or flat region.

6. Why is Rosenbrock difficult?
   The optimizer must follow a narrow, curved valley with steep cross-valley
   walls and a gentle direction toward (1,1).

7. Why reset params for every sweep run?
   Otherwise later configurations inherit earlier progress, making the
   comparison unfair.

8. Why inspect history rather than final loss only?
   History reveals speed, oscillation, stalls, and divergence along the path.

RUNNING THIS FILE
-----------------
The main block executes all four experiments using only Python's standard
library. Results are printed as tables. Change step counts or hyperparameters
and rerun to extend the investigation.
"""

from math import isfinite, sqrt


def rosenbrock(params):
    x, y = params
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def rosenbrock_gradient(params):
    x, y = params
    error = y - x ** 2
    return [-2 * (1 - x) - 400 * x * error, 200 * error]


def saddle(params):
    x, y = params
    return x ** 2 - y ** 2


def saddle_gradient(params):
    x, y = params
    return [2 * x, -2 * y]


class GradientDescent:
    def __init__(self, lr=0.001, schedule=None):
        self.initial_lr = lr
        self.lr = lr
        self.schedule = schedule
        self.t = 0

    def step(self, params, grads):
        if self.schedule is not None:
            self.lr = self.schedule(self.initial_lr, self.t)
        updated = [p - self.lr * g for p, g in zip(params, grads)]
        self.t += 1
        return updated


class Momentum:
    def __init__(self, lr=0.001, beta=0.9):
        self.lr = lr
        self.beta = beta
        self.velocity = None

    def step(self, params, grads):
        if self.velocity is None:
            self.velocity = [0.0] * len(params)
        self.velocity = [
            self.beta * velocity + gradient
            for velocity, gradient in zip(self.velocity, grads)
        ]
        return [p - self.lr * v for p, v in zip(params, self.velocity)]


class Adam:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def step(self, params, grads):
        if self.m is None:
            self.m = [0.0] * len(params)
            self.v = [0.0] * len(params)
        self.t += 1
        self.m = [
            self.beta1 * m + (1 - self.beta1) * g
            for m, g in zip(self.m, grads)
        ]
        self.v = [
            self.beta2 * v + (1 - self.beta2) * g ** 2
            for v, g in zip(self.v, grads)
        ]
        m_hat = [m / (1 - self.beta1 ** self.t) for m in self.m]
        v_hat = [v / (1 - self.beta2 ** self.t) for v in self.v]
        return [
            p - self.lr * mh / (sqrt(vh) + self.epsilon)
            for p, mh, vh in zip(params, m_hat, v_hat)
        ]


def safe_loss(function, params):
    try:
        value = function(params)
    except OverflowError:
        return float("inf")
    return value if isfinite(value) else float("inf")


def run(optimizer, function, gradient_function, start, steps, divergence=1e100):
    params = [float(value) for value in start]
    history = []

    for step in range(steps + 1):
        loss = safe_loss(function, params)
        history.append(
            {"step": step, "params": params[:], "loss": loss}
        )
        if loss > divergence:
            return {
                "status": "diverged",
                "params": params,
                "loss": loss,
                "history": history,
            }
        if step == steps:
            break
        try:
            grads = gradient_function(params)
            params = optimizer.step(params, grads)
        except OverflowError:
            return {
                "status": "diverged",
                "params": params,
                "loss": float("inf"),
                "history": history,
            }

    return {
        "status": "completed",
        "params": params,
        "loss": safe_loss(function, params),
        "history": history,
    }


def exponential_schedule(initial_lr, step, gamma=0.999):
    return initial_lr * gamma ** step


def learning_rate_sweep():
    print("\nEXPERIMENT 1 — LEARNING-RATE SWEEP")
    print("lr         status       final loss       final params")
    results = []
    for lr in [0.0001, 0.0005, 0.001, 0.005, 0.01]:
        result = run(
            GradientDescent(lr=lr),
            rosenbrock,
            rosenbrock_gradient,
            start=[-1.0, 1.0],
            steps=5000,
        )
        results.append((lr, result))
        print(
            f"{lr:<10g} {result['status']:11s} {result['loss']:15.8g} "
            f"{result['params']}"
        )
    return results


def momentum_sweep():
    print("\nEXPERIMENT 2 — MOMENTUM SWEEP")
    print("beta       status       final loss       final params")
    results = []
    for beta in [0.0, 0.5, 0.9, 0.99]:
        result = run(
            Momentum(lr=0.0001, beta=beta),
            rosenbrock,
            rosenbrock_gradient,
            start=[-1.0, 1.0],
            steps=5000,
        )
        results.append((beta, result))
        print(
            f"{beta:<10g} {result['status']:11s} {result['loss']:15.8g} "
            f"{result['params']}"
        )
    return results


def saddle_escape_comparison():
    print("\nEXPERIMENT 3 — SADDLE ESCAPE")
    configurations = [
        ("GD", GradientDescent(lr=0.1)),
        ("Momentum", Momentum(lr=0.05, beta=0.9)),
        ("Adam", Adam(lr=0.02)),
    ]
    results = []
    for name, optimizer in configurations:
        result = run(
            optimizer,
            saddle,
            saddle_gradient,
            start=[0.01, 0.01],
            steps=20,
            divergence=1e100,
        )
        results.append((name, result))
        x, y = result["params"]
        print(
            f"{name:9s} -> x={x:+.8f}, y={y:+.8f}, "
            f"loss={result['loss']:+.8f}"
        )
    return results


def decay_comparison():
    print("\nEXPERIMENT 4 — FIXED LR VERSUS EXPONENTIAL DECAY")
    fixed = run(
        GradientDescent(lr=0.0005),
        rosenbrock,
        rosenbrock_gradient,
        start=[-1.0, 1.0],
        steps=5000,
    )
    decayed = run(
        GradientDescent(
            lr=0.0005,
            schedule=lambda initial, step: exponential_schedule(
                initial,
                step,
                gamma=0.9999,
            ),
        ),
        rosenbrock,
        rosenbrock_gradient,
        start=[-1.0, 1.0],
        steps=5000,
    )
    print(f"fixed lr: final loss={fixed['loss']:.10f}, params={fixed['params']}")
    print(f"decayed:  final loss={decayed['loss']:.10f}, params={decayed['params']}")
    return fixed, decayed


if __name__ == "__main__":
    lr_results = learning_rate_sweep()
    momentum_results = momentum_sweep()
    saddle_results = saddle_escape_comparison()
    fixed_result, decay_result = decay_comparison()

    assert lr_results[0][1]["status"] == "completed"
    assert any(result["status"] == "diverged" for _, result in lr_results)
    assert all(result["loss"] < 0 for _, result in saddle_results)
    assert fixed_result["loss"] < rosenbrock([-1.0, 1.0])

