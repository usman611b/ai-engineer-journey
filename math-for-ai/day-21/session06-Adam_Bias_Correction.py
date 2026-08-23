"""
DAY 21 — SESSION 06: ADAM BIAS CORRECTION
=========================================

1. THE COLD-START PROBLEM
-------------------------
Adam initializes m0=0 and v0=0 because no gradient history exists. Early moving
averages are therefore artificially pulled toward zero. This is initialization
bias, not statistical unfairness.

With g1=4, beta1=0.9 and beta2=0.999:

    m1 = 0.9(0) + 0.1(4) = 0.4
    v1 = 0.999(0) + 0.001(4^2) = 0.016

The only observed gradient is 4 and squared gradient is 16, yet stored values
are 0.4 and 0.016 because zero initialization dominates the first step.

2. CORRECTION FORMULAS
----------------------

    m_hat_t = m_t / (1-beta1^t)
    v_hat_t = v_t / (1-beta2^t)

t is the optimizer update count, starting at 1.

At t=1:

    m_hat1 = 0.4/(1-0.9) = 0.4/0.1 = 4
    v_hat1 = 0.016/(1-0.999) = 0.016/0.001 = 16

Correction recovers the appropriate first-step estimates.

3. COMPLETE FIRST UPDATE
------------------------
Let w0=10, lr=0.001, and ignore tiny epsilon for readable arithmetic:

    scaled direction = 4/sqrt(16) = 1
    w1 = 10 - 0.001(1) = 9.999

Our other practice values m1=0.2 and v1=0.004 correspond to gradient 2:

    m_hat1=0.2/0.1=2
    v_hat1=0.004/0.001=4
    scaled direction=2/sqrt(4)=1

4. WHY CORRECTION FADES OVER TIME
---------------------------------
For beta1=0.9:

    t=1:   1-0.9^1   = 0.1
    t=10:  1-0.9^10  is about 0.6513
    t=100: 1-0.9^100 is about 0.99997

As t grows, beta^t approaches zero, so 1-beta^t approaches one. Division by a
number near one changes little. Correction is strongest when history is short.

Because beta2=0.999 is closer to one, its uncorrected v warms up more slowly;
v bias correction is especially important early.

5. WHY t MUST INCREASE ONCE PER OPTIMIZER STEP
-----------------------------------------------
t counts parameter-update rounds, not parameters. If a model has one million
weights, processing all of them in one optimizer.step() changes t once. All
weights share t but retain separate m and v arrays.

6. COMMON ERRORS
----------------
* Using uncorrected m and v in early updates.
* Starting t at zero inside correction, causing division by 1-beta^0=0.
* Resetting t, m, or v every training iteration.
* Forgetting to square gradients for v.
* Confusing v with momentum-class velocity.
"""


def update_moments(old_m, old_v, gradient, beta1=0.9, beta2=0.999):
    new_m = beta1 * old_m + (1 - beta1) * gradient
    new_v = beta2 * old_v + (1 - beta2) * gradient ** 2
    return new_m, new_v


def correct_bias(moment, beta, step):
    if step < 1:
        raise ValueError("step must begin at 1")
    return moment / (1 - beta ** step)


if __name__ == "__main__":
    gradient = 4.0
    m, v = update_moments(0.0, 0.0, gradient)
    m_hat = correct_bias(m, 0.9, 1)
    v_hat = correct_bias(v, 0.999, 1)
    print(f"raw m={m}, raw v={v}")
    print(f"corrected m={m_hat}, corrected v={v_hat}")
    print(f"scaled direction={m_hat / v_hat ** 0.5}")

