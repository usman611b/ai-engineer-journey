# Lesson 4 — Calculus, Optimisation, and Backpropagation for AI

> **The main question of this lesson:**
>
> A model makes a prediction and has some error. How can it know **which number to change**, **in which direction**, and **by how much** so that the error becomes smaller?

This is one complete revision guide. Read it from top to bottom when you return after a week or a month. The goal is to understand the story, not memorise isolated formulas.

---

## 1. The whole story first

Machine learning training is a repeating loop:

```text
input → prediction → error/loss → gradient → update weights → better prediction
```

For a simple line model:

```text
prediction = w * x + b
```

- `x` is an input, such as hours studied.
- `w` is a weight: how strongly `x` affects the prediction.
- `b` is a bias: a starting offset.
- `prediction` is what the model currently says.
- `target` is the correct answer.

We measure wrongness with a loss, for example:

```text
error = prediction - target
loss = error²
```

Then calculus gives a **gradient**. A gradient is an instruction such as:

```text
weight w: decrease it strongly
bias b:   decrease it a little
```

Gradient descent follows those instructions repeatedly.

---

## 2. Why calculus is needed in AI

An AI model may have millions or billions of weights. After it makes a wrong prediction, we cannot guess every weight change.

Think of each weight as a knob:

```text
weight knob → prediction → loss
```

We need to answer:

> “If I turn this one knob a tiny amount, what happens to the loss?”

That answer is a **derivative**. In a model with many knobs, the answers together are a **gradient**.

---

## 3. Derivatives: slope and rate of change

For the function:

```text
f(x) = x²
```

its derivative is:

```text
f'(x) = 2x
```

At `x = 3`, the derivative is `6`. If `x` goes up a tiny bit, `f(x)` goes up; the slope is positive.

At `x = -3`, the derivative is `-6`. If `x` goes up a tiny bit, `f(x)` goes down; the slope is negative.

At `x = 0`, the derivative is `0`. The graph is flat there.

For `x²`, zero is the minimum. But **derivative = 0 does not always mean minimum**. It may be a minimum, maximum, or saddle point. The Hessian helps us tell later.

### Three ways to get derivatives

1. **Analytical differentiation**: derive the exact rule with calculus. Example: derivative of `x²` is `2x`.
2. **Numerical differentiation**: estimate slope using tiny changes in input.
3. **Automatic differentiation**: software applies the chain rule automatically. PyTorch and TensorFlow use this. This is what real deep-learning work normally uses.

You should understand the first two so that automatic differentiation is not magic. You do not need to manually differentiate a huge neural network in real projects.

---

## 4. Learning rate: how big is one step?

The learning rate (`lr`) controls update size.

```text
new value = old value − learning rate × gradient
```

- Small learning rate: safe but slow.
- Large learning rate: fast at first, but can jump over the minimum or become unstable.
- `lr = 0`: no movement and no learning.

Example on `f(x) = x²`, starting at `x = 5`:

```py
x = 5.0
learning_rate = 0.1
gradient = 2 * x       # 10
x = x - learning_rate * gradient   # 5 - 0.1 * 10 = 4
```

The gradient says “uphill is positive.” To go downhill and reduce loss, subtract it.

---

## 5. Gradient descent: repeat the update

Gradient descent is the basic training algorithm.

```text
1. Start with a value (or random weights).
2. Calculate loss.
3. Calculate gradient.
4. Move opposite the gradient.
5. Repeat.
```

For `f(x) = x²`, `gradient = 2x`:

```py
x = 5.0
learning_rate = 0.1

for step in range(3):
    gradient = 2 * x
    x = x - learning_rate * gradient
    loss = x**2
    print(step + 1, x, loss)
```

The values are:

```text
start: x = 5
step 1: x = 4
step 2: x = 3.2
step 3: x = 2.56
```

It approaches zero because every step moves downhill. Notice that it usually gets closer and closer; it does not have to land exactly on zero.

---

## 6. Partial derivatives: one variable at a time

Real models have many weights, so their loss has many inputs.

Take:

```text
f(x, y) = x² + 3xy + y²
```

To find the partial derivative with respect to `x`, treat `y` as a constant:

```text
∂f/∂x = 2x + 3y
```

