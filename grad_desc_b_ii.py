import sympy
import matplotlib.pyplot as plt
import numpy as np
#x0, x1 = sympy.symbols("x0, x1", real=True)
x0 = sympy.symbols("x0", real=True)
#x=sympy.Array([x0,x1])
quart_func=x0**4
quart_deriv = sympy.diff(quart_func,x0)
print(quart_func,quart_deriv)

alpha = 0.1

def f(x):
    return quart_func.subs(x0, x)

def df(x):
    return quart_deriv.subs(x0, x)

def calc_step(slope):
    return alpha*slope

num_iterations = 100

current_x = 1
current_y = f(current_x)

x_guesses = []
y_values = []

for iteration in range(num_iterations):
    x_guesses.append(current_x)
    y_values.append(current_y)
    
    print(current_x)
    print(current_y)
    print("\n")
    
    prev_x = current_x
        
    slope = df(current_x)
    step = alpha*slope
    current_x = current_x - step
    current_y = f(current_x)
    
plt.title("x and f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x_guesses, y_values)
plt.show()

plt.title("Change in x")
plt.xlabel("Iterations")
plt.ylabel("x")
plt.plot(x_guesses)
plt.show()

plt.title("Change in f(x)")
plt.xlabel("Iterations")
plt.ylabel("f(x)")
plt.plot(y_values)
plt.show()