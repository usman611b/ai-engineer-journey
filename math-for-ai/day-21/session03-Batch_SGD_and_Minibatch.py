"""
DAY 21 — SESSION 03: BATCH GD, SGD, AND MINI-BATCH GD
=====================================================

1. THE QUESTION THESE TERMS ANSWER
----------------------------------
A dataset contains many examples, and each example can suggest a gradient. How
many examples should contribute to a gradient before parameters are updated?

The update formula can remain identical:

    w_new = w - lr * estimated_gradient

What changes is how estimated_gradient is calculated.

2. STEP/UPDATE VERSUS EPOCH
---------------------------
A step (update) changes parameters once. An epoch means every training example
has been processed once. They are not synonyms.

    updates_per_epoch = ceil(dataset_size / batch_size)

For 1000 examples:

    batch size 1000 -> 1 update/epoch
    batch size 1    -> 1000 updates/epoch
    batch size 50   -> 20 updates/epoch

The ceiling matters when the final batch is incomplete: 103 examples with batch
size 20 require 6 updates (five groups of 20 and one group of 3).

3. BATCH GRADIENT DESCENT
-------------------------
Use the complete dataset, average all example gradients, then update once.

Example gradients [2,4,6,8]:

    batch_gradient = (2+4+6+8)/4 = 5
    w_new = w - lr(5)

It is like asking every example for an opinion before moving. The gradient is
stable and exact for the current dataset, but each update can be slow and may
not fit into memory for enormous datasets.

4. PURE STOCHASTIC GRADIENT DESCENT
-----------------------------------
Use one shuffled example and update immediately. With gradients [2,4,6,8], SGD
takes four updates rather than averaging first.

"Stochastic" means randomness is involved: data is shuffled and a single
example is a noisy estimate of the full gradient. One example may pull left and
the next right. Individual steps are cheap and learning starts immediately,
but the path is noisy and processing one item poorly utilizes GPU parallelism.

5. MINI-BATCH GRADIENT DESCENT
------------------------------
Use a small group such as 32, 64, 128, or 256. With [2,4,6,8] and batch size 2:

    first gradient  = (2+4)/2 = 3  -> update
    second gradient = (6+8)/2 = 7  -> update

Mini-batches balance the extremes:

* more reliable than one example;
* lower memory and more frequent updates than the whole dataset;
* efficient matrix operations on GPUs;
* retains some useful gradient noise.

This is the standard deep-learning approach. In practice, "SGD" commonly means
mini-batch SGD rather than mathematically pure single-example SGD.

6. WHY NOISE CAN HELP
---------------------
Noise is not always a defect. A perfectly deterministic gradient may travel
into a flat or shallow undesirable region. Different mini-batches perturb the
direction and can help movement through saddle regions. Too much noise is still
harmful; batch size controls this tradeoff.

7. MORE UPDATES DO NOT AUTOMATICALLY MEAN BETTER
------------------------------------------------
Pure SGD has the most updates per epoch, but each gradient has high variance.
Batch GD has one accurate update, but it is expensive. Mini-batch training wins
practically because it balances information quality, frequency, memory, and
hardware throughput.

8. BATCH SIZE AND OPTIMIZER ARE DIFFERENT CHOICES
-------------------------------------------------
Batching decides which data calculates the gradient. Momentum or Adam decides
how gradients update parameters. We can use mini-batches with vanilla GD,
momentum, or Adam.
"""

import math
import random


def updates_per_epoch(dataset_size, batch_size):
    if dataset_size <= 0 or batch_size <= 0:
        raise ValueError("dataset_size and batch_size must be positive")
    return math.ceil(dataset_size / batch_size)


def make_batches(values, batch_size, shuffle=False, seed=42):
    values = list(values)
    if shuffle:
        random.Random(seed).shuffle(values)
    return [values[i:i + batch_size] for i in range(0, len(values), batch_size)]


def average(numbers):
    return sum(numbers) / len(numbers)


def demonstrate_gradient_estimates():
    gradients = [2, 4, 6, 8]
    print("Batch GD gradient:", average(gradients))
    print("Pure SGD gradients:", gradients)
    mini_batches = make_batches(gradients, batch_size=2)
    print("Mini-batches:", mini_batches)
    print("Mini-batch gradients:", [average(batch) for batch in mini_batches])
    print("1000 examples, batch size 50:", updates_per_epoch(1000, 50))
    print("103 examples, batch size 20:", updates_per_epoch(103, 20))


if __name__ == "__main__":
    demonstrate_gradient_estimates()

