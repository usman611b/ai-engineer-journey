"""
DAY 21 — SESSION 07: ADAM FROM SCRATCH
======================================

This file combines every Adam idea into an executable optimizer and explains
the data flow from gradients to updated parameters.

COMPLETE ALGORITHM
------------------
For every step t and every parameter:

    m_t     = beta1*m_(t-1) + (1-beta1)*g_t
    v_t     = beta2*v_(t-1) + (1-beta2)*g_t^2
    m_hat_t = m_t/(1-beta1^t)
    v_hat_t = v_t/(1-beta2^t)
    w_t     = w_(t-1) - lr*m_hat_t/(sqrt(v_hat_t)+epsilon)

DATA STRUCTURE INTUITION
------------------------
params=[5,8] and grads=[2,-4] mean gradient 2 belongs to parameter 5 and
gradient -4 belongs to parameter 8. zip() preserves these pairs. Adam also
stores m and v at matching positions:

    parameter:  [5,   8]
    gradient:   [2,  -4]
    m history:  [m1, m2]
    v history:  [v1, v2]

FIRST-STEP DRY RUN FOR TWO PARAMETERS
-------------------------------------
Initial m=[0,0], v=[0,0], t=0. After t becomes 1:

For gradients [2,-4]:

    m = [0.1(2), 0.1(-4)] = [0.2,-0.4]
    v = [0.001(2^2), 0.001((-4)^2)] = [0.004,0.016]

Bias correction:

    m_hat = [0.2/0.1, -0.4/0.1] = [2,-4]
    v_hat = [0.004/0.001, 0.016/0.001] = [4,16]

Scaled directions:

    [2/sqrt(4), -4/sqrt(16)] = [1,-1]

At lr=0.001:

    first parameter  = 5 - 0.001(1)  = 4.999
    second parameter = 8 - 0.001(-1) = 8.001

The second parameter increases because subtracting a negative update adds.

STATEFUL BEHAVIOR
-----------------
The returned params are used in the next forward pass. The optimizer object
keeps m, v, and t internally. Creating a new Adam object every iteration would
erase history and prevent Adam from behaving correctly.

CONNECTION TO A NEURAL-NETWORK LOOP
-----------------------------------
Conceptually:

    predictions = model(inputs)
    loss = loss_function(predictions, targets)
    grads = backward(loss)
    params = optimizer.step(params, grads)

Backpropagation produces grads; Adam transforms them into parameter updates.
Real PyTorch optimizers mutate tensor parameters in place, but this educational
list implementation returns a new list to make every value easy to inspect.
"""


class Adam:
    """Educational list-based Adam implementation."""

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def step(self, params, grads):
        if len(params) != len(grads):
            raise ValueError("params and grads must have equal length")

        if self.m is None:
            self.m = [0.0] * len(params)
            self.v = [0.0] * len(params)
        elif len(params) != len(self.m):
            raise ValueError("parameter count changed after optimizer initialization")

        self.t += 1

        self.m = [
            self.beta1 * old_m + (1 - self.beta1) * gradient
            for old_m, gradient in zip(self.m, grads)
        ]
        self.v = [
            self.beta2 * old_v + (1 - self.beta2) * gradient ** 2
            for old_v, gradient in zip(self.v, grads)
        ]

        m_hat = [
            moment / (1 - self.beta1 ** self.t)
            for moment in self.m
        ]
        v_hat = [
            moment / (1 - self.beta2 ** self.t)
            for moment in self.v
        ]

        new_params = [
            parameter
            - self.lr * corrected_m / (corrected_v ** 0.5 + self.epsilon)
            for parameter, corrected_m, corrected_v
            in zip(params, m_hat, v_hat)
        ]
        return new_params

    def state(self):
        """Return copies for learning/debugging without exposing mutable lists."""
        return {
            "step": self.t,
            "m": None if self.m is None else self.m[:],
            "v": None if self.v is None else self.v[:],
        }


def two_parameter_dry_run():
    optimizer = Adam(lr=0.001)
    params = [5.0, 8.0]
    grads = [2.0, -4.0]
    new_params = optimizer.step(params, grads)

    print("old params:", params)
    print("gradients: ", grads)
    print("state:     ", optimizer.state())
    print("new params:", new_params)

    assert abs(new_params[0] - 4.999) < 1e-8
    assert abs(new_params[1] - 8.001) < 1e-8


if __name__ == "__main__":
    two_parameter_dry_run()