To find the partial derivative with respect to `y`, treat `x` as a constant:

```text
∂f/∂y = 3x + 2y
```

The `3xy` term connects the variables. When differentiating with respect to `x`, `y` is a fixed number, so `3xy` becomes `3y`. When differentiating with respect to `y`, `x` is fixed, so it becomes `3x`.

At `(x, y) = (1, 2)`:

```text
∂f/∂x = 2(1) + 3(2) = 8
∂f/∂y = 3(1) + 2(2) = 7
```

---

## 7. Gradient vector: one instruction for every variable

The gradient collects all partial derivatives:

```text
∇f(x, y) = [∂f/∂x, ∂f/∂y]
```

For the previous function:

```text
∇f(1, 2) = (8, 7)
```

This means the function increases if we increase `x`, and also increases if we increase `y`. So gradient descent decreases both:

```text
x_new = x − lr × 8
y_new = y − lr × 7
```

If a gradient is `(-5, 12)`:

- subtracting `-5` makes `x` increase;
- subtracting `12` makes `y` decrease.

So a gradient is not “the answer.” It is a direction-and-strength instruction for each parameter.

```py
def f(x, y):
    return x**2 + 3*x*y + y**2

def grad(x, y):
    x_grad = 2*x + 3*y
    y_grad = 3*x + 2*y
    return x_grad, y_grad

def gradient_descent_2d(x, y, learning_rate, steps):
    for step in range(steps):
        x_gradient, y_gradient = grad(x, y)
        x = x - learning_rate * x_gradient
        y = y - learning_rate * y_gradient
        print(step + 1, x, y, f(x, y))
    return x, y
```

In AI, replace `x` and `y` with weights such as `w1`, `w2`, and bias `b`.

---

## 8. Chain rule: how an early weight affects final loss

Neural networks are chains of calculations:

```text
weight → hidden value → prediction → error → loss
```

The chain rule connects the effect across each small link:

```text
d(loss)/d(weight)
= d(loss)/d(error)
  × d(error)/d(prediction)
  × d(prediction)/d(weight)
```

The idea is more important than memorising the symbols:

> To see how one early value affects the final loss, multiply its effect through every later step.

### One-weight neural example

```text
prediction = w × x
error = prediction − target
loss = error²
```

The weight gradient is:

```text
dL/dw = 2 × error × x
```

Why?

```text
loss changes with error:          2 × error
error changes with prediction:    1
prediction changes with weight:   x
```

Multiply them: `2 × error × 1 × x`.

If prediction is too high, error is positive. With positive `x`, the gradient is positive, so gradient descent decreases `w`. That makes the next prediction lower.

If prediction is too low, error is negative. The update makes `w` increase, lifting the next prediction.

### Bias gradient

For:

```text
prediction = w×x + b
```

the bias changes prediction by exactly `1`, so:

```text
dL/db = 2 × error
```

---

## 9. Backpropagation: the practical name for this process

**Backpropagation** means calculating the loss signal backwards through the network, using the chain rule.

Simple meaning:

> Backpropagation finds how much each weight contributed to the final loss, then gives that weight a gradient instruction to reduce the loss.

It is not a separate magical algorithm from the chain rule. It is the chain rule applied efficiently from the loss back toward all earlier weights.

For a hidden connection:

```text
h = w × x
prediction = v × h
```

- Effect of `w` on `h` is `x`.
- Effect of `h` on prediction is `v`.
- Then the loss signal travels backward through those links.

Backprop gives every weight its own instruction. The gradient tells the direction and strength of that instruction.

---

## 10. Activation functions and sigmoid

Networks use activation functions to make learning non-linear patterns possible.

For sigmoid:

```text
a = sigmoid(z) = 1 / (1 + e^(-z))
```

Its useful derivative is:

```text
da/dz = a × (1 − a)
```

This lets us compute the slope from the activation value `a`, which is convenient during backpropagation. In real code, frameworks calculate these gradients automatically.

---

## 11. Training on a dataset: loss and gradients are averaged

Suppose data follows:

```text
y = 2x + 1
```

Training examples:

```py
xs = [1.0, 2.0, 3.0, 4.0, 5.0]
ys = [3.0, 5.0, 7.0, 9.0, 11.0]
```

