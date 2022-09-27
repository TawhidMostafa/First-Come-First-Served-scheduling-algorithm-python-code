class process:
    def __init__(self):
        self.pid = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = 0
n = None
p = [process() for _ in range(100)]
Completion_Time=0
Turn_Around_Time=0
Waiting_time=0
average_waiting_time=0
average_turn_around_time=0
total_turnaround_time=0
total_waiting_time=0
disk={}
print("Enter the number of processes: ",end=' ')
n=int(input())
for i in range(0, n):
    print("Enter arrival time of process ",i+1,' :',end=' ')
    p[i].arrival_time=int(input())
    print("Enter burst time of process ",i+1,' :',end=' ')
    p[i].burst_time=int(input())
    p[i].pid = i+1

for j in range(n):
    if(j==0):
        p[j].completion_time=p[j].burst_time
    else:
        p[j].completion_time =(p[j-1].completion_time+p[j].burst_time)
for i in range(n):
    p[i].turnaround_time=(p[i].completion_time-p[i].arrival_time)
    p[i].waiting_time=(p[i].turnaround_time-p[i].burst_time)
    total_turnaround_time += p[i].turnaround_time
    total_waiting_time += p[i].waiting_time
for i in range(n):
    disk['Process:',int(p[i].pid)]=p[i].waiting_time

average_waiting_time=(total_waiting_time/n)
average_turn_around_time=(total_turnaround_time/n)
print("Precess ID\t","Arrival time\t","Burst time\t","Completion Time\t","Turnaround Time\t","Waiting Time\n")
for i in range(0, n):
    print(p[i].pid,"\t\t\t\t",p[i].arrival_time,"\t\t\t\t",p[i].burst_time,"\t\t\t\t",p[i].completion_time,"\t\t\t\t",
          p[i].turnaround_time,"\t\t\t\t",p[i].waiting_time,"\t\t\t\t\n")

print('Waiting time for each process are :\n',disk,"\n\nThe Average Turn Around Time is :",average_turn_around_time,'\n\nThe Average Waiting Time is :',average_waiting_time)

