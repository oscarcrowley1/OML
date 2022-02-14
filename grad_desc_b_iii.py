import sympy
import matplotlib.pyplot as plt
import numpy as np
#x0, x1 = sympy.symbols("x0, x1", real=True)
x0 = sympy.symbols("x0", real=True)
#x=sympy.Array([x0,x1])
quart_func=x0**4
quart_deriv = sympy.diff(quart_func,x0)
print(quart_func,quart_deriv)


def f(x):
    return quart_func.subs(x0, x)

def df(x):
    return quart_deriv.subs(x0, x)

alpha_range = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]
x_start_range = [0.001, 0.01, 0.1, 1, 10]

for alpha in alpha_range:
    for x_start in x_start_range:
        num_iterations = 1000

        #alpha = 0.1

        current_x = x_start
        #current_x = 1
        current_y = f(current_x)

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
                
            slope = df(current_x)
            step = alpha*slope
            current_x = current_x - step
            current_y = f(current_x)
            
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

        
        plt.plot(y_values, label=f"x_start: {x_start}")
        
    plt.title(f"Change in f(x) (for alpha: {alpha})")
    plt.xlabel("Iterations")
    plt.ylabel("f(x)")
    plt.yscale("log")
    plt.ylim(top=100000)
    plt.legend()
    plt.show()