from sympy import gcd

def phi(n):
    p=0
    for z in range(1,n):
        if gcd (z,n) == 1:
            p+=1
    return p
print('--- n --|-- phi(n)---')
print('---------------------')
for number in range(1,40):
    print(number,'\t|\t', phi(number))



##Euler's Totient Function, denoted as ϕ(n), is a fundamental concept
##in number theory that counts the number of positive integers up to n
##that are coprime with n. 
##Two numbers are coprime if their greatest common divisor (GCD) is 1.
##
##
##For a positive integer n, ϕ(n) is the number of integers
##k (where 1 ≤ k ≤ n) such that GCD(k, n) = 1
##
##Example: If n=6, the integers 1, 2, 3, 4, 5, 6 are less than or equal
##to 6. The ones that are coprime with 6 are 1 and 5
##(because GCD(1,6) = 1 and GCD(5,6) = 1). Therefore, ϕ(6) = 2
##If n is a prime number, then ϕ(n) = n−1, because a prime number
##is only divisible by 1 and itself, so all numbers less than n are
##coprime with n.
##
##If n is the product of two distinct primes, say n = p × q, then
##ϕ(n) = (p − 1) × (q − 1)


