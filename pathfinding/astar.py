import heapq


def heuristic(a, b) -> int:
    """Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid: list[list[int]]) -> list[list[int, int]]:
    rows:  int = len(grid)
    cols:  int = len(grid[0])

    start = goal = None
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 3:
                start = (x, y)
            elif grid[y][x] == 4:
                goal = (x, y)

    if not start or not goal:
        return []

    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))  # (priority score, actual cost, current position)
    came_from = {}
    g_score = {start: 0}
    directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            x, y = neighbor
            if 0 <= x < cols and 0 <= y < rows and grid[y][x] != 1:
                tentative_g = current_g + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                    came_from[neighbor] = current
    return []
