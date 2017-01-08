class Queue():

    def __init__(self, quantum, priority):
        self.items = []
        self.quantum = quantum
        self.priority = priority

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        item.Qtime = self.quantum
        item.priority = self.priority
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

Main

queues = [ Queue(i*10, i) for i in range(256)]
# pendingProcs: [(pid, QIndex)]
pendingProcs = []
currProc = None

def schedule():
    global currProc
   
        index = currProc.priority

        Q = queues[index]

        p = currProc
        # if p is blocking for I/O
        if p.blocking == 1:
            # save process state to PCB
            # TODO
            Q.dequeue()

            # if p is at the top level
            if index == 0:
                Q.enqueue(p)

            
            else:
                queues[index-1].enqueue(p)

       
        elif p.leave == 1:
            # save process state to PCB
            # TODO
            Q.dequeue()

            pendingProcs.append({"pid" : p.PID, "Qindex" : index})

        
        else:
           
            p.Qtime =-1
          
            p.time -=1
        
            if p.Qtime <= 0:
               

                Q.dequeue()
               
                if p.time > 0:
                   
                    queues[index + 1].enqueue(p)
         
                else:
                    # TODO: destroy p
                    pass

          
            elseif p.time <= 0:
                Q.dequeue()
                # TODO: destroy p

           
            else:
                pass

    
    for Q in enumerate(queues):
        # empty queues are disregarded
        if not Q.isEmpty():
              p = Q.peek()
            currProc = p
           break

def addToQueue(process):
   
  if (entry = filter(lambda pp: pp["pid"] == process, pendingProcs)) is not None:
         queues[entry["Qindex"]].enqueue(process)
    else:
          queues[0].enqueue(process)

