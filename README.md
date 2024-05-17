# py-prime
Prime number within 10s

## prime-alpha.py -  original code
- Fixed a bug
- Implement timer: display time completed

```py
for n in range(first_int, final_int + 1):
    start = time.time() 
    time.sleep(.01)  # simulate some work is being done
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print(n)

current = time.time()
elapsed = current - start

print('Time completed: ' , elapsed)
```
- `start.time()` inside `range()` because this is when you start your checks.  There is a logic problem with your old code. Your `start.time()` starts at the very begining of your program, you are not accounting the time user needs to input interval.
- `time.sleep(.01)` on my machine it happens so fast at the end of the program it shows 0.0s.  This is to add a little delay between each number.
- At the very end after the `for()` loop is complete we calculate the time spent.


## primeNum.py - Prime number within 10s

### 1. Function that check for prim numbers
```py
def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
```

### 2. Start time
We start time outside of `is_prime()` because we don't have to worry about time user need to input interval.
```py
start = time.time()
```

### 3. While loop
Constant check timmer if it has reached 10s.  If reached break.  If not continue...
```py
while True:
    current = time.time();
    elapsed = current - start

    if elapsed >= 10:
        break
    if is_prime(n):
        print(n)
    n += 1
```

## Final Thoughts

**prime-alpha.py (original code)**
Not sure what the inputs `frist_int` & `final_int` was in relations to your question "Prime number within 10s".  So I wasn't able to integrated it with primeNum.py.

**primeNum.py**
Something is bugging me about `is_prime()` function.  Could there be ways to make the computer output more numbers? Given limited of time I couldn't explore to much but a few thoughts maybe you could try...

- [ ] How about getting rid of all even numbers?
- [ ] What other method can we reduce number of iterations needed?

-----

Thank you, this was kind of fun, poked my brains a bit!