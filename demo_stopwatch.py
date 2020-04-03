import time

print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit.")
input()
print("Started.")
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap {lapNum}: {lapTime} \t (Total {totalTime} seconds)')
        lapTime += 1
        lastTime = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying
    print('\nDone.')    