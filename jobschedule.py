def job_scheduling(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [False] * max_deadline
    result = ["-"] * max_deadline

    total_profit = 0

    for job in jobs:

        job_id = job[0]
        deadline = job[1]
        profit = job[2]

        # Find free slot before deadline
        for j in range(deadline - 1, -1, -1):

            if slots[j] == False:

                slots[j] = True
                result[j] = job_id
                total_profit += profit
                break

    print("\nSelected Jobs:")
    for i in result:
        print(i, end=" ")

    print("\nTotal Profit =", total_profit)


# Main Program

n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):

    print("\nEnter details for Job", i + 1)

    job_id = input("Enter Job ID: ")
    deadline = int(input("Enter Deadline: "))
    profit = int(input("Enter Profit: "))

    jobs.append([job_id, deadline, profit])

job_scheduling(jobs)


"""Title
Job Scheduling Problem Using Greedy Method in Python

Objective
To schedule jobs in such a way that maximum profit is earned while completing jobs before their deadlines.

Theory
The Job Scheduling Problem is an optimization problem in which multiple jobs are given with deadlines and profits. The objective is to perform jobs in an order that gives maximum total profit. Each job takes one unit of time, and a job must be completed before or on its deadline.
This program uses the Greedy Method to solve the job scheduling problem. A greedy algorithm always chooses the best possible option at the current step. In this case, the program first selects jobs with higher profit because they contribute more to the total profit.
The jobs are stored in a list where:


job_id represents the job name,

deadline represents the last time slot before which the job must be completed,
profit represents the earning from that job.

The program first sorts all jobs in descending order of profit using:
jobs.sort(key=lambda x: x[2], reverse=True)
This ensures that high-profit jobs are considered first.
After sorting, the program finds the maximum deadline to determine how many slots are available. A slots[] array is used to check whether a time slot is occupied or free. Another array called result[] stores the scheduled jobs.
For each job, the algorithm checks slots from the job’s deadline backward to find a free slot. If a free slot is available, the job is scheduled there and its profit is added to the total profit. If no slot is available, the job is skipped.
This method helps in maximizing total profit while satisfying job deadlines.
Important Points

Job Scheduling
Schedule jobs before deadlines.
Goal is maximum profit.

Greedy Algorithm
Selects highest-profit job first.

Sorting
Jobs are sorted in decreasing order of profit.

Deadline
Each job must finish before its deadline.

Slots Array
Checks whether a time slot is free or occupied.


Result Array
Stores selected jobs.

Profit Calculation
Profit is added only when a job is scheduled successfully.

Backward Checking
Program checks slots from deadline to beginning.


Optimization Problem
Finds best scheduling solution

Applications
CPU scheduling
Task management
Project scheduling

Algorithm
Start the program.
Read number of jobs.
Input job ID, deadline, and profit for each job.
Store all jobs in a list.
Sort jobs according to profit in descending order.
Find maximum deadline.
Create slots array initialized as False.
Create result array initialized as "-".
For each job:
Check free slot before deadline.
If free slot found:
Assign job to slot.
Mark slot as occupied.
Add profit to total profit.
Print selected jobs.
Print total profit.
End the program.


Conclusion
This program solves the Job Scheduling Problem using the greedy approach. It schedules jobs based on maximum profit while satisfying deadlines. The algorithm efficiently selects the best jobs and maximizes total profit using sorting and slot allocation techniques."""