# Math for AI — Lab Index

> Mathematics here is treated as executable intuition: explain it, calculate it, implement it, then test what changes when the assumptions change.

This track contains the mathematical foundations I am using to build a deeper understanding of machine learning and intelligent systems.

## Active learning pattern

```text
concept → intuition → derivation → numerical example → Python implementation → experiment
```

The goal is not symbolic manipulation for its own sake. Each topic should eventually answer a practical engineering question: **what behavior does this mathematics create inside a learning system?**

---

## Recent modules

### [Day 20 — Bayesian reasoning, likelihood & uncertainty](./day-20)

A hands-on Bayesian module covering ideas such as:

- Bayesian thinking and conditional-probability reversal;
- prior, likelihood, evidence, and posterior;
- total probability and Bayes derivation;
- base-rate effects in diagnostic-style examples;
- sequential Bayesian updating;
- Naive Bayes classification;
- Laplace smoothing;
- log probabilities and numerical underflow;
- maximum likelihood estimation;
- MAP-style reasoning and uncertainty-oriented thinking.

The emphasis is on understanding how evidence changes belief — and how those ideas later appear in statistical learning.

### [Day 21 — Optimization & learning dynamics](./day-21)

An optimization lab built around understanding the mechanics behind parameter updates rather than treating optimizers as configuration choices.

Current work includes:

- gradient descent;
- stochastic and mini-batch updates;
- momentum;
- Adam;
- learning-rate schedules;
- convex and non-convex behavior;
- saddle points and plateaus;
- loss landscapes;
- sharp vs flat minima;
- Rosenbrock-style benchmark problems;
- optimizer comparison through experiments.

The key question is: **why does an optimizer behave the way it does on a particular landscape?**

---

## Earlier foundation work

The surrounding day folders contain the build-up toward the current modules, including probability, distributions, uncertainty, automatic differentiation, and other mathematical tools that become useful once models start learning from data.

Browse the track from [`day-13`](./day-13) through the latest day folders to see the progression.

---

## What a strong session should contain

- a plain-language explanation;
- the mathematical object or equation involved;
- at least one concrete numerical example;
- a Python implementation;
- an experiment, comparison, or visualization when useful;
- a short note on **why this matters for AI/ML**.

That structure keeps the mathematics connected to engineering rather than isolated from it.

---

[← Back to AI Engineer Journey](../README.md)
