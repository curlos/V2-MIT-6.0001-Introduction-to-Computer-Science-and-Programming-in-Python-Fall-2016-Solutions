import math

x = int(input("Enter a number 'x': "))
y = int(input("Enter a number 'y': "))
x_pow_y = x**y
log_x = math.floor(math.log(x, 2))

print(f'"x" to the power of "y" = {x_pow_y}')
print(f"Log of X is: {log_x}")
