import random
import math

#Method to compute the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# ------ Methods to compute PI ------
# Approximate PI by the Monte-Carlo's method
# The method consists to take a square of 1 by 1 dimension,
# then, place random points with both x and y coordinates
# between 0 and 1. Finally, check if x² + y² < 1, it represents
# the place of the generated point (inside a 1 radius circle)
# Compute the ration of point inside the circle and then
# multiply it by 4 (the square if a quarter of the circle)
# then, you got an approximation of PI
def monteCarloMethod(iteration):
    number = 0
    iteration = 100000
    for i in range(0, iteration):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1:
            number = number + 1
    return number * 4 / iteration

# Approximate PI by the Ramanujan's method
# The method uses an equation found by Ramanujan and needs
# less iteration than Monte-Carlo to get a better result.
def ramanujanMethod(iteration):
    sum = 0
    for i in range(0, iteration):
        sum = sum +((factorial(4 * i) / (factorial(i))**4 ) * ((26390 * i + 1103) / 396**(4 * i)))
    return 1 / (sum * math.sqrt(8)/9801)

print("Approximation de Pi par Monte-Carlo : "+str(monteCarloMethod(1000000)))
print("Approximation de Pi par Ramanujan : "+str(ramanujanMethod(10)))
