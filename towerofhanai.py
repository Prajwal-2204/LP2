def print_towers(towers):
    print("\nCurrent Towers State:")
    for tower in towers:
        print(f"{tower} = {towers[tower]}")
    print("-" * 40)
def move_disk(source, destination, towers):
    disk = towers[source].pop()
    towers[destination].append(disk)
    print(f"\nMove Disk {disk} from Tower {source} ---> Tower {destination}")
    print_towers(towers)
def tower_of_hanoi(n, source, auxiliary, destination, towers):
    if n == 1:
        move_disk(source, destination, towers)
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary, towers)
    move_disk(source, destination, towers)
    tower_of_hanoi(n - 1, auxiliary, source, destination, towers)
n = int(input("Enter number of disks: "))
num_towers = 3
print(f"\nNumber of Towers Required = {num_towers}")
weights = []
print("\nEnter random disk weights:")
for i in range(n):
    weight = int(input(f"Enter weight of disk {i+1}: "))
    weights.append(weight)
weights.sort(reverse=True)
print("\nDisks arranged from biggest to smallest:")
print(weights)
towers = {
    'A': weights.copy(),  
    'B': [],               
    'C': []                
}
print("\nInitial Towers Arrangement")
print_towers(towers)
print("\n========== STEPS ==========")
tower_of_hanoi(n, 'A', 'B', 'C', towers)
print("\n========== FINAL STATE ==========")
print_towers(towers)

"""Title
Tower of Hanoi Using Recursion in Python
Objective
To move all disks from the source tower to the destination tower using an auxiliary tower by following Tower of Hanoi rules.

Theory
Tower of Hanoi is a famous mathematical puzzle. It contains three towers and some disks of different sizes. The goal is to move all disks from the source tower to the destination tower using the auxiliary tower.
In this program, the user enters random disk weights. These weights are sorted in descending order so that bigger disks are placed at the bottom and smaller disks are placed at the top.
The Tower of Hanoi problem follows these rules:

Only one disk can be moved at a time.

Only the top disk of a tower can be moved.

A bigger disk should not be placed on a smaller disk.

This program uses recursion to solve the problem. Recursion means a function calls itself to solve smaller parts of the same problem. To move n disks, the program first moves n-1 disks from source to auxiliary tower, then moves the largest disk from source to destination, and finally moves n-1 disks from auxiliary to destination.
The print_towers() function shows the current state of all towers. The move_disk() function moves one disk from one tower to another. The tower_of_hanoi() function performs the recursive logic.
Important Points

Tower of Hanoi
A puzzle with three towers and multiple disks.


Three Towers
Source tower: starting tower.
Auxiliary tower: helper tower.
Destination tower: final tower.

Disk Movement
Only one disk moves at a time.

Recursion
Function calls itself to solve smaller disk problems.


Base Case
If only one disk is present, move it directly.

Recursive Case
Move n-1 disks first.

Move largest disk.
Move n-1 disks again.
Sorting Weights
Disk weights are sorted from biggest to smallest.

Tower Dictionary
Towers are stored using dictionary keys A, B, and C.

Step Display
Program prints every disk movement.


Algorithm
Start the program.
Read number of disks.
Read disk weights from user.
Sort disk weights in descending order.
Store all disks in tower A.
Keep tower B and tower C empty.
Display initial tower arrangement.
Call tower_of_hanoi(n, A, B, C).
If n == 1, move disk directly from source to destination.
Otherwise:
Move n-1 disks from source to auxiliary.
Move largest disk from source to destination
Move n-1 disks from auxiliary to destination.
Display final tower state.
End the program.


Conclusion
This program solves the Tower of Hanoi problem using recursion. It moves disks from tower A to tower C with the help of tower B. The program clearly displays every movement and helps understand how recursion works step by step."""