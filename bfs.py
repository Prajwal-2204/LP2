def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    order = []
    step = 0

    print(f"\nStep 0: INIT     start = {start_node}")
    print(f"         Queue   : {queue}")
    print(f"         Visited : {sorted(visited)}")
    print(f"         Order   : {order}")
    print()

    while queue:
        step += 1
        current_node = queue.pop(0)
        order.append(current_node)

        print(f"Step {step}: DEQUEUE  node = {current_node}")
        print(f"         Queue   : {queue}")
        print(f"         Visited : {sorted(visited)}")
        print(f"         Order   : {order}")
        print()

        for neighbor in graph[current_node]:
            step += 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

                print(f"Step {step}: ENQUEUE  {current_node} → {neighbor} (unvisited, added to queue)")
            else:
                print(f"Step {step}: SKIP     {current_node} → {neighbor} (already visited)")

            print(f"         Queue   : {queue}")
            print(f"         Visited : {sorted(visited)}")
            print(f"         Order   : {order}")
            print()

    return order


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"\nEnter node {i+1}: ")
    
    neighbors = input(
        f"Enter neighbors of {node}: "
    ).split()

    graph[node] = neighbors

start_node = input("\nEnter starting node for BFS: ")

print("\n" + "=" * 50)
print("BFS TRAVERSAL — STEP BY STEP")
print("=" * 50)

result = bfs(graph, start_node)

print("=" * 50)
print(f"FINAL BFS ORDER: {result}")
print("=" * 50)



"""
Title

Breadth First Search (BFS) Traversal in Python

Objective

To implement the Breadth First Search (BFS) algorithm for graph traversal and understand how nodes are visited level by level using a queue.

Theory (Simple and Detailed)

Breadth First Search (BFS) is a graph traversal algorithm used to visit all nodes of a graph systematically.

In BFS, traversal starts from a selected starting node and explores all its neighboring nodes first. After visiting all immediate neighbors, it moves to the next level of neighbors. Because of this behavior, BFS is also called level-order traversal.

BFS uses two important things:

1. Queue (FIFO)

Queue follows the rule:
First In First Out (FIFO)

The first node inserted into the queue is removed first.
Newly discovered nodes are added at the end of the queue.

Example:

Queue = [A]

Remove A
Add B and C

Queue = [B, C]
2. Visited Set

A visited set stores nodes that are already visited.

Why needed?

To avoid visiting the same node multiple times.
Prevents infinite loops in cyclic graphs.

Example:

Visited = {A, B, C}
Working of BFS

Suppose graph is:

A → B, C
B → D
C → D
D → -

Start from node A

Step-by-step traversal:
Visit A
Add neighbors B and C
Visit B
Add neighbor D
Visit C
D already discovered
Visit D

Final BFS order:

A → B → C → D
Features of BFS
Traverses graph level by level
Uses Queue data structure
Guarantees shortest path in unweighted graphs
Simple and efficient traversal technique
Applications of BFS
Shortest path finding
GPS and map navigation
Social networking suggestions
Web crawling
Network broadcasting
AI search problems
Algorithm
Create an empty visited set.
Create a queue and insert the starting node.
Mark starting node as visited.
Repeat until queue becomes empty:
Remove node from queue.
Visit the node.
Check all neighbors.
If neighbor is unvisited:
Mark visited.
Add to queue.
Print traversal order.
Conclusion

This program demonstrates Breadth First Search (BFS) traversal step by step using a queue and visited set. BFS visits nodes level by level and avoids revisiting nodes. It is widely used in graph traversal and shortest path problems.
"""