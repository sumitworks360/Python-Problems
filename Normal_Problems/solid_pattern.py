def solid_square_pattern(n):
    return ("* " * n + "\n") * n

# Example usage:
n = int(input("Enter the size of the square pattern: "))
result = solid_square_pattern(n)
print(result)
