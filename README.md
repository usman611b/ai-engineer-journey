<div align="center">

# AI Engineer Journey

### From first principles → intelligent systems

**A public engineering lab for mathematics, machine learning, deep learning, data systems, and production AI.**

![Python](https://img.shields.io/badge/Python-111827?style=flat-square&logo=python&logoColor=FFD43B)
![Math for AI](https://img.shields.io/badge/Math_for_AI-111827?style=flat-square&logo=wolfram&logoColor=FF6B35)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-111827?style=flat-square&logo=scikitlearn&logoColor=F7931E)
![Deep Learning](https://img.shields.io/badge/Deep_Learning-111827?style=flat-square&logo=pytorch&logoColor=EE4C2C)
![Systems](https://img.shields.io/badge/Systems_Thinking-111827?style=flat-square&logo=linux&logoColor=FCC624)

</div>

---

## What this repository is

This is not a checklist of technologies I want to claim.

It is a **working record of how I build understanding**: concepts are unpacked, implemented, tested, compared, broken, debugged, and connected to the larger AI engineering stack.

The long-term question behind the repository is:

> **How do we move from mathematical ideas and learning algorithms to intelligent systems that are useful, reliable, and deployable?**

That means the repository grows in layers: foundations first, then models, then systems.

---

## Current lab

### Optimization & learning dynamics

Recent work focuses on the behavior of optimization algorithms rather than treating them as black-box library calls.

Topics currently being explored include:

- gradient-based optimization;
- batch, stochastic, and mini-batch updates;
- momentum;
- Adam;
- learning-rate behavior and schedules;
- convex vs non-convex optimization;
- saddle points and plateaus;
- sharp vs flat minima;
- loss landscapes;
- Rosenbrock-style benchmark problems;
- optimizer comparison through executable experiments.

**Working loop:**

```text
intuition → mathematics → implementation → experiment → interpretation
```

Explore the active material in [`math-for-ai/day-21`](./math-for-ai/day-21).

---

## Repository map

```text
ai-engineer-journey/
│
├── python-for-ai/      # Language + engineering foundations
├── math-for-ai/        # Mathematics, probability, autodiff, Bayes, optimization
└── README.md            # Lab index and engineering narrative
```

The repository is intentionally expanded only when the corresponding material is actually being studied and implemented. Future layers such as machine learning, deep learning, data systems, LLMs, agents, and MLOps will appear as real work is added — not as empty folders.

---

## Foundation track

### Python for AI

The Python track builds the programming habits needed to reason about and implement AI systems rather than only operate notebooks.

It covers language fundamentals, functions, object-oriented design, iteration patterns, error handling, concurrency concepts, and practical Python engineering.

→ [`python-for-ai/`](./python-for-ai)

### Mathematics for AI

The mathematics track is where abstract ideas are turned into executable intuition.

The current material spans topics such as:

- linear algebra and vector reasoning;
- probability and distributions;
- expected value and variance;
- Gaussian behavior and uncertainty;
- Bayes' theorem;
- likelihood, MLE, MAP, and Beta distributions;
- automatic differentiation and computational graphs;
- gradient-based optimization and optimizer behavior.

→ [`math-for-ai/`](./math-for-ai)

---

## How I use this repo

Every serious topic should leave behind more than a note.

A strong module aims to contain some combination of:

| Evidence | What it proves |
|---|---|
| Theory notes | I can explain the idea in my own words |
| From-scratch implementation | I understand the mechanism below the library call |
| Numerical example | I can trace the mathematics concretely |
| Experiment | I can test assumptions instead of only repeating them |
| Comparison | I can reason about trade-offs |
| Visualization | I can inspect behavior, not just final numbers |
| Reflection | I can explain what failed, surprised me, or changed my understanding |

The point is to leave an **engineering trail**, not just completed exercises.

---

## Learning architecture

```text
FOUNDATIONS
  ↓
DATA + REPRESENTATION
  ↓
MACHINE LEARNING
  ↓
DEEP LEARNING
  ↓
INTELLIGENT APPLICATIONS
  ↓
INFRASTRUCTURE + MLOPS
  ↓
PRODUCTION AI SYSTEMS
```

I am intentionally moving through this stack from the bottom upward so that later abstractions have something solid underneath them.

---

## Build log philosophy

Commits in this repository are meant to describe **what changed in the understanding**, not simply say `update files`.

Examples from the current optimization work include:

```text
Day 21 Session 09: explain convex and non-convex optimization
Day 21 Session 11: explain loss landscapes
Day 21 Session 14: derive the Rosenbrock gradient
Day 21 Session 17: compare GD, momentum, and Adam
Day 21 Session 18: add optimization experiments and practice
```

That commit history is part of the learning record.

---

## What comes next

The next major layers will be added when they become active work:

**Data analysis → Machine learning → Deep learning → Computer vision / NLP → LLM systems → Agents → MLOps / deployment → production-scale projects**

The goal is not speed through the labels. The goal is to build enough understanding that each new layer connects naturally to the previous one.

---

## Principles

- **Understand before abstracting.**
- **Implement before depending.**
- **Experiment before concluding.**
- **Debug instead of hiding failure.**
- **Connect every model to the system around it.**
- **Keep the evidence.**

---

<div align="center">

### Engineering, evidenced.

[GitHub Profile](https://github.com/usman611b) · [Portfolio](https://www.usmanalii.com/)

</div>
