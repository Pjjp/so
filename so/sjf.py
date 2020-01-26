
from tabulate import tabulate

class SJF:

    def __init__(self, processes, n):
        self.processes = processes
        self.n = n


    def findWaitingTime(self, wt): 
        rt = [0] * self.n 

        for i in range(self.n): 
            rt[i] = self.processes[i][1] 
        complete = 0
        t = 0
        minm = 999999999
        short = 0
        check = False

        while (complete != self.n): 
            
            for j in range(self.n): 
                if ((self.processes[j][2] <= t) and
                    (rt[j] < minm) and rt[j] > 0): 
                    minm = rt[j] 
                    short = j 
                    check = True
            if (check == False): 
                t += 1
                continue
                
            rt[short] -= 1

            minm = rt[short] 
            if (minm == 0): 
                minm = 999999999

            if (rt[short] == 0): 

                complete += 1
                check = False
                fint = t + 1
                wt[short] = (fint - self.processes[short][1] -	
                                    self.processes[short][2]) 
                if (wt[short] < 0): 
                    wt[short] = 0
            t += 1


    def findTurnAroundTime(self, wt, tat): 
        
        for i in range(self.n): 
            tat[i] = self.processes[i][1] + wt[i]


    def getStats(self): 
        wt = [0] * self.n 
        tat = [0] * self.n 

        self.findWaitingTime(wt) 
        self.findTurnAroundTime(wt, tat) 

        total_wt = 0
        total_tat = 0
    
        rows = []
        for i in range(self.n): 
            rows.append([str(self.processes[i][0]), str(self.processes[i][1]), str(wt[i]), str(tat[i])])
            total_wt += wt[i]
        print(tabulate(rows, headers=['id', 'start_time', 'burst_time', 'reverse_time'])) 

        print("\nAverage waiting time = %.5f "%(total_wt / self.n)) 
