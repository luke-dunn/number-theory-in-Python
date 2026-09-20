# numbers that are equal to the sum of powers
# of their digits, search starts at case 3
# because it can shown that the case of squares
# has no solutions
from tqdm import tqdm

for p in range(3,12):
    for n in range(2,100000000):
        if n == sum(int(digit) ** p for digit in str(n)):
            print(n,p)
## 153 3
## 370 3
## 371 3
## 407 3
## 1634 4
## 8208 4
## 9474 4
## 4150 5
## 4151 5
## 54748 5
## 92727 5
## 93084 5
## 194979 5
## 548834 6
## 1741725 7
## 4210818 7
## 9800817 7
## 9926315 7
## 14459929 7
## 24678050 8
## 24678051 8
## 88593477 8