For every example, the model predicts, measures error, and makes a gradient contribution. We add all contributions, then divide by the number of examples.

```py
import random

random.seed(42)
w = random.gauss(0, 1)
b = random.gauss(0, 1)
lr = 0.01

for epoch in range(200):
    total_loss = 0
    dw = 0
    db = 0

    for x, y in zip(xs, ys):
        pred = w * x + b
        error = pred - y
        total_loss += error**2
        dw += 2 * error * x
        db += 2 * error

    dw /= len(xs)
    db /= len(xs)
    total_loss /= len(xs)

    w -= lr * dw
    b -= lr * db

print(w, b)
```

Why average?

- It represents the typical error/gradient for the data.
- It prevents an update from becoming larger merely because we repeated or added examples.
- The average loss is the expected loss over this small dataset.

An **epoch** means one full pass through all training examples.

Important printing detail: in this code, `total_loss` is calculated using the old `w` and `b`, then `w` and `b` are updated. So the printed loss belongs to before that epoch’s update, while the printed weights belong to after it.

---

## 12. Why basic gradient descent can struggle

Ordinary gradient descent uses only the current gradient. This can be slow, zig-zag in narrow valleys, or need careful learning-rate tuning.

Optimisers improve how we use gradients. They do not replace gradients or backpropagation.

```text
backpropagation → calculates gradients
optimiser       → uses gradients to update weights
```

-----

## 13. Momentum: remember previous movement

Momentum keeps a velocity, like a ball rolling downhill:

```text
velocity = momentum × old_velocity − learning_rate × gradient
x = x + velocity
```

If gradients keep pointing in a similar direction, momentum builds speed. If updates jump left-right, old movement can partly cancel the noise.

```py
velocity = 0.0
x = 5.0

for step in range(5):
    gradient = 2 * x
    velocity = 0.9 * velocity - 0.1 * gradient
    x = x + velocity
    print(step + 1, x, velocity)
```

Momentum can overshoot the minimum. That is not automatically a mistake: the loss is still `x²`, so it is never negative. A negative `x` is just a point on the other side of zero.

---

## 14. RMSProp: adjust step size per direction

RMSProp remembers recent **squared gradients**:

```text
s = decay × old_s + (1 − decay) × gradient²
parameter = parameter − lr × gradient / (sqrt(s) + epsilon)
```

- Large, repeated gradients make `s` large, reducing future steps.
- Small gradients allow relatively larger steps.
- `epsilon` prevents division by zero.

It uses the square root because `s` contains squared units. The square root puts the scale back in the same kind of units as the gradient.

---

## 15. Adam: momentum + RMSProp

Adam is commonly used for neural-network training. It combines:

- `m`: moving average of gradients (direction/momentum)
- `v`: moving average of squared gradients (size adjustment)

```text
m = beta1 × m + (1 − beta1) × gradient
v = beta2 × v + (1 − beta2) × gradient²
```

At the start, these moving averages are biased toward zero because they start at zero. Adam corrects that:

```text
m_hat = m / (1 − beta1^t)
v_hat = v / (1 − beta2^t)
parameter = parameter − lr × m_hat / (sqrt(v_hat) + epsilon)
```

We do **not** square-root `m`: it must keep its positive/negative direction. We square-root `v` because it stores squared magnitude.

In practice, Adam is often a strong default. The framework provides it; you need to understand why it exists, not write it from memory every time.

---

## 16. Second derivatives and the Hessian

The first derivative describes slope. The second derivative describes curvature.

For one variable:

- `f''(x) > 0`: bowl shape; possible local minimum.
- `f''(x) < 0`: upside-down bowl; possible local maximum.

For two variables, the **Hessian** is a table of second partial derivatives:

```text
H = [[fxx, fxy],
     [fyx, fyy]]
```

At a stationary point (gradient is zero), calculate:

```text
D = fxx × fyy − (fxy)²
```

- `D > 0` and `fxx > 0` → local minimum.
- `D > 0` and `fxx < 0` → local maximum.
- `D < 0` → saddle point.
- `D = 0` → test cannot decide.

Examples at `(0, 0)`:

```text
x² + y²  → minimum (bowl)
−x² − y² → maximum (hill)
x² − y²  → saddle (up in x direction, down in y direction)
```

