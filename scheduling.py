def first_come_first_serve(processes, burst_time , arrival_time):
    n = len(processes)

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    completion_time[0] = burst_time[0] + arrival_time[0]
    for i in range(1, n):
        completion_time[i] = max(completion_time[i-1], arrival_time[i]) + burst_time[i]
    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    print(f"{'Process':<10}{'Burst Time':<12}{'Arrival Time':<14}{'Completion Time':<18}{'TAT':<8}{'WT':<8}")
    for i in range(n):
        print(f"{processes[i]:<10}{burst_time[i]:<12}{arrival_time[i]:<14}{completion_time[i]:<18}{turnaround_time[i]:<8}{waiting_time[i]:<8}")

def shortest_job_first_NP(processes, burst_time, arrival_time):
    n = len(processes)
    completition_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    is_completed = [False] * n
    time = 0
    completed = 0
    print(f"{'Process':<10}{'Burst Time':<12}{'Arrival Time':<14}{'Completion Time':<18}{'TAT':<8}{'WT':<8}")

    while completed != n:
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if(arrival_time[i] <= time and not is_completed[i] and burst_time[i] < min_burst):
                min_burst = burst_time[i]
                idx = i
        
        if idx == -1:
            time += 1
            continue

        time += burst_time[idx]
        completition_time[idx] = time
        turnaround_time[idx] = completition_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        is_completed[idx] = True
        completed += 1
        print(f"{processes[idx]:<10}{burst_time[idx]:<12}{arrival_time[idx]:<14}{completition_time[idx]:<18}{turnaround_time[idx]:<8}{waiting_time[idx]:<8}")


def shortest_job_first_P(processes, burst_time, arrival_time):
    n = len(processes)
    remaining_time = burst_time.copy()
    completition_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    time = 0
    completed = 0
    min_burst = float('inf')
    shortest = None
    check = False

    while completed < n:
        for i in range(n):
            if arrival_time[i] <= time and remaining_time[i] > 0 and remaining_time[i] < min_burst:
                shortest = i
                check = True
                min_burst = remaining_time[i]
            
        if not check:
            time += 1
            continue

        remaining_time[shortest] -= 1
        min_burst = remaining_time[shortest]
        if min_burst == 0:
            min_burst = float('inf')
        
        if remaining_time[shortest] == 0:
            completed += 1
            check = False
            completition_time[shortest] = time + 1
            turnaround_time[shortest] = completition_time[shortest] - arrival_time[shortest]
            waiting_time[shortest] = turnaround_time[shortest] - burst_time[shortest]

        time += 1
    
    print(f"{'Process':<10}{'Burst Time':<12}{'Arrival Time':<14}{'Completion Time':<18}{'TAT':<8}{'WT':<8}")
    for i in range(n):
        print(f"{processes[i]:<10}{burst_time[i]:<12}{arrival_time[i]:<14}{completition_time[i]:<18}{turnaround_time[i]:<8}{waiting_time[i]:<8}")

    

processes = [1, 2, 3, 4]  # Process IDs
burst_time = [6, 8, 7, 3]  # Burst time for each process
arrival_time = [0, 1, 2, 3]  # Arrival time for each process


print("\nPreemptive Shortest Job First Scheduling")
shortest_job_first_NP(processes, burst_time, arrival_time)

# Calculate FCFS Scheduling
#first_come_first_serve(processes, burst_time, arrival_time)