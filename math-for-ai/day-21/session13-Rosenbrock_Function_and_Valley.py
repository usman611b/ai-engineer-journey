"""
DAY 21 — SESSION 13: THE ROSENBROCK FUNCTION AND CURVED VALLEY
==============================================================

LEARNING GOALS
--------------
This file introduces the Day 21 optimization benchmark, proves its global
minimum, explains both terms, shows why the coefficient 100 matters, and builds
a simple executable implementation before any optimizer is applied.

1. THE FUNCTION
---------------
The two-dimensional Rosenbrock function is:

    f(x,y) = (1-x)^2 + 100*(y-x^2)^2

Its global minimum is:

    (x,y)=(1,1), f(1,1)=0

x and y act like two trainable model parameters. f acts like training loss.
An optimizer must change x and y until the loss becomes small.

2. WHY USE A TEST FUNCTION?
---------------------------
Before comparing optimizers on millions of neural-network weights, a controlled
test function provides:

* a known correct answer;
* an exact gradient;
* a landscape difficult enough to reveal different optimizer behavior;
* parameters and updates that can be inspected by hand;
* reproducible comparisons from the same starting point.

Rosenbrock is not a neural network. It is an optimization laboratory.

3. FIRST TERM: SELECT x=1
-------------------------
The first term is:

    (1-x)^2

It is non-negative and becomes zero only when x=1.

    x=-1 -> (1-(-1))^2 = 4
    x= 0 -> (1-0)^2    = 1
    x= 1 -> (1-1)^2    = 0
    x= 2 -> (1-2)^2    = 1

This term pulls x toward 1.

4. SECOND TERM: SELECT THE CURVED VALLEY
----------------------------------------
The second term is:

    100*(y-x^2)^2

It becomes zero whenever:

    y=x^2

This is a parabola, so points such as the following lie exactly on the valley:

    (-2,4), (-1,1), (0,0), (1,1), (2,4)

At all these points, the second term is zero. But not every point on the valley
is the global minimum because the first term still requires x=1.

5. WHY MULTIPLY BY 100?
-----------------------
The coefficient makes departures from y=x^2 expensive:

    y-x^2 = 0.01 -> second term = 100*(0.01)^2 = 0.01
    y-x^2 = 0.10 -> second term = 100*(0.10)^2 = 1
    y-x^2 = 1.00 -> second term = 100*(1.00)^2 = 100

This creates steep valley walls. The optimizer must coordinate x and y so that
y follows the changing value x^2.

6. PROOF OF THE GLOBAL MINIMUM
------------------------------
Both terms are squared quantities:

    (1-x)^2 >= 0
    100*(y-x^2)^2 >= 0

Therefore f(x,y)>=0 everywhere. The smallest possible value is zero, requiring
both terms to vanish.

From the first term:

    x=1

From the second term:

    y=x^2

Substitute x=1:

    y=1^2=1

At (1,1), the loss is zero. Since no loss can be negative, this is the global
minimum.

7. IMPORTANT EXAMPLE VALUES
---------------------------
At (0,0):

    first term=1, second term=0, total=1

This point lies on the valley but has not reached x=1.

At (-1,1):

    first term=4, second term=0, total=4

Again, it is on the valley but not at the destination.

At (2,4):

    first term=1, second term=0, total=1

At (1,0):

    first term=0, second term=100, total=100

x is correct, but y is far from x^2.

At (0,1):

    first term=1, second term=100, total=101

8. WHY IT IS DIFFICULT
----------------------
The minimum is easy to state but difficult to reach because the valley is:

* narrow: leaving y=x^2 raises loss quickly;
* curved: the useful direction changes along the path;
* steep across its walls: gradients can be very large;
* relatively gentle along its length: forward progress can be slow.

Vanilla gradient descent may bounce from wall to wall. Momentum can dampen
sideways oscillation. Adam can adapt x and y updates using separate magnitude
histories.

9. EASY TO FIND, HARD TO FOLLOW
-------------------------------
An optimizer may rapidly reduce the large second term by reaching the vicinity
of y=x^2. It must then travel along the curved valley until x approaches 1.
This second stage may take many updates even though loss already looks much
smaller than at initialization.

10. THE ROAD ANALOGY
--------------------
Imagine a narrow curved road. The second term penalizes driving off the road.
The first term identifies the destination along the road. Optimization must
both remain near the road and progress toward (1,1).
"""


def rosenbrock_components(params, valley_weight=100.0):
    """Return both terms separately so their roles can be inspected."""
    x, y = params
    first_term = (1 - x) ** 2
    valley_error = y - x ** 2
    second_term = valley_weight * valley_error ** 2
    return first_term, second_term, valley_error


def rosenbrock(params, valley_weight=100.0):
    first_term, second_term, _ = rosenbrock_components(params, valley_weight)
    return first_term + second_term


def lies_on_valley(params, tolerance=1e-12):
    x, y = params
    return abs(y - x ** 2) <= tolerance


def describe_point(params):
    first, second, valley_error = rosenbrock_components(params)
    return {
        "point": list(params),
        "first_term": first,
        "valley_error": valley_error,
        "second_term": second,
        "total_loss": first + second,
        "on_valley": lies_on_valley(params),
    }


def compare_coefficient_effect(error_values=(0.01, 0.1, 1.0)):
    print("Effect of coefficient 100")
    for error in error_values:
        penalty = 100 * error ** 2
        print(f"valley error={error:5.2f} -> penalty={penalty:8.4f}")


def print_known_points():
    points = [(1, 1), (0, 0), (-1, 1), (2, 4), (1, 0), (0, 1)]
    print("\nRosenbrock point analysis")
    for point in points:
        record = describe_point(point)
        print(
            f"point={point!s:8s} first={record['first_term']:7.2f} "
            f"second={record['second_term']:7.2f} "
            f"loss={record['total_loss']:7.2f} "
            f"on_valley={record['on_valley']}"
        )


if __name__ == "__main__":
    assert rosenbrock([1, 1]) == 0
    assert rosenbrock([0, 0]) == 1
    assert rosenbrock([-1, 1]) == 4
    assert rosenbrock([2, 4]) == 1
    assert rosenbrock([1, 0]) == 100
    assert rosenbrock([0, 1]) == 101
    assert lies_on_valley([2, 4])
    assert not lies_on_valley([0, 1])

    compare_coefficient_effect()
    print_known_points()

