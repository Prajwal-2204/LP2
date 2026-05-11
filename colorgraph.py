color_names = {1:"R", 2:"G", 3:"B", 4:"Y"}

def print_colors(colors):
    print("Current Colors:", [color_names[c] if c!=0 else 0 for c in colors])
    print("-" * 25)

def is_safe(graph, colors, node, color):

    for i in range(len(graph)):

        if graph[node][i] == 1 and colors[i] == color:
            return False

    return True

def graph_coloring(graph, m, colors, node):

    if node == len(graph):

        print("\nSolution Found")
        print_colors(colors)

        print("\nVertex Coloring:")

        for i in range(len(colors)):
            print(f"Vertex V{i} -> {color_names[colors[i]]}")

        return True

    for color in range(1, m + 1):

        print(f"Trying Color {color} for Vertex V{node}")

        if is_safe(graph, colors, node, color):

            colors[node] = color

            print(f"Assigned Color {color} to Vertex V{node}")
            print_colors(colors)

            if graph_coloring(graph, m, colors, node + 1):
                return True

            colors[node] = 0

            print(f"Backtracking from Vertex V{node}")
            print_colors(colors)

        else:
            print(f"Color {color} is not safe for Vertex V{node}")

    return False


n = int(input("Enter number of nodes: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

colors = [0] * n

if not graph_coloring(graph, m, colors, 0):
    print("No Solution Found")


"""
Title
Graph Coloring Using Backtracking in Python

Objective
To assign colors to all vertices of a graph so that no two adjacent vertices have the same color using the backtracking technique.

Theory
Graph coloring is a Constraint Satisfaction Problem. In this problem, colors are assigned to the vertices of a graph. The main condition is that two connected vertices should not have the same color. For example, if vertex V0 and vertex V1 are connected, then both vertices must have different colors.
This program uses the backtracking method to solve the graph coloring problem. Backtracking means trying one possible solution, checking whether it is valid, and moving forward if it is correct. If the solution becomes invalid later, the program goes back and tries another option. In this code, the program tries to assign colors to vertices one by one.
The graph is represented using an adjacency matrix. In this matrix, 1 means two vertices are connected, and 0 means they are not connected. The is_safe() function checks whether a selected color can be assigned to a vertex. If any adjacent vertex already has the same color, then that color is not safe.
The graph_coloring() function tries colors for each vertex. If a color is safe, it assigns that color and moves to the next vertex. If no color works for a vertex, it removes the previous color and goes back. This process continues until all vertices are colored correctly or no solution is found.
Important Points


Graph Coloring
Assign colors to graph vertices.
Adjacent vertices must have different colors.


Backtracking

Try one solution.
If correct, move forward.
If wrong, go back and try another color.


Adjacency Matrix
Used to represent graph connections.
1 means edge exists.
0 means no edge.




Color Dictionary


Stores color names:
{1:"R", 2:"G", 3:"B", 4:"Y"}


Safe Condition
A color is safe if no connected vertex has the same color.


Recursive Function
The function calls itself for the next vertex.



Backtracking Step
If color assignment fails, color is reset to 0.


Final Solution
If all vertices get valid colors, solution is printed.



Algorithm
Start the program.
Read the number of vertices.
Input the adjacency matrix.
Read the number of colors.
Initialize all vertex colors as 0.
Start coloring from vertex 0.
For each vertex:
Try each color from 1 to m.
Check whether the color is safe.
If safe, assign the color.
Recursively color the next vertex.
If next coloring fails, remove the color and backtrack.
If all vertices are colored, print the solution.
If no valid coloring is possible, print “No Solution Found”.
End the program.


Conclusion
This program solves the graph coloring problem using backtracking. It checks each color for every vertex and ensures that adjacent vertices do not have the same color. The program clearly shows how colors are assigned and how backtracking happens when a wrong choice is made."""