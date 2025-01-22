# Efficient Solvers for the Traveling Salesman Problem (TSP)

## Overview

This repository contains implementations of algorithms for solving the **Traveling Salesman Problem (TSP)**. The TSP is a combinatorial optimization problem where the goal is to find the shortest route to visit a set of cities exactly once and return to the starting city. The project provides two approaches: a basic brute-force implementation and an optimized solution using a Nearest Neighbor heuristic and Dynamic Programming.

---

## Features

- **Basic Solver**:
  - Implements a straightforward brute-force approach for TSP.
  - Reads `.tsp` files and calculates distances between nodes.
  - Suitable for small datasets but computationally expensive for larger inputs.

- **Optimized Solver**:
  - Uses the Nearest Neighbor heuristic and Dynamic Programming for improved efficiency.
  - Reduces runtime significantly compared to the basic brute-force approach.

- **Support for Standard TSP Input Format**:
  - Parses `.tsp` files containing city coordinates (e.g., `att48.tsp` and `att532.tsp`).

- **Visualization (Optional)**:
  - Plots the computed TSP route for better analysis.

---

## Prerequisites

To run this project, you need:

- **Python 3.6+**
- Required libraries:
  - NumPy
  - Matplotlib (optional, for visualization)

Install the dependencies using:
```bash
pip install numpy matplotlib
