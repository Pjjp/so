
from tabulate import tabulate

class RR:

    def __init__(self, processes, n, bt, quantum):
        self.processes = processes
        self.n = n
        self.bt = bt
        self.quantum = quantum


    def findWaitingTime(self, wt):  
        rem_bt = [0] * self.n 
    
        for i in range(self.n):  
            rem_bt[i] = self.bt[i] 
        t = 0  
    
        while(1): 
            done = True
    
            for i in range(self.n): 
                
                if (rem_bt[i] > 0) : 
                    done = False

                    if (rem_bt[i] > self.quantum):
                        t += self.quantum
                        rem_bt[i] -= self.quantum
                    else: 
                        t = t + rem_bt[i]  
                        wt[i] = t - self.bt[i]  
                        rem_bt[i] = 0
                    
            if (done == True): 
                break
                
    def findTurnAroundTime(self, wt, tat): 
        
        for i in range(self.n): 
            tat[i] = self.bt[i] + wt[i]  
    
    def getStats(self):  
        wt = [0] * self.n 
        tat = [0] * self.n  
        self.findWaitingTime(wt)  
        self.findTurnAroundTime(wt, tat)  
    
        total_wt = 0
        total_tat = 0

        rows = []
        for i in range(self.n): 
            rows.append([str(i + 1), str(self.bt[i]), str(wt[i]), str(tat[i])])
            total_wt += wt[i]
        print(tabulate(rows, headers=['id', 'start_time', 'burst_time', 'reverse_time'])) 
    
        print("\nAverage waiting time = %.5f "%(total_wt / self.n) )
    