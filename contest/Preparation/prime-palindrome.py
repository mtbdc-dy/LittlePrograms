import math

flag_prime = True
n = 17
# for i in range(2, int(math.log(n))+1):
for i in range(2, int(math.sqrt(n))+1):     # Square Root Calculations
    if n % i == 0:
        print('非素数')
        flag_prime = False

if flag_prime:
    print('素数')

if str(n) == str(n)[::-1]:
    print('回文')
else:
    print('不是回文')
