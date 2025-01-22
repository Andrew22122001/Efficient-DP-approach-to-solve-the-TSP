# Efficient Dynamic Programming Approach to Solve the TSP

## Overview

This repository contains an implementation of an **Efficient Dynamic Programming (DP) solution for the Traveling Salesman Problem (TSP)**. The TSP is a classic combinatorial optimization problem that seeks the shortest route to visit a set of cities exactly once and return to the starting city. This project uses a state-compression DP technique to optimize the computational efficiency while maintaining accuracy.

---

## Features

- **Dynamic Programming with State Compression**: Efficiently manages the exponential growth of possible routes by using a bitmask representation for visited cities.
- **Customizable Input**: Supports user-defined distance matrices for flexibility.
- **Optimal Route Finder**: Computes the shortest path visiting all cities exactly once and returning to the starting point.
- **Cost Calculation**: Displays the total cost of the computed optimal route.
- **Visualization (Optional)**: Plots the optimal route using Matplotlib for graphical representation of city connections.

---

## Prerequisites

To run this project, you need:

- **Python**: Version 3.6 or above.
- **Required Libraries**:
  - NumPy: For efficient numerical operations.
  - Matplotlib (optional): For visualization of the computed route.

Install the dependencies using:
```bash
pip install numpy matplotlib
