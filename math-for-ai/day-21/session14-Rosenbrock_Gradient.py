"""
DAY 21 — SESSION 14: DERIVING AND CHECKING THE ROSENBROCK GRADIENT
=================================================================

LEARNING GOALS
--------------
This file derives both partial derivatives step by step, explains every chain-
rule factor, evaluates important points, performs a finite-difference gradient
check, and demonstrates one two-parameter gradient-descent update.

1. STARTING LOSS
----------------

    f(x,y) = (1-x)^2 + 100*(y-x^2)^2

The gradient contains one partial derivative for every parameter:

    gradient f(x,y) = [df/dx, df/dy]

When differentiating with respect to x, y is treated as constant. When
differentiating with respect to y, x is treated as constant.

2. DERIVATIVE OF THE FIRST TERM WITH RESPECT TO x
--------------------------------------------------
Let:

    A=(1-x)^2
    u=1-x

The outer derivative is:

    d(u^2)/du = 2u

The inner derivative is:

    du/dx = -1

By the chain rule:

    dA/dx = 2(1-x)*(-1)
           = -2(1-x)
           = 2(x-1)

All three final forms are equivalent.

3. DERIVATIVE OF THE SECOND TERM WITH RESPECT TO x
---------------------------------------------------
Let:

    B=100*(y-x^2)^2
    u=y-x^2

Outer derivative:

    d(100u^2)/du = 200u

Inner derivative with respect to x:

    du/dx = d(y-x^2)/dx = 0-2x = -2x

Multiply the chain-rule factors:

    dB/dx = 200*(y-x^2)*(-2x)
           = -400x*(y-x^2)

4. COMPLETE x DERIVATIVE
------------------------
Add both term contributions:

    df/dx = -2(1-x) - 400x*(y-x^2)

Equivalent roadmap form:

    df/dx = -2(1-x) + 200*(y-x^2)*(-2x)

5. y DERIVATIVE
---------------
The first term contains no y, so its y derivative is zero. For the second term:

    outer derivative = 200*(y-x^2)
    inner derivative = d(y-x^2)/dy = 1

Therefore:

    df/dy = 200*(y-x^2)

6. COMPLETE GRADIENT
--------------------

    gradient f(x,y) = [
        -2(1-x) - 400x*(y-x^2),
        200*(y-x^2)
    ]

The intermediate value y-x^2 is part of both formulas. It is not by itself the
complete x gradient or y gradient.

7. IMPORTANT POINTS
-------------------
At (1,1): y-x^2=0

    df/dx=0, df/dy=0

At (-1,1): y-x^2=0

    df/dx=-2(1-(-1))=-4
    df/dy=0

At (2,4): y-x^2=0

    df/dx=-2(1-2)=2
    df/dy=0

The point is on the valley, so the second-term contribution vanishes, but the
first term still moves x toward 1.

At (1,0): y-x^2=-1

    df/dx=0-400(1)(-1)=400
    df/dy=200(-1)=-200

The large gradient reflects the steep valley penalty.

8. ONE UPDATE AT (2,4)
----------------------
With lr=0.001 and gradient [2,0]:

    x_new = 2 - 0.001(2) = 1.998
    y_new = 4 - 0.001(0) = 4

9. WHY SMALL LEARNING RATES ARE COMMON HERE
--------------------------------------------
The formulas contain factors 200 and 400. Away from the valley, gradients can
become large. Since update=lr*gradient, a learning rate that sounds small may
still create a large jump.

10. FINITE-DIFFERENCE GRADIENT CHECK
------------------------------------
An analytical derivative can be checked numerically:

    df/dx approximately [f(x+h,y)-f(x-h,y)]/(2h)

and similarly for y. A small h, such as 1e-6, usually gives a close check.
This detects algebra or code mistakes; it does not replace understanding the
chain rule.

Extremely tiny h can suffer floating-point cancellation, while a large h gives
a poor local approximation. Gradient checks therefore use a small but not
infinitesimal value.
"""


def rosenbrock(params):
    x, y = params
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def rosenbrock_gradient(params):
    """The simplified analytical gradient."""
    x, y = params
    valley_error = y - x ** 2
    df_dx = -2 * (1 - x) - 400 * x * valley_error
    df_dy = 200 * valley_error
    return [df_dx, df_dy]


def rosenbrock_gradient_roadmap(params):
    """Same derivative written exactly in the roadmap's chain-rule form."""
    x, y = params
    df_dx = -2 * (1 - x) + 200 * (y - x ** 2) * (-2 * x)
    df_dy = 200 * (y - x ** 2)
    return [df_dx, df_dy]


def central_difference_gradient(params, step_size=1e-6):
    if step_size <= 0:
        raise ValueError("step_size must be positive")
    numerical = []
    for index in range(len(params)):
        plus = list(params)
        minus = list(params)
        plus[index] += step_size
        minus[index] -= step_size
        derivative = (rosenbrock(plus) - rosenbrock(minus)) / (2 * step_size)
        numerical.append(derivative)
    return numerical


def gradient_descent_step(params, grads, lr):
    if len(params) != len(grads):
        raise ValueError("params and grads must have equal lengths")
    return [parameter - lr * gradient for parameter, gradient in zip(params, grads)]


def explain_point(params, lr=0.001):
    x, y = params
    valley_error = y - x ** 2
    analytical = rosenbrock_gradient(params)
    numerical = central_difference_gradient(params)
    updated = gradient_descent_step(params, analytical, lr)
    print(f"point={params}, loss={rosenbrock(params):.8f}")
    print(f"  y-x^2:             {valley_error:+.8f}")
    print(f"  analytical grad:   {analytical}")
    print(f"  numerical grad:    {[round(value, 8) for value in numerical]}")
    print(f"  one update lr={lr}: {updated}")


def verify_gradient(params, tolerance=1e-4):
    analytical = rosenbrock_gradient(params)
    numerical = central_difference_gradient(params)
    errors = [abs(a - n) for a, n in zip(analytical, numerical)]
    return max(errors) <= tolerance, errors


if __name__ == "__main__":
    expected = {
        (1.0, 1.0): [0.0, 0.0],
        (-1.0, 1.0): [-4.0, 0.0],
        (2.0, 4.0): [2.0, 0.0],
        (1.0, 0.0): [400.0, -200.0],
    }
    for point, wanted in expected.items():
        assert rosenbrock_gradient(point) == wanted
        assert rosenbrock_gradient_roadmap(point) == wanted
        okay, errors = verify_gradient(point)
        assert okay, (point, errors)
        explain_point(list(point))

