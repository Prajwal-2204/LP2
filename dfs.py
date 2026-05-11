from collections import deque

def dfs(graph, node, visited=None, order=None, stack=None, step=None):
    if visited is None:
        visited = set()
        order = []
        stack = []
        step = [0]

    step[0] += 1
    stack.append(node)
    visited.add(node)
    order.append(node)

    print(f"Step {step[0]}: VISIT    node = {node}")
    print(f"         Stack   : {stack}")
    print(f"         Visited : {sorted(visited)}")
    print(f"         Order   : {order}")
    print()

    for neighbor in graph[node]:

        if neighbor not in visited:

            step[0] += 1

            print(f"Step {step[0]}: RECURSE  {node} → {neighbor} (unvisited, going deeper)")
            print(f"         Stack   : {stack}")
            print(f"         Visited : {sorted(visited)}")
            print(f"         Order   : {order}")
            print()

            dfs(graph, neighbor, visited, order, stack, step)

        else:

            step[0] += 1

            print(f"Step {step[0]}: SKIP     {node} → {neighbor} (already visited)")
            print(f"         Stack   : {stack}")
            print(f"         Visited : {sorted(visited)}")
            print(f"         Order   : {order}")
            print()

    stack.pop()

    step[0] += 1

    print(f"Step {step[0]}: RETURN   from {node} → back to {stack[-1] if stack else 'None (done)'}")
    print(f"         Stack   : {stack}")
    print(f"         Visited : {sorted(visited)}")
    print(f"         Order   : {order}")
    print()

    return order



graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):

    node = input(f"\nEnter node {i+1}: ")

    neighbors = input(
        f"Enter neighbors of {node} separated by space: "
    ).split()

    graph[node] = neighbors


start_node = input("\nEnter starting node for DFS: ")


print("\n" + "=" * 50)
print("DFS TRAVERSAL — STEP BY STEP")
print("=" * 50)
print()

result = dfs(graph, start_node)

print("=" * 50)
print(f"FINAL DFS ORDER: {result}")
print("=" * 50)


"""
Title
Depth First Search (DFS) Traversal in Python

Objective
To implement Depth First Search traversal on a graph and display each step of visiting, recursion, skipping, and returning.

Theory
Depth First Search, also called DFS, is a graph traversal technique used to visit nodes of a graph. In DFS, the traversal starts from a selected node and goes as deep as possible along one path before coming back and trying another path.
This program uses recursion to perform DFS. Recursion means a function calls itself again and again until a stopping condition is reached. When DFS visits a node, it marks that node as visited and then checks its neighbors. If a neighbor is not visited, DFS moves deeper to that neighbor. If all neighbors are visited or no more nodes are available, the function returns back to the previous node.
The program also uses a stack concept. In recursive DFS, the function call itself works like a stack. Here, a list named stack is used to show which nodes are currently active in the DFS path. When a node is visited, it is added to the stack. When DFS finishes exploring that node, it is removed from the stack.
A visited set is used to store already visited nodes. This prevents visiting the same node again and avoids infinite loops in cyclic graphs. The order list stores the final DFS traversal order.
Important Points


DFS
DFS means Depth First Search.
It visits nodes by going deep first.

Graph
A graph contains nodes and edges.
Nodes are entered by the user.


Recursion
DFS function calls itself for unvisited neighbors.
This helps in going deeper into the graph.


Stack

Stack stores the current DFS path.
Node is added when visited.
Node is removed when DFS returns.


Visited Set
Stores already visited nodes.
Prevents repeated visits.


Order List
Stores final DFS traversal sequence.

Skip Condition
If a neighbor is already visited, DFS skips it.


Return Step
When all neighbors are checked, DFS returns to the previous node.

Step Counter
step[0] is used to count and display every action.


Algorithm

Start the program.
Create an empty graph dictionary.
Read number of nodes from the user.
Read each node and its neighbors.
Read the starting node for DFS.
Call the dfs() function.
Inside DFS:
Mark the current node as visited.
Add it to stack.
Add it to traversal order.
Check all neighbors of the current node.
If neighbor is not visited:
Recursively call DFS for that neighbor.
If neighbor is already visited:
Skip that neighbor.
After checking all neighbors:
Remove current node from stack.
Return to previous node.
Print final DFS order.
End the program.


Conclusion
This program demonstrates Depth First Search traversal using recursion. It shows how DFS visits nodes, moves deeper into the graph, skips already visited nodes, and returns back after completing each path. The step-by-step output makes the working of DFS easy to understand."""