from collections import deque
matrix = [[0 for _ in range(5)] for _ in range(5)]
def get_coordinates(prompt):
    while True:
        try:
            x, y = map(int, input(prompt).split())
            if 0 <= x < 5 and 0 <= y < 5:
                return (x, y)
            else:
                print(" Please enter numbers between 0 and 4 (inclusive).")
        except ValueError:
            print(" Invalid input! Enter two numbers separated by a space.")
print("Enter start and goal positions as: row column (e.g., 0 0)")
start = get_coordinates("Enter START position: ")
goal = get_coordinates("Enter GOAL position: ")
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5 and matrix[x][y] == 0
def bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = current

    return None
path = bfs(start, goal)
if path:
    print("\nPath from start to goal:")
    for step in path:
        print(step)
else:
    print("\n No path found.")
if path:
    for (x, y) in path:
        matrix[x][y] = 1

print("\nMatrix with path marked as 1:")
for row in matrix:
    print(row)
