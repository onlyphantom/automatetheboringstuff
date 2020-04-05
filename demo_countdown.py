import time, subprocess, sys

timeLeft = int(sys.argv[1])
while timeLeft > 0:
    print(timeLeft, end='\n')
    time.sleep(1)
    timeLeft -= 1
    
print("Time's Up!")
subprocess.Popen(['open', 'alarm.wav'])