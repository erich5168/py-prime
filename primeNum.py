#import time library
import time

# Function to check if a number is prime
def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

start = time.time()
print(start)