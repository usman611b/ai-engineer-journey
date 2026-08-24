"""
DAY 21 — SESSION 17: COMPARING GD, MOMENTUM, AND ADAM
=====================================================

LEARNING GOALS
--------------
This integration lesson runs all three roadmap optimizers on the same
Rosenbrock problem. It explains fair comparison, optimizer state, convergence
metrics, why Adam adapts per parameter, and why fastest training loss does not
automatically imply best test generalization.

1. THREE UPDATE STRATEGIES
--------------------------
Vanilla gradient descent:

    p = p - lr*g

It uses only the current gradient and one global learning rate.

Momentum:

    velocity = beta*velocity + g
    p = p - lr*velocity

It stores a direction history that accelerates consistent movement and dampens
some oscillation.

Adam:

    m = beta1*m + (1-beta1)*g
    v = beta2*v + (1-beta2)*g^2
    m_hat = m/(1-beta1^t)
    v_hat = v/(1-beta2^t)
    p = p - lr*m_hat/(sqrt(v_hat)+epsilon)

It stores direction and squared-magnitude histories per parameter.

2. WHAT MAKES A COMPARISON FAIR?
--------------------------------
Use the same:

* loss and analytical gradient;
* starting parameters;
* maximum number of update steps;
* numerical precision;
* convergence thresholds;
* reporting rules.

Learning rates need not be numerically identical because each optimizer scales
gradients differently. Fairness means giving each a sensible documented
configuration, not forcing the same number into mathematically different rules.

The Day 21 roadmap configurations are:

    GD:       lr=0.0005
    Momentum: lr=0.0001, momentum=0.9
    Adam:     lr=0.01

3. METRICS TO COMPARE
---------------------
Final loss alone is incomplete. This file measures:

* final x, y, and loss;
* first step reaching selected loss thresholds;
* path length through parameter space;
* number of recorded updates;
* whether the run diverged.

Path length is the sum of Euclidean distances between consecutive parameter
vectors. A long path can indicate oscillation, detours, or simply large useful
movement. It must be interpreted with the loss history.

4. EXPECTED ROSENBROCK BEHAVIOR
-------------------------------
Vanilla GD normally progresses slowly along the narrow curved valley. Momentum
uses its velocity to smooth and accelerate persistent directions. Adam adapts
x and y using their separate gradient histories and often reduces this
benchmark loss quickly.

Exact rankings depend on learning rates, start, step budget, and implementation.
The phrase Adam converges fastest is an empirical result for the documented
configuration, not a theorem for every optimization problem.

5. WHY ADAM ADAPTS PER PARAMETER
--------------------------------
For parameter i, the denominator sqrt(v_hat_i) reflects that parameter's own
recent squared gradients. A parameter with historically large gradients gets a
larger denominator; one with smaller gradients gets a smaller denominator.

Adam does not use one shared v for the whole model. params, m, and v have
matching entries. That is the source of per-parameter adaptation.

6. OPTIMIZER STATE
------------------
GD has no history in this implementation. Momentum stores velocity. Adam stores
m, v, and step counter t. All stateful optimizer objects must be created once
and reused through the loop.

7. TRAINING SPEED VERSUS GENERALIZATION
---------------------------------------
Rosenbrock has no train/test split, so it measures optimization behavior only.
On a neural network, the optimizer that reaches the lowest training loss
fastest may not produce the best validation accuracy. Generalization depends on
data, architecture, regularization, batch noise, schedule, and the solution
region.

8. SIMPLE VERSUS ROADMAP IMPLEMENTATION
----------------------------------------
The simple view is one method call:

    grads = gradient_function(params)
    params = optimizer.step(params, grads)

The complete code below keeps the roadmap equations intact and adds shared
validation and comparison measurements.
"""

from math import isfinite, sqrt


def rosenbrock(params):
    x, y = params
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def rosenbrock_gradient(params):
    x, y = params
    error = y - x ** 2
    return [-2 * (1 - x) - 400 * x * error, 200 * error]


class GradientDescent:
    def __init__(self, lr=0.001):
        self.lr = lr

    def step(self, params, grads):
        return [p - self.lr * g for p, g in zip(params, grads)]


class SGDMomentum:
    def __init__(self, lr=0.001, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.velocity = None

    def step(self, params, grads):
        if self.velocity is None:
            self.velocity = [0.0] * len(params)
        self.velocity = [
            self.momentum * velocity + gradient
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


def optimize(optimizer, function, gradient_function, start, steps=5000):
    params = list(start)
    history = [
        {"step": 0, "params": params[:], "loss": function(params)}
    ]
    status = "completed"

    for step in range(1, steps + 1):
        grads = gradient_function(params)
        params = optimizer.step(params, grads)
        try:
            loss = function(params)
        except OverflowError:
            loss = float("inf")
        history.append({"step": step, "params": params[:], "loss": loss})
        if not isfinite(loss) or loss > 1e100:
            status = "diverged"
            break

    return {"status": status, "params": params, "history": history}


def first_step_below(history, threshold):
    for record in history:
        if record["loss"] < threshold:
            return record["step"]
    return None


def path_length(history):
    total = 0.0
    for previous, current in zip(history, history[1:]):
        total += sqrt(
            sum(
                (new - old) ** 2
                for old, new in zip(previous["params"], current["params"])
            )
        )
    return total


def summarize(name, result):
    history = result["history"]
    final = history[-1]
    x, y = final["params"]
    return {
        "name": name,
        "status": result["status"],
        "steps": final["step"],
        "x": x,
        "y": y,
        "loss": final["loss"],
        "below_1e-2": first_step_below(history, 1e-2),
        "below_1e-4": first_step_below(history, 1e-4),
        "path_length": path_length(history),
    }


def roadmap_comparison(steps=5000):
    start = [-1.0, 1.0]
    configurations = [
        ("GD", GradientDescent(lr=0.0005)),
        ("Momentum", SGDMomentum(lr=0.0001, momentum=0.9)),
        ("Adam", Adam(lr=0.01)),
    ]

    summaries = []
    for name, optimizer in configurations:
        result = optimize(
            optimizer,
            rosenbrock,
            rosenbrock_gradient,
            start,
            steps,
        )
        summaries.append(summarize(name, result))

    print("Roadmap comparison from start [-1,1]")
    print(
        "optimizer  status      steps      final loss     "
        "step<1e-2  step<1e-4  path length"
    )
    for item in summaries:
        print(
            f"{item['name']:9s} {item['status']:10s} {item['steps']:6d} "
            f"{item['loss']:15.8g} {str(item['below_1e-2']):>10s} "
            f"{str(item['below_1e-4']):>10s} {item['path_length']:12.6f}"
        )
        print(f"           final point = ({item['x']:.8f}, {item['y']:.8f})")
    return summaries


if __name__ == "__main__":
    results = roadmap_comparison()
    assert all(item["status"] == "completed" for item in results)
    # With the roadmap's exact start, lr, and 5,000-step budget, Adam reaches
    # roughly 1e-6. Test the documented run instead of demanding extra steps.
    assert results[-1]["loss"] < 1e-5
