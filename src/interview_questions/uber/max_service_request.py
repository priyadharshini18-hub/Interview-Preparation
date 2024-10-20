# Write a code for service request and capacity

# Eg - serverpower =[1,2,1,2,1]
# Events =[request, request, fail 2, request, fail 3, request, request]
# Output - 1 (Server that provided maximum requests)

serverPower =[1, 2, 1, 2, 1]
events = ['REQUEST', 'REQUEST', 'FAIL 2', 'REQUEST', 'FAIL 3', 'REQUEST', 'REQUEST']

serviceCount = [0, 0, 0, 0, 0]
failedServers = [False, False, False, False, False]
count = [0, 0, 0, 0, 0]

for op in events :
    if op == 'REQUEST' :
        for i in range(len(serverPower))  :
            if serverPower[i] > 0 and failedServers[i] == False :
                serverPower[i] -= 1
                serviceCount[i] += 1
                break

    elif op.startswith('FAIL') :
        failure = int(op.split()[1])
        serverPower[failure] = 0
        failedServers[failure] = True

max_requests = max(serviceCount)
most_requested_server = serviceCount.index(max_requests)

print('Server with max service is ', most_requested_server)

# Explanation:
# Event 0: request Goes to server 0
# Request counter =[1,0,0,0,0]
# Server capacity =[0,2,1,2,1]
#
# Event 1: request goes to server 1
# Request counter =[1,1,0,0,0]
# Server capacity =[0,1,1,2,1]
#
# Event 2: fail 2
# Request counter =[1,1,0,0,0]
# Server capacity =[0,1,1,2,1] - index 2 is shut down
#
# Event 3:request goes to 1
# Request counter =[1,2,0,0,0]
# Server capacity =[0,0,1,2,1]
#
# Next request goes to server 3 as server 2 is shut...