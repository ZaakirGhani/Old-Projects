import time
import threading

stop_thread = False  # Flag to signal the thread to stop

def timer():
    global stop_thread
    for x in range(3600, 0, -1):
        if stop_thread:  # Check flag to exit loop
            print("\nTimer stopped.")
            return
        time.sleep(1)

    print('\nTIMES UP!')
    
def p():
    global stop_thread
    stopwatch = threading.Thread(target=timer)
    stopwatch.start()
    
    p = input(':: ')  # First input
    l = input(':')  # Second input
    
    stop_thread = True  # Signal the timer thread to stop
    stopwatch.join()  # Wait for thread to finish before exiting
    print("Timer has been stopped. Program ends.")

p()


