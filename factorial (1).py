# Optimized factorial calculation using iteration
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial of 5: {factorial(5)}")