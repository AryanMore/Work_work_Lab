def is_safe(processes , available , max_demand, allocated):
    n = len(processes)
    m = len(available)

    need = [[max_demand[i][j] - allocated[i][j] for j in range(m)] for i in range(n)]

    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocated[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    found = True
                    print(f"Process {processes[i]} is executed")
                    break
        if not found:
            print(f"Prcoess {processes[i]} was not executed")
            return False , []
    print("The System is in safe state")
    return True , safe_sequence





processes = [0, 1, 2, 3, 4]  # Process IDs
available = [3, 3, 2]  # Initial available resources
max_demand = [
    [7, 5, 3],  # Max demand of P0
    [3, 2, 2],  # Max demand of P1
    [9, 0, 2],  # Max demand of P2
    [2, 2, 2],  # Max demand of P3
    [4, 3, 3]   # Max demand of P4
]
allocated = [
    [0, 1, 0],  # Resources allocated to P0
    [2, 0, 0],  # Resources allocated to P1
    [3, 0, 2],  # Resources allocated to P2
    [2, 1, 1],  # Resources allocated to P3
    [0, 0, 2]   # Resources allocated to P4
]

# Check if the system is in a safe state
is_it , safe_sequence = is_safe(processes, available, max_demand, allocated)

if(is_it):
    print(f"The proccess is in safe state :  {safe_sequence}")
