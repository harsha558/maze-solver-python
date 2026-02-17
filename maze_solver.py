from collections import deque
import time

# ---------------------------
# Maze (10 rows x 20 cols)
# '0' = free, '1' = wall
# Start = (0,1), Goal = (9,18)
# ---------------------------
maze = [
[ int(ch) for ch in list("00111111111111101100") ],
[ int(ch) for ch in list("10000000000111101100") ],
[ int(ch) for ch in list("11111011110000001100") ],
[ int(ch) for ch in list("11111011111101000000") ],
[ int(ch) for ch in list("10000000000001111101") ],
[ int(ch) for ch in list("10111111111101111101") ],
[ int(ch) for ch in list("10000000000000001101") ],
[ int(ch) for ch in list("11111111111011000101") ],
[ int(ch) for ch in list("10000001000001110001") ],
[ int(ch) for ch in list("11111111111111110001") ],
]

ROWS = len(maze)
COLS = len(maze[0])
start = (0, 1)
goal = (9, 18)

# Helper: get valid neighbors (Up, Right, Down, Left)
def neighbors(cell):
    r, c = cell
    for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and maze[nr][nc] == 0:
            yield (nr, nc)

# Reconstruct path from parent map (inclusive start->goal)
def reconstruct_path(parent, end):
    path = []
    cur = end
    while cur in parent or cur == start:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]
    path.reverse()
    return path

# Breadth-First Search (BFS)
def bfs(start, goal):
    t0 = time.perf_counter()
    queue = deque([start])
    parent = {}
    visited = set([start])
    nodes_explored = 0
    while queue:
        node = queue.popleft()
        nodes_explored += 1
        if node == goal:
            t1 = time.perf_counter()
            path = reconstruct_path(parent, goal)
            return path, nodes_explored, (t1 - t0)
        for nbr in neighbors(node):
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                queue.append(nbr)
    t1 = time.perf_counter()
    return None, nodes_explored, (t1 - t0)

# Iterative Depth-First Search (DFS)
def dfs(start, goal):
    t0 = time.perf_counter()
    stack = [start]
    parent = {}
    discovered = set([start])
    nodes_explored = 0
    while stack:
        node = stack.pop()
        nodes_explored += 1
        if node == goal:
            t1 = time.perf_counter()
            path = reconstruct_path(parent, goal)
            return path, nodes_explored, (t1 - t0)
        nbrs = list(neighbors(node))
        # keep neighbor order consistent
        for nbr in nbrs:
            if nbr not in discovered:
                discovered.add(nbr)
                parent[nbr] = node
                stack.append(nbr)
    t1 = time.perf_counter()
    return None, nodes_explored, (t1 - t0)

# Pretty-print maze with path. Path cells (except start/end) become '*', start='S', goal='G'
def print_maze_with_path(maze, path, title="Maze"):
    grid = [['1' if maze[r][c]==1 else '0' for c in range(COLS)] for r in range(ROWS)]
    if path:
        for (r,c) in path:
            grid[r][c] = '*'
        sr, sc = start
        gr, gc = goal
        grid[sr][sc] = 'S'
        grid[gr][gc] = 'G'
    print(f"\n{title}:")
    for row in grid:
        print(''.join(row))
    if path:
        print(f"Path length (cells including start and goal): {len(path)}")
    else:
        print("No path found")

# Run BFS and DFS, show results
b_path, b_nodes, b_time = bfs(start, goal)
d_path, d_nodes, d_time = dfs(start, goal)

print("=== RESULTS ===")
if b_path:
    print(f"BFS: found path, nodes explored = {b_nodes}, time = {b_time*1000:.3f} ms, steps = {len(b_path)-1}")
else:
    print(f"BFS: no path found, nodes explored = {b_nodes}, time = {b_time*1000:.3f} ms")

if d_path:
    print(f"DFS: found path, nodes explored = {d_nodes}, time = {d_time*1000:.3f} ms, steps = {len(d_path)-1}")
else:
    print(f"DFS: no path found, nodes explored = {d_nodes}, time = {d_time*1000:.3f} ms")

# Show visual mazes
print_maze_with_path(maze, b_path, title="BFS path (S=start, G=goal, *=path)")
print_maze_with_path(maze, d_path, title="DFS path (S=start, G=goal, *=path)")

# Summary for report
print("\n--- Summary (for report) ---")
print(f"Start: {start}")
print(f"Goal: {goal}")
print(f"BFS: nodes explored = {b_nodes}, time = {b_time*1000:.3f} ms, path length (edges) = {len(b_path)-1 if b_path else 'N/A'}")
print(f"DFS: nodes explored = {d_nodes}, time = {d_time*1000:.3f} ms, path length (edges) = {len(d_path)-1 if d_path else 'N/A'}")
