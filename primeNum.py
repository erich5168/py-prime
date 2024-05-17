#import time library
import time

# Function to check if a number is prime
def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

# N has to start with 2.  2 is the only even prim number
n = 2 

# Start time
start = time.time()

# While loop through time

while True:
    current = time.time();
    elapsed = current - start

    if elapsed >= 10:
        break
    if is_prime(n):
        print(n)
    n += 1
    
print("10 seconds is up.")