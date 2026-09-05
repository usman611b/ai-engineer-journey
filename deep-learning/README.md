# Deep Learning

This directory is the evidence trail for my **7th-semester Deep Learning course** and its connection to my wider AI Engineering Journey.

The aim is not only to complete university theory and lab requirements. Each important topic should become something I can explain mathematically, implement from first principles, compare with a framework implementation, test experimentally, and connect to a real AI system.

## Current status

| Item | Status |
|---|---:|
| University syllabus mapping | ⏳ Awaiting course outline |
| Theory sequence | ⏳ To be mapped |
| Lab sequence | ⏳ To be mapped |
| First implementation artifact | ⏳ Not started |

This course track runs alongside the current mathematical-foundations work. Creating this directory does **not** claim that Phase 4 of the main roadmap is complete or that its prerequisites should be skipped.

## Learning sequence

Every substantial concept will be studied through this progression:

```text
INTUITION
   ↓
SMALL NUMERICAL EXAMPLE
   ↓
MATHEMATICS + DERIVATION
   ↓
MANUAL CALCULATION
   ↓
FROM-SCRATCH IMPLEMENTATION
   ↓
NUMPY IMPLEMENTATION
   ↓
PYTORCH EQUIVALENT
   ↓
EXPERIMENT + FAILURE ANALYSIS
   ↓
REAL AI-SYSTEM CONNECTION
```

For implementable fundamentals, the default order is:

1. Pure Python to expose the mechanism.
2. NumPy when vectorization becomes the natural next step.
3. PyTorch only after the underlying operation is understood.

## Depth standard

The track will cover both required university material and deeper engineering understanding:

- first-principles intuition and mathematical derivations;
- assumptions behind formulas and architectures;
- computational graphs, tensor shapes, and internal data flow;
- edge cases, failure modes, and debugging signals;
- alternative methods and evidence-based comparisons;
- training, validation, evaluation, checkpoints, and reproducibility;
- modern practice without hiding foundations behind high-level APIs;
- precise, respectful technical questions for incomplete classroom explanations.

## Existing foundations to reuse

The Deep Learning track will explicitly connect to existing repository work instead of restarting it blindly:

- linear algebra and transformations;
- derivatives, partial derivatives, and the chain rule;
- backpropagation and reverse-mode automatic differentiation;
- probability distributions, log-probabilities, softmax, and cross-entropy;
- Bayesian reasoning, MLE, and MAP;
- gradient descent, SGD, Momentum, Adam, schedules, and loss landscapes.

Relevant foundations are currently documented under [`../math-for-ai`](../math-for-ai).

## Planned repository organization

The exact lesson folders will be created after the university syllabus is mapped. No empty lesson directories will be added merely for appearance.

Each completed lesson may contain:

```text
deep-learning/
├── README.md
└── day-NN/
    ├── README.md                 # concept notes, derivations, conclusions
    ├── session01-*.py           # first-principles implementation
    ├── session02-*.py           # NumPy implementation or experiment
    ├── session03-*.py           # PyTorch equivalent
    └── assets/                  # plots or other evidence when needed
```

The structure may be refined once the official theory and lab outlines are available, but all Deep Learning progress will remain inside this directory.

## Evidence required before marking a topic complete

A topic is complete only when the relevant evidence exists:

- a clear explanation in my own words;
- a derivation or traceable numerical calculation;
- a from-scratch implementation where appropriate;
- a NumPy and/or PyTorch comparison;
- at least one meaningful experiment;
- interpretation of results and failure modes;
- a connection to a larger model or production concern.
