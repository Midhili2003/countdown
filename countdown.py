import time
n = int(input("For how many seconds do you want to set the timer?"))
while n:
    mins = n//60
    secs = n%60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    n -= 1
    time.sleep(1)
print("Blast off!!")
