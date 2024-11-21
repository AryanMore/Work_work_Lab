def priority_scheduling_P(processes, burst_time, arrival_time, priority):
    n = len(processes)
    remaining_time = burst_time.copy()

    completed = 0
    time = 0
    is_completed = [False] * n
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    check = False
    
    while completed != n:
        prior = None
        min_priority = float('inf')
        for i in range(n):
            if arrival_time[i] <= time and not is_completed[i] and min_priority > priority[i]:
                prior = i
                min_priority = priority[i]
                check = True

        if not check:
            time += 1
            continue
        
        remaining_time[prior] -= 1
        time += 1

        if remaining_time[prior] == 0:
            check = False
            completed += 1
            is_completed[prior] = True
            completion_time[prior] = time
            turnaround_time[prior] = completion_time[prior] - arrival_time[prior]
            waiting_time[prior] = turnaround_time[prior] - burst_time[prior]
        
    print(f"{'Process':<10}{'Burst Time':<12}{'Arrival Time':<14}{'Priority':<10}{'Completion Time':<18}{'TAT':<8}{'WT':<8}")
    for i in range(n):
        print(f"{processes[i]:<10}{burst_time[i]:<12}{arrival_time[i]:<14}{priority[i]:<10}{completion_time[i]:<18}{turnaround_time[i]:<8}{waiting_time[i]:<8}")


def priority_scheduling_NP(processes , burst_time, arrival_time, priority):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    is_completed = [False] * n

    time = 0
    completed = 0

    while completed != n:
        prior = -1
        min_priority = float('inf')
        for i in range(n):
            if arrival_time[i] <= time and not is_completed[i] and min_priority > priority[i]:
                min_priority = priority[i]
                prior = i
            
        if prior == -1:
                time += 1
                continue

        time += burst_time[prior]
        completion_time[prior] = time
        turnaround_time[prior] = completion_time[prior] - arrival_time[prior]
        waiting_time[prior] = turnaround_time[prior] - burst_time[prior]
        is_completed[prior] = True
        completed += 1

    print(f"{'Process':<10}{'Burst Time':<12}{'Arrival Time':<14}{'Priority':<10}{'Completion Time':<18}{'TAT':<8}{'WT':<8}")
    for i in range(n):
        print(f"{processes[i]:<10}{burst_time[i]:<12}{arrival_time[i]:<14}{priority[i]:<10}{completion_time[i]:<18}{turnaround_time[i]:<8}{waiting_time[i]:<8}")


processes = [1, 2, 3, 4]  # Process IDs
burst_time = [8, 4, 9, 5]  # Burst time for each process
arrival_time = [0, 1, 2, 3]  # Arrival time for each process
priority = [2, 1, 4, 3]  # Priority (lower number = higher priority)

print("Preemptive Priority Scheduling")
priority_scheduling_NP(processes, burst_time, arrival_time, priority)
        
        


        