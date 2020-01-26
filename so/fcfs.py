
from tabulate import tabulate

class FCFS:

    def __init__(self, processes, n, burst_time):
        self.processes = processes
        self.n = n
        self.burst_time = burst_time


    def getWtTime(self, wt): 
        wt[0] = 0
        for i in range(1, self.n ): 
            wt[i] = self.burst_time[i - 1] + wt[i - 1]  

            
    def getReverseTime(self, wt, tat): 
        for i in range(self.n): 
            tat[i] = self.burst_time[i] + wt[i] 

    
    def getStats(self): 
    
        wt = [0] * self.n 
        tat = [0] * self.n  
        total_wt = 0
    
        self.getWtTime(wt) 
        self.getReverseTime(wt, tat) 

        rows = []
        for i in range(self.n): 
            rows.append([str(i + 1), str(self.burst_time[i]), str(wt[i]), str(tat[i])])
            total_wt += wt[i]

        print(tabulate(rows, headers=['id', 'start_time', 'burst_time', 
            'reverse_time'])) 
    
        print("Average waiting time = " + str(total_wt / self.n)) 
