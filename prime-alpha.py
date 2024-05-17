#import time library
import time

# variables
start = time.time() # start timer

# wait a few seconds

current = time.time() # get time again
elapsed = round(float(current - start), 6)  # measure elapsed time  

first_int = int(input("Enter first interval: "))
final_int = int(input("Enter final interval: "))


# for n in range(first_int, final_int + 1):
#     if n > 1:
#         for x in range(2, n):
#             if n % x == 0:
#                 break
#             else:    <----- Incorrect indentation: This causes incorrect multiple prints of n
#                 print(n)
# Results:
# Enter first interval: 1
# Enter final interval: 10
# 3
# 5
# 5
# 5
# 7
# 7
# 7
# 7
# 7
# 9

for n in range(first_int, final_int + 1):
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print(n)

# Result:
# Enter first interval: 1
# Enter final interval: 10
# 2
# 3
# 5
# 7