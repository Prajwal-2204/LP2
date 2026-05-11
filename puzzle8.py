from heapq import heappush, heappop
from itertools import count

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

start = []

print("Enter the initial state row by row:")
for i in range(3):
    row = list(map(int ,input().split()))
    start.append(row)

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors

counter = count()

def a_star():
    pq = []

    heappush(pq, (heuristic(start), 0, next(counter), start, []))

    visited = set()

    while pq:
        f, g, _, current, path = heappop(pq)

        current_tuple = state_to_tuple(current)

        if current_tuple in visited:
            continue

        visited.add(current_tuple)

        path = path + [current]

        if current == goal:
            return path

        for neighbor in get_neighbors(current):
            neighbor_tuple = state_to_tuple(neighbor)

            if neighbor_tuple not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heappush(pq, (new_f, new_g, next(counter), neighbor, path))

    return None

solution = a_star()

if solution:
    print("\nSolution Path:\n")

    for index, step in enumerate(solution):
        print("Step:", index)

        for row in step:
            print(row)

        print()

    print("Total moves:", len(solution) - 1)

else:
    print("No solution found")

"""
Title
8-Puzzle Problem Using A* Algorithm in Python

Objective
To solve the 8-puzzle problem using the A* search algorithm and display the solution path from the initial state to the goal state.

Theory
The 8-puzzle problem is a sliding puzzle problem. It contains a 3 × 3 board with numbers from 1 to 8 and one blank space represented by 0. The goal is to move the blank space up, down, left, or right and arrange the tiles in the correct order.
A* Algorithm is an informed search algorithm. It uses both actual cost and estimated cost to find the best path. In this program, A* is used to reach the goal state from the given initial state.

The algorithm uses this formula:
f(n) = g(n) + h(n)
Here:
g(n) = number of moves taken from start state
h(n) = heuristic value
f(n) = total estimated cost

The heuristic used in this program is the number of misplaced tiles. It counts how many tiles are not in their correct position compared to the goal state. The blank tile 0 is ignored.
The priority queue is used to always select the state with the smallest f(n) value. This helps the algorithm move toward the goal efficiently.

Important Points

8-Puzzle
A 3 × 3 sliding puzzle.

Contains numbers 1 to 8 and blank space 0.


Goal State
Final required arrangement:
[1, 2, 3][4, 5, 6][7, 8, 0]

A Algorithm*
Finds best path using cost and heuristic.

Heuristic Function
Counts misplaced tiles.
Helps estimate distance from goal.

Priority Queue
Stores puzzle states based on smallest cost.

Blank Tile
Represented by 0.
Can move up, down, left, and right.

Visited Set
Stores already checked states.
Avoids repeated processing.

Neighbor States
New states created by moving the blank tile.

Solution Path
Stores all steps from start to goal.

Algorithm
Start the program.
Define the goal state.
Input the initial state from user.
Define heuristic function to count misplaced tiles.
Find the position of blank tile 0.
Generate possible neighbor states.
Insert start state into priority queue.
Repeat until queue is empty:
Remove state with minimum f(n).
If it is the goal state, return path.
Otherwise, generate its neighbors.
Calculate g, h, and f values.
Insert neighbors into priority queue.
Print solution path and total moves.
If no path found, print “No solution found”.


Conclusion
This program solves the 8-puzzle problem using the A* search algorithm. It uses the misplaced tiles heuristic to estimate the cost and a priority queue to select the best state. The program displays each step required to reach the goal state and shows the total number of moves."""