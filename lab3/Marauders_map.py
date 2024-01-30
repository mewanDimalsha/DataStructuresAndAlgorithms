from collections import deque
H = int(input())
W = int(input())
starting_point = tuple(map(int, input().split()))
ending_point = tuple(map(int, input().split()))

grid = []
for _ in range(H):
    row = list(map(int, input().strip('[]').split(',')))
    grid.append(row)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < H and 0 <= y < W

def bfs(start, end):
    queue = deque([(start, 0)]) 
    visited = set(start) 
    while queue:
        current, distance = queue.popleft()
        if current == end:
            return distance  
        x, y = current
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), distance + 1))
                visited.add((new_x, new_y))

    return -1 

min_distance = bfs(starting_point, ending_point)
if(min_distance!= -1):
    print("The minimum distance is", min_distance)
else:
    print("There is no possible path")