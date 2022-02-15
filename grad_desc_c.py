import sympy
import matplotlib.pyplot as plt
import numpy as np
from torch import linspace
#x0, x1 = sympy.symbols("x0, x1", real=True)


#gamma = 1


x0, g = sympy.symbols("x0, g", real=True)
#x=sympy.Array([x0,x1])
#gamma_func=g*(x0**2)
gamma_func=g*abs(x0)
gamma_deriv = sympy.diff(gamma_func,x0)
print(gamma_func,gamma_deriv)


def f(x, gam):
    return gamma_func.subs([(x0, x), (g, gam)])

def df(x, gam):
    return gamma_deriv.subs([(x0, x), (g, gam)])

gamma_range = [0.001, 0.01, 0.1, 1, 10, 100]
#gamma_range = linspace(-10, 10, 10)
x_start_range = [0.01, 0.1, 1, 10, 100]

#for alpha in alpha_range:
for gamma in gamma_range:
    for x_start in x_start_range:
        num_iterations = 1000

        alpha = 0.1

        current_x = x_start
        #current_x = 1
        current_y = f(current_x, gamma)
        print(current_y)

        x_guesses = []
        y_values = []

        for iteration in range(num_iterations):
            
            if current_y > 10000000:
                break
            
            x_guesses.append(current_x)
            y_values.append(current_y)
            
            print(current_x)
            print(current_y)
            print("\n")
            
            prev_x = current_x
                
            slope = df(current_x, gamma)
            step = alpha*slope
            current_x = current_x - step
            current_y = f(current_x, gamma)
            
        # plt.title("x and f(x)")
        # plt.xlabel("x")
        # plt.ylabel("f(x)")
        # plt.plot(x_guesses, y_values)
        # #plt.show()

        # plt.title("Change in x")
        # plt.xlabel("Iterations")
        # plt.ylabel("x")
        # plt.plot(x_guesses)
        # #plt.show()

        
        plt.plot(y_values, label=f"Current x_start {x_start}")
        
    plt.title(f"Change in f(x) (at gamma={gamma})")
    plt.xlabel("Iterations")
    plt.ylabel("f(x)")
    #plt.yscale("log")
    #plt.ylim(top=100000)
    plt.legend()
    plt.show()