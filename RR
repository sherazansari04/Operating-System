#!/usr/bin/python


numberOfProcesses = 5
listOfProcesses = ["p0","p1","p2","p3","p4"]
ArrivalTimes = [0,1,3,1,0]
ExecutionTimes = [5,3,10,6,8]

clock = 0

processPerClock = []

#quantom = input("plz input quantom: ")

quantom = 2



AE = zip(ArrivalTimes,ExecutionTimes)
AE.sort()

ArrivalTimes_sorted = [ArrivalTimes for ArrivalTimes, ExecutionTimes in AE]

ExecutionTimes_sorted = [ExecutionTimes for ArrivalTimes, ExecutionTimes in AE]



Al = zip(copyOfArrivalTimes,listOfProcesses)
Al.sort()
listOfProcesses_sorted = [listOfProcesses for copyOfArrivalTimes, listOfProcesses in Al]


while len(listOfProcesses_sorted) != 0:

	flag = False

	
	for i in range(len(AE)):
		
		for j in range(quantom):
			if ExecutionTimes_sorted[i] > 0:

				ExecutionTimes_sorted[i] = ExecutionTimes_sorted[i] - 1
				processPerClock.append(listOfProcesses_sorted[i])

			else:
				newTmp = i
				flag = True
				break

	if flag == True:
		del ExecutionTimes_sorted[newTmp]
		del AE[newTmp]
		del listOfProcesses_sorted[newTmp]
		del ArrivalTimes_sorted[newTmp]

print "processPerClock: ", processPerClock


turnAroundTimes = []

for i in range(len(copyOfArrivalTimes2)):
	turnAroundTimes.append((len(processPerClock) - processPerClock[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes2[i])

averageTurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes2)

print "average turnAround time: ", averageTurnAroundTime

waitingtimes = []
for i in range(len(copyOfListOfProcesses2)):
	waitingtimes.append(turnAroundTimes[i] - copyOfExecutionTimes[i])

averageWaitingsTime = float(sum(waitingtimes))/len(copyOfArrivalTimes2)

print "average waiting time: ", averageWaitingsTime

responseTimes = []
for i in range(len(copyOfArrivalTimes2)):
	responseTimes.append(waitingtimes[i]-copyOfArrivalTimes2[i])

averageResponseTime = float(sum(responseTimes))/len(copyOfArrivalTimes2)

print "average response time: ", averageResponseTime
