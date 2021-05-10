import time
n = int(input("Enter the initial countdown time(in seconds): "))
for i in range(n, -1,-1 ):
    print(i, end="\r")
    time.sleep(1)
