#Write a Function That Checks if a Number Is Prime or Not
from operator import truediv


def is_prime(num):

    if num < 2:
        return False

    if num == 2:
         return True

    for i in range(2, num+1):
        if num % i == 0:
            return False

        else:
            return True