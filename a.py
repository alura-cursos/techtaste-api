from collections import deque

def find_path(n, m, labyrinth):
  # Find the start and end positions
  start = None
  end = None
  for i in range(n):
    for j in range(m):
      if labyrinth[i][j] == 'A':
        start = (i, j)
      elif labyrinth[i][j] == 'B':
        end = (i, j)

  # Define the possible movements
  movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  directions = ['R', 'L', 'D', 'U']

  # Initialize the visited array and the queue for BFS
  visited = [[False] * m for _ in range(n)]
  queue = deque([(start, '')])

  # Perform BFS
  while queue:
    current, path = queue.popleft()
    i, j = current

    # Check if we reached the end
    if current == end:
      return 'YES', len(path), path

    # Check if the current position is valid and not visited
    if i < 0 or i >= n or j < 0 or j >= m or labyrinth[i][j] == '#' or visited[i][j]:
      continue

    # Mark the current position as visited
    visited[i][j] = True

    # Add the neighboring positions to the queue
    for movement, direction in zip(movements, directions):
      ni, nj = i + movement[0], j + movement[1]
      queue.append(((ni, nj), path + direction))

  # If we reach this point, there is no path
  return 'NO'

# Read input
n, m = map(int, input().split())
labyrinth = [list(input()) for _ in range(n)]

# Find path
result = find_path(n, m, labyrinth)

# Print output
print(result)