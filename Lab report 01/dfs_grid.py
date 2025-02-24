import random

def generate_grid(N, obstacle_prob=0.3):
    grid = [[0 if random.random() > obstacle_prob else 1 for _ in range(N)] for _ in range(N)]
    return grid

def get_valid_position(grid, N):
    while True:
        x, y = random.randint(0, N-1), random.randint(0, N-1)
        if grid[x][y] == 0:
            return (x, y)

def dfs(grid, start, goal, N):
    stack = [start]
    visited = set()
    parent = {}
    topological_order = []

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        topological_order.append((x, y))
        if (x, y) == goal:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = (x, y)

    path = []
    if goal in visited:
        node = goal
        while node != start:
            path.append(node)
            node = parent.get(node, start)
        path.append(start)
        path.reverse()
    
    return path, topological_order

def print_grid(grid, N, start, goal, path):
    for i in range(N):
        for j in range(N):
            if (i, j) == start:
                print('S', end=' ')
            elif (i, j) == goal:
                print('G', end=' ')
            elif (i, j) in path:
                print('.', end=' ')
            elif grid[i][j] == 1:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()

def main():
    N = random.randint(4, 7)
    grid = generate_grid(N)
    source = get_valid_position(grid, N)
    goal = get_valid_position(grid, N)
    while source == goal:
        goal = get_valid_position(grid, N)
    
    path, topological_order = dfs(grid, source, goal, N)
    print("Grid:")
    print_grid(grid, N, source, goal, path)
    print("\nSource:", source)
    print("Goal:", goal)
    print("DFS Path:", path if path else "No path found")
    print("Topological Order:", topological_order)

if __name__ == "__main__":
    main()