The Hessian is useful for understanding curvature. Modern deep-learning models normally use first-order optimisers such as Adam instead, because a full Hessian is extremely expensive for millions of weights.

---

## 17. Taylor approximation, Newton’s method, L-BFGS, natural gradient

These are important ideas to recognise. You do not need to memorise their full code now.

### Taylor approximation

Near a point, a complicated function can be approximated by a simpler polynomial. A first-order approximation uses slope; a second-order approximation also uses curvature.

### Newton’s method

Newton uses gradient and curvature/Hessian:

```text
new position = old position − inverse(Hessian) × gradient
```

For an exact quadratic bowl, it can go directly to the minimum. For real neural networks, computing and inverting a huge Hessian is usually too expensive and may be unstable.

### L-BFGS

L-BFGS estimates useful curvature information from past gradients rather than storing the full Hessian. It can be good for smaller optimisation problems, but is not the usual default for large deep-learning training.

### Natural gradient

Natural gradient changes the update direction using the geometry of probability distributions. It can be useful in specialised probabilistic settings, but it is more expensive and less commonly the first tool for standard neural networks.

---

## 18. Integrals and expected loss

Derivatives ask: “How fast is this changing here?”

Integrals ask: “What total amount accumulates over a range?”

In machine learning, an expected loss means the average loss over all possible data. With a finite dataset, we estimate it using an average:

```text
average loss = total loss / number of examples
```

That is why batch and dataset training average the loss and gradients.

---

## 19. Jacobian: many outputs and many inputs

A gradient is used when one output depends on many inputs.

A **Jacobian** is used when many outputs depend on many inputs. It is a table:

```text
rows    = outputs
columns = inputs
entries = derivatives
```

This appears inside neural-network calculations, but automatic differentiation handles it in real frameworks. For now, understand the idea: it records how each output changes with each input.

---

## 20. The final connected mental model

```text
Input data
    ↓
Weights and bias make a prediction
    ↓
Loss measures how wrong it is
    ↓
Derivatives / partial derivatives measure sensitivity
    ↓
Chain rule carries loss information backward
    ↓
Backpropagation calculates every weight’s gradient
    ↓
An optimiser (GD, Momentum, RMSProp, Adam) updates weights
    ↓
Repeat across data until loss becomes low enough
```

The model is not “thinking” the correct answer. It starts with imperfect/random parameters, makes predictions, gets a numerical signal about the error, and gradually adjusts each parameter.

---

## 21. What to truly remember

You do **not** need to write every formula from scratch right now. Your target is to understand and be able to explain:

1. A derivative tells how output changes when an input changes a little.
2. A partial derivative changes one variable while holding others fixed.
3. A gradient gives one slope instruction per parameter.
4. Gradient descent subtracts the gradient to move toward lower loss.
5. Learning rate controls how large that move is.
6. The chain rule connects an early weight to final loss through every step between them.
7. Backpropagation applies the chain rule backwards to calculate gradients for all weights.
8. An optimiser decides how to use those gradients: plain GD, Momentum, RMSProp, or Adam.
9. Loss decreasing is the sign that learning is working.
10. Libraries calculate complicated derivatives/backpropagation automatically; your conceptual understanding lets you use them correctly.

### Common mistakes to avoid

- A negative **gradient** does not mean negative loss. It means the update direction changes.
- A negative `x` does not mean negative `x²` loss.
- Gradient descent subtracts the gradient because the gradient points uphill.
- In a partial derivative, treat the other variables as constants.
- Update `x` and `y` using their gradients; do not update the gradients themselves.
- In dataset training, calculate all gradients for the batch before changing the weights.
- Loss does not need to become exactly zero. We aim for a small enough loss and good performance on new data.

---

## 22. Where this leads next

Lesson 4 gave you the mathematical engine behind training. Later, when you use neural-network libraries, you will see the practical version:

```py
loss.backward()    # backpropagation calculates gradients
optimizer.step()   # Adam/SGD updates weights
optimizer.zero_grad()
```

Now those lines have a meaning:

- `loss.backward()` = “tell every weight how it affected the loss.”
- `optimizer.step()` = “move each weight according to its instruction.”

That is the foundation of learning in neural networks.
