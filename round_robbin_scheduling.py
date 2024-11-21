def round_robin(processes, burst_time, arrival_time, time_quantum):
    n = len(processes)

    remaining_time = burst_time.copy()
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    time = 0
    queue = []
    visited = [False] * n
    completed = 0

    for i in range(n):
        if arrival_time[i] == 0:
            queue.append(i)
            visited[i] = True

    while completed != n:
        if queue:
            current = queue.pop(0)
            if remaining_time[current] <= time_quantum:
                time += remaining_time[current]
                remaining_time[current] = 0
                completion_time[current] = time
                turnaround_time[current] = completion_time[current] - arrival_time[current]
                waiting_time[current] = turnaround_time[current] - burst_time[current]
                completed += 1
                print('OSI')

            else:
                time += time_quantum
                remaining_time[current] -= time_quantum
            
            for i in range(n):
                if arrival_time[i] <= time and not visited[i]:
                    queue.append(i)
                    visited[i] = True
            
            if remaining_time[current] > 0:
                queue.append(current)

        else:
            time+= 1
            for i in range(n):
                if arrival_time[i] <= time and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    print(f"{'Process':<10}{'Burst Time':<12}{'Arrival Time':<14}{'Completion Time':<18}{'TAT':<8}{'WT':<8}")
    for i in range(n):
        print(f"{processes[i]:<10}{burst_time[i]:<12}{arrival_time[i]:<14}{completion_time[i]:<18}{turnaround_time[i]:<8}{waiting_time[i]:<8}")


processes = [1, 2, 3, 4]  # Process IDs
burst_time = [5, 15, 6, 8]  # Burst time for each process
arrival_time = [0, 1, 2, 3]  # Arrival time for each process
time_quantum = 4  # Time quantum

print("Round Robin Scheduling")
round_robin(processes, burst_time, arrival_time, time_quantum)