"""
DAY 21 — SESSION 05: ADAM INTUITION AND MOMENTS
===============================================

1. WHY ADAM EXISTS
------------------
One global learning rate may not suit every weight. Some parameters receive
large gradients frequently; others receive tiny or sparse gradients. Vanilla
GD scales both by exactly the same lr. Momentum remembers direction but still
does not explicitly normalize each parameter by its own magnitude history.

Adam means Adaptive Moment Estimation. It combines:

* direction memory similar to momentum;
* magnitude memory from squared gradients;
* a separately scaled update for every parameter.

2. FIRST MOMENT m: RECENT DIRECTION
-----------------------------------

    m_t = beta1*m_(t-1) + (1-beta1)*g_t

m is an exponential moving average of gradients. It asks: "In which direction
have recent gradients generally pointed?" Typical beta1=0.9. Unlike the earlier
momentum convention, Adam includes (1-beta1), making m a moving average scale.

3. SECOND MOMENT v: RECENT SQUARED MAGNITUDE
--------------------------------------------

    v_t = beta2*v_(t-1) + (1-beta2)*g_t^2

v asks: "How large have this parameter's recent gradients been?" Typical
beta2=0.999, so this magnitude estimate changes slowly and smoothly.

Why square? Gradients +10 and -10 average to zero despite both being large.
Squares are 100 and 100: sign disappears and magnitude remains. In Adam, v is
not the velocity variable from our momentum class; it is squared-gradient
history.

4. THE ADAPTIVE SCALING IDEA
----------------------------
After bias correction (next session), Adam uses:

    scaled_direction = m_hat / (sqrt(v_hat) + epsilon)
    w_new = w - lr * scaled_direction

Large historical magnitude makes sqrt(v_hat) large and restrains an update.
Small historical magnitude makes the denominator small so a parameter is not
forced to crawl merely because its raw gradient scale is small.

Example A:
    m=100, v=10000 -> 100/sqrt(10000)=100/100=1

Example B:
    m=0.01, v=0.0001 -> 0.01/sqrt(0.0001)=0.01/0.01=1

Raw scales differ by 10,000 times, yet their normalized directions match.
This does NOT imply all Adam updates always match. Across many steps, every
weight has its own direction consistency and magnitude history.

5. A SECOND COMPARISON
----------------------
Weight A: m=20, v=400
    scaled direction = 20/sqrt(400)=1

Weight B: m=2, v=16
    scaled direction = 2/sqrt(16)=0.5

At lr=0.001, update magnitudes are 0.001 and 0.0005. A receives the larger
update. Adam does not mechanically enlarge every small raw gradient; it uses
the ratio of direction history to magnitude history.

6. EPSILON
----------
If v_hat is zero, division by sqrt(v_hat) would divide by zero. Adam adds a tiny
epsilon, normally 1e-8:

    sqrt(v_hat) + epsilon

Its main purpose is numerical stability. It is not a meaningful learning rate
and does not represent gradient history.

7. STANDARD DEFAULTS
--------------------
    lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8

These are useful starting points, not universal guarantees.

8. OPTIMIZER COMPARISON
-----------------------
Vanilla GD: no direction memory, no magnitude memory, one raw scaling.
Momentum: direction history, but no squared-magnitude adaptation.
Adam: direction history m, squared-magnitude history v, per-weight adaptation.
"""


def scaled_direction(first_moment, second_moment, epsilon=1e-8):
    if second_moment < 0:
        raise ValueError("second moment cannot be negative")
    return first_moment / (second_moment ** 0.5 + epsilon)


if __name__ == "__main__":
    examples = [(100, 10_000), (0.01, 0.0001), (20, 400), (2, 16)]
    for first, second in examples:
        value = scaled_direction(first, second, epsilon=0.0)
        print(f"m={first:g}, v={second:g}, m/sqrt(v)={value:g}")

