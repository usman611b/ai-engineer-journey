"""
DAY 21 — SESSION 04: SGD WITH MOMENTUM
======================================

1. THE WEAKNESS OF VANILLA GD
-----------------------------
Vanilla gradient descent uses only the current gradient and forgets every past
step. In a narrow curved valley, steep side-to-side gradients can change sign
repeatedly while the useful forward component stays consistent. GD zigzags
between walls and makes slow forward progress.

2. ROLLING-BALL INTUITION
-------------------------
A ball rolling downhill has velocity. Repeated force in one direction builds
speed; opposing forces cancel; one small bump does not erase all motion.
Momentum gives an optimizer similar memory.

This lesson uses the convention:

    v_t = beta * v_(t-1) + g_t
    w_t = w_(t-1) - lr * v_t

Some books put (1-beta) before g or store a negative velocity. These are related
conventions, but formulas and learning-rate scales must not be mixed blindly.

3. MEANING OF EACH TERM
-----------------------
g_t is the current gradient. v_t is accumulated gradient history. beta controls
how much previous velocity remains. lr scales the final update. Typical beta is
0.9.

    beta=0    -> v_t=g_t, so this reduces to vanilla GD
    beta=0.5  -> short memory
    beta=0.9  -> strong practical memory
    beta=0.99 -> very long memory; smooth but may react slowly or overshoot

4. CONSISTENT GRADIENTS BUILD SPEED
-----------------------------------
Let w=10, lr=0.1, beta=0.9, v0=0, and every gradient equal 2.

Step 1:
    v1=0.9(0)+2=2
    w1=10-0.1(2)=9.8

Step 2:
    v2=0.9(2)+2=3.8
    w2=9.8-0.1(3.8)=9.42

Step 3:
    v3=0.9(3.8)+2=5.42
    w3=9.42-0.1(5.42)=8.878

Vanilla GD would move 0.2 every time. Momentum moves 0.2, then 0.38, then
0.542 because history agrees with the current direction.

5. OPPOSING GRADIENTS DAMPEN ZIGZAGS
------------------------------------
Let beta=0.9, v0=0, g1=+2, g2=-2:

    v1=2
    v2=0.9(2)-2=-0.2

Without memory, direction changes fully from +2 to -2. Momentum's retained +1.8
mostly cancels the new -2, leaving -0.2. In dimensions whose gradients alternate,
oscillation shrinks. In dimensions whose gradients agree, speed grows.

6. OUR PRACTICE EXAMPLE
-----------------------
w0=5, v0=0, beta=0.5, lr=0.1, g1=4, g2=2:

    v1=0.5(0)+4=4;       w1=5-0.1(4)=4.6
    v2=0.5(4)+2=4;       w2=4.6-0.1(4)=4.2

Although the current gradient fell from 4 to 2, retained history kept velocity
at 4. Without momentum, the second result would be 4.4 instead of 4.2.

7. STATEFUL OPTIMIZATION
------------------------
Momentum must store one velocity per parameter. A model with one million
parameters needs one million velocity values. The state must survive between
step() calls; resetting it each step destroys momentum.

8. SGD VERSUS MOMENTUM
----------------------
SGD/mini-batch describes how data estimates the gradient. Momentum describes
how current and past gradients are combined. "SGD with momentum" normally uses
mini-batch gradients plus velocity memory.
"""


class SGDMomentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.velocity = None

    def step(self, params, grads):
        if len(params) != len(grads):
            raise ValueError("params and grads must have equal length")
        if self.velocity is None:
            self.velocity = [0.0] * len(params)

        self.velocity = [
            self.momentum * old_velocity + gradient
            for old_velocity, gradient in zip(self.velocity, grads)
        ]
        return [
            parameter - self.lr * velocity
            for parameter, velocity in zip(params, self.velocity)
        ]


if __name__ == "__main__":
    optimizer = SGDMomentum(lr=0.1, momentum=0.5)
    params = [5.0]
    for step, grads in enumerate(([4.0], [2.0]), start=1):
        params = optimizer.step(params, grads)
        print(f"step={step}, velocity={optimizer.velocity}, params={params}")

