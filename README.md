# maze-solver-python
Solving a maze using BFS and DFS 

## Overview

This project demonstrates how classic search strategies explore paths in a grid-based maze.  
The maze is represented as a 2D grid where:

- `0` = free cell (walkable)
- `1` = wall (blocked)

The program attempts to find a valid path from a defined **start** position to a **goal** position using two fundamental algorithms:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**

The purpose of the project is to observe differences in traversal behaviour, efficiency, and path discovery.

---

## Problem Representation

The maze is modeled as a matrix (list of lists) of integers.  
Movement is allowed only to adjacent cells (up, right, down, left) that are within bounds and not blocked by walls.

Start and goal coordinates are explicitly defined.

---

## Algorithms Implemented

### Breadth-First Search (BFS)

BFS explores the maze level by level using a queue.  
It guarantees the shortest path in an unweighted grid if a solution exists.

### Depth-First Search (DFS)

DFS explores as deeply as possible along each branch using a stack.  
It may find a solution quickly but does not guarantee the shortest path.

---

## Metrics Observed

For each algorithm, the program reports:

- Number of nodes explored
- Execution time
- Path length

This allows comparison of search behaviour and efficiency.

---

## Output

The maze is printed in the console with:

- `S` = Start
- `G` = Goal
- `*` = Path (if found)

---

## How to Run

Ensure Python is installed, then run:

python maze_search.py
