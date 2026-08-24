"""
DAY 21 — SESSION 08: LEARNING-RATE SCHEDULES
=============================================

LEARNING GOALS
--------------
By the end of this file you should be able to explain:

1. why one fixed learning rate is often a compromise;
2. what a learning-rate schedule changes and what it does not change;
3. the difference between step decay, exponential decay, cosine annealing,
   warmup, and warmup followed by decay;
4. whether a schedule should be updated per optimizer step or per epoch;
5. how to implement the roadmap formulas without PyTorch;
6. common schedule mistakes and how to diagnose them.

1. WHY CHANGE THE LEARNING RATE?
--------------------------------
Gradient descent updates one parameter w using:

    w_new = w_old - learning_rate * gradient

The gradient supplies direction and local slope. The learning rate controls
how much of that gradient becomes an actual movement.

Early in training, parameters may be far from a useful minimum. Larger steps
can cover distance quickly. Late in training, the optimizer may be inside a
narrow low-loss region. Smaller steps help it settle instead of repeatedly
jumping across the bottom.

A fixed learning rate must do both jobs:

    early job: move quickly;
    late job:  move carefully.

A schedule removes some of this compromise by changing the learning rate as
training progresses.

IMPORTANT: a schedule does not calculate gradients, change the loss function,
or replace an optimizer. It supplies the learning rate that the optimizer uses
at the current training step.

2. THE GENERAL PICTURE
----------------------
Let lr_0 be the initial learning rate and t be progress through training:

    lr_t = schedule(lr_0, t)

Then gradient descent uses:

    w_(t+1) = w_t - lr_t * g_t

Because lr_t changes, two identical gradients can produce different update
sizes at different times.

Example with gradient g=20:

    early lr=0.01:   update size = 0.01 * 20   = 0.2
    late lr=0.0001:  update size = 0.0001 * 20 = 0.002

The gradient direction is identical, but the late update is 100 times smaller.

3. STEP DECAY
-------------
Step decay keeps the learning rate constant for a block of training, then
multiplies it by a factor.

    lr_t = lr_0 * factor^(floor(t / step_size))

Example:

    lr_0=0.1, factor=0.5, step_size=3

    t=0,1,2  -> 0.1
    t=3,4,5  -> 0.05
    t=6,7,8  -> 0.025

Advantages: simple, predictable, easy to control.
Disadvantage: the learning rate changes suddenly rather than smoothly.

4. EXPONENTIAL DECAY
--------------------
Exponential decay multiplies the learning rate by the same decay factor each
step:

    lr_t = lr_0 * gamma^t

For lr_0=0.1 and gamma=0.9:

    t=0 -> 0.1000
    t=1 -> 0.0900
    t=2 -> 0.0810
    t=3 -> 0.0729

If gamma is close to one, decay is slow. If gamma is much smaller than one,
the learning rate may become uselessly tiny too early.

5. COSINE ANNEALING
-------------------
The roadmap formula is:

    lr_t = lr_min + 0.5*(lr_max-lr_min)*(1 + cos(pi*t/T))

where 0 <= t <= T.

At t=0, cos(0)=1, so lr_t=lr_max.
At t=T, cos(pi)=-1, so lr_t=lr_min.

The schedule falls smoothly: it changes slowly near the beginning and end and
more rapidly in the middle. It is common in modern deep-learning training.

This file implements one non-restarting cosine curve. Some libraries also
offer cosine restarts, which periodically raise the learning rate again. That
is a separate policy and should not be confused with basic cosine annealing.

6. WARMUP
---------
Warmup begins with a small learning rate and increases it gradually:

    lr_t = target_lr * (t+1)/warmup_steps

Why begin cautiously? At initialization, model activations, gradients, and
optimizer statistics may not yet be stable. A full learning rate can create a
destructive first update, especially in large models or large-batch training.

Warmup is normally a first phase, not the whole schedule:

    phase 1: warm up from small lr to peak lr;
    phase 2: decay from peak lr to a small final lr.

7. STEP VERSUS EPOCH
--------------------
An epoch means one pass through the dataset. An optimizer step means one
parameter update. With 100 mini-batches per epoch, there are 100 optimizer
steps in one epoch.

A per-step schedule changes after every mini-batch. A per-epoch schedule
changes only after a full pass. Both can be valid, but t and total_steps must
use the same unit. Mixing epochs with mini-batch counts makes the schedule run
100 times too quickly or too slowly.

8. COMMON FAILURE MODES
-----------------------
* Decaying before training has made useful progress.
* Using gamma=0.9 per mini-batch when it was intended per epoch.
* Letting cosine t exceed T without defining the desired behavior.
* Applying warmup and decay with inconsistent step numbering.
* Recreating a stateful scheduler every iteration.
* Assuming a schedule can rescue an extremely poor base learning rate.
* Reporting only final loss without comparing training speed and stability.

9. PRACTICAL RULE
-----------------
A schedule is successful when it gives useful early progress and stable late
refinement. There is no universally best curve. The base learning rate,
optimizer, batch size, model, and training length all interact.
"""

from math import cos, pi


def fixed_learning_rate(initial_lr, step):
    """Return a constant rate. step is accepted for a common interface."""
    if initial_lr < 0 or step < 0:
        raise ValueError("learning rate and step must be non-negative")
    return initial_lr


def step_decay(initial_lr, step, step_size=10, factor=0.5):
    """Roadmap-style discrete decay every step_size updates."""
    if initial_lr < 0 or step < 0:
        raise ValueError("learning rate and step must be non-negative")
    if step_size <= 0:
        raise ValueError("step_size must be positive")
    if not 0 < factor <= 1:
        raise ValueError("factor must be in (0, 1]")
    completed_blocks = step // step_size
    return initial_lr * factor ** completed_blocks


def exponential_decay(initial_lr, step, gamma=0.999):
    """Smooth multiplicative decay: lr_t = lr_0 * gamma**t."""
    if initial_lr < 0 or step < 0:
        raise ValueError("learning rate and step must be non-negative")
    if not 0 < gamma <= 1:
        raise ValueError("gamma must be in (0, 1]")
    return initial_lr * gamma ** step


def cosine_annealing(max_lr, min_lr, step, total_steps):
    """One cosine decay, clamped after total_steps at min_lr."""
    if total_steps <= 0:
        raise ValueError("total_steps must be positive")
    if not 0 <= min_lr <= max_lr:
        raise ValueError("require 0 <= min_lr <= max_lr")
    if step < 0:
        raise ValueError("step must be non-negative")
    progress = min(step, total_steps) / total_steps
    return min_lr + 0.5 * (max_lr - min_lr) * (1 + cos(pi * progress))


def linear_warmup(target_lr, step, warmup_steps):
    """Rise linearly and then remain at target_lr."""
    if target_lr < 0 or step < 0:
        raise ValueError("learning rate and step must be non-negative")
    if warmup_steps <= 0:
        raise ValueError("warmup_steps must be positive")
    fraction = min((step + 1) / warmup_steps, 1.0)
    return target_lr * fraction


def warmup_then_cosine(
    max_lr,
    min_lr,
    step,
    total_steps,
    warmup_steps,
):
    """A simple modern policy: linear warmup followed by cosine decay."""
    if not 0 < warmup_steps < total_steps:
        raise ValueError("warmup_steps must be between 0 and total_steps")
    if step < warmup_steps:
        return linear_warmup(max_lr, step, warmup_steps)

    decay_step = step - warmup_steps
    decay_steps = total_steps - warmup_steps
    return cosine_annealing(max_lr, min_lr, decay_step, decay_steps)


def apply_gradient_descent(parameter, gradient, learning_rate):
    """A deliberately simple scalar update showing where a schedule is used."""
    return parameter - learning_rate * gradient


def print_schedule(name, schedule_function, steps):
    print(f"\n{name}")
    for step in steps:
        print(f"step={step:2d}  lr={schedule_function(step):.6f}")


def roadmap_demo():
    """Print the schedules named in the Day 21 roadmap."""
    steps = [0, 1, 2, 3, 5, 8, 10]

    print_schedule(
        "Step decay",
        lambda t: step_decay(0.1, t, step_size=3, factor=0.5),
        steps,
    )
    print_schedule(
        "Exponential decay",
        lambda t: exponential_decay(0.1, t, gamma=0.9),
        steps,
    )
    print_schedule(
        "Cosine annealing",
        lambda t: cosine_annealing(0.1, 0.001, t, total_steps=10),
        steps,
    )
    print_schedule(
        "Warmup then cosine",
        lambda t: warmup_then_cosine(0.1, 0.001, t, 10, 3),
        steps,
    )


def simple_training_example():
    """Minimize f(w)=w^2, whose gradient is 2w, with exponential decay."""
    parameter = 5.0
    initial_lr = 0.1

    print("\nMinimizing f(w)=w^2 with exponential decay")
    for step in range(8):
        gradient = 2 * parameter
        lr = exponential_decay(initial_lr, step, gamma=0.9)
        parameter = apply_gradient_descent(parameter, gradient, lr)
        loss = parameter ** 2
        print(
            f"step={step:2d} lr={lr:.5f} "
            f"gradient={gradient:8.4f} w={parameter:8.4f} loss={loss:9.5f}"
        )


if __name__ == "__main__":
    assert abs(exponential_decay(0.1, 3, 0.9) - 0.0729) < 1e-12
    assert step_decay(0.1, 2, 3, 0.5) == 0.1
    assert step_decay(0.1, 3, 3, 0.5) == 0.05
    assert abs(cosine_annealing(0.1, 0.001, 0, 10) - 0.1) < 1e-12
    assert abs(cosine_annealing(0.1, 0.001, 10, 10) - 0.001) < 1e-12

    roadmap_demo()
    simple_training_example()

