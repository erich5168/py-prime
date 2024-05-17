# py-prime
Prime number within 10s

## prime-alpha.py -  original code
Did not change anything only fixed a bug. 


## primeNum.py - Prime number withint 10s

### 1. Function that check for prim numbers
```py
def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
```

### 2. Start time
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
Not sure what the inputs `frist_int` & `final_int` was for related to your question "Prime number within 10s".  So I wasn't able to integrated it with primeNum.py.

**primeNum.py**
Something is bugging me about `is_prime()` function.  Could there be ways to make the computer output more numbers? Given limited of time I couldn't explore to much but a few thoughts maybe you could try...

- [ ] How about getting rid of all even numbers?
- [ ] What other method can we reduce number of iterations needed?

-----

Thank you, this was kind of fun, poked my brains a bit!