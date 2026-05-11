from heapq import heappush, heappop

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
goal = int(input("Enter goal amount: "))

def heuristic(state):
    x, y = state
    return min(abs(x - goal), abs(y - goal))

def get_neighbors(state):
    x, y = state
    neighbors = []

    neighbors.append((jug1, y))
    neighbors.append((x, jug2))
    neighbors.append((0, y))
    neighbors.append((x, 0))

    transfer = min(x, jug2 - y)
    neighbors.append((x - transfer, y + transfer))

    transfer = min(y, jug1 - x)
    neighbors.append((x + transfer, y - transfer))

    return neighbors

def a_star():
    start = (0, 0)

    pq = []
    heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, current, path = heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        x, y = current

        if x == goal or y == goal:
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heappush(pq, (new_f, new_g, neighbor, path))

    return None

solution = a_star()

if solution:
    print("Solution Path:")
    for step in solution:
        print(step)
else:
    print("No solution found")


"""Title

Water Jug Problem Using A* Algorithm in Python

Objective

To solve the Water Jug Problem using the A* search algorithm and find the steps required to reach the goal amount of water.

Theory

The Water Jug Problem is a classic Artificial Intelligence problem. In this problem, two jugs with fixed capacities are given. The goal is to measure a required amount of water using these two jugs.

This program solves the Water Jug Problem using the A* algorithm. A* is an informed search algorithm that selects the best next state using cost and heuristic value.

The state of the problem is represented as:

(x, y)

Here:

x = current water in Jug 1
y = current water in Jug 2

The initial state is:

(0, 0)

This means both jugs are empty at the beginning.

The goal is reached when either Jug 1 or Jug 2 contains the required amount of water.

A* algorithm uses this formula:

f(n) = g(n) + h(n)

Where:

g(n) is the number of steps taken from the start state.
h(n) is the estimated distance from the goal.
f(n) is the total estimated cost.

In this program, the heuristic function calculates how close the current jug amount is to the goal:

min(abs(x - goal), abs(y - goal))

The program generates possible next states using operations like filling a jug, emptying a jug, and pouring water from one jug to another.

Important Points
Water Jug Problem
Measure a required amount using two jugs.
A Algorithm*
Uses cost and heuristic to find a solution path.
State Representation
A state is represented as (jug1_water, jug2_water).
Initial State
Both jugs start empty: (0, 0).
Goal State
Goal is reached if either jug contains the required amount.
Heuristic Function
Finds how close current jug values are to the goal.
Priority Queue
Stores states based on lowest f(n) value.
Visited Set
Avoids checking the same state again.
Possible Operations
Fill Jug 1.
Fill Jug 2.
Empty Jug 1.
Empty Jug 2.
Pour Jug 1 into Jug 2.
Pour Jug 2 into Jug 1.
Solution Path
Stores all states from start to goal.


Algorithm
Start the program.
Read capacity of Jug 1.
Read capacity of Jug 2.
Read goal amount.
Set initial state as (0, 0).
Insert initial state into priority queue.
Repeat until priority queue becomes empty:
Remove state with smallest f(n).
If state is already visited, skip it.
Add state to solution path.
If either jug contains the goal amount, return path.
Generate all possible neighbor states.
Calculate new cost and heuristic.
Insert neighbor states into priority queue.
If solution exists, print solution path.
Otherwise, print “No solution found”.
End the program.
Conclusion

This program solves the Water Jug Problem using the A* algorithm. It finds a sequence of steps by filling, emptying, and pouring water between two jugs. The heuristic helps the algorithm choose states closer to the goal, making the search more efficient."""