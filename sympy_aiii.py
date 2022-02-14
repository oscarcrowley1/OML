import sympy
import matplotlib.pyplot as plt
import numpy as np
from torch import logspace
#x0, x1 = sympy.symbols("x0, x1", real=True)
x0 = sympy.symbols("x0", real=True)
#x=sympy.Array([x0,x1])
f=x0**4
#f=0.5*(x[0]**2+10*x[1]**2)
dfdx = sympy.diff(f,x0)
print(f,dfdx)

#x_range = [0.01, 0.1, 1, 10, 100, 1000]
half_width = 10
x_range = np.linspace(-half_width, half_width)
#delta = 0.01
#delta_range = [0.001, 0.01, 0.1, 1]
delta_range = np.logspace(-3, 0, num=4)

for delta in delta_range:

    deriv_array = []
    fin_diff_array = []

    for x_test in x_range:
        deriv = dfdx.subs(x0, x_test)
        print(deriv)
        f_x = f.subs(x0, x_test)
        f_x_plusdelta = f.subs(x0, x_test+delta)
        fin_diff = (f_x_plusdelta - f_x) / delta
        print(fin_diff)
        print("\n")
        
        deriv_array.append(deriv)
        fin_diff_array.append(fin_diff)
        
    fin_diff_array = np.array(fin_diff_array)
    deriv_array = np.array(deriv_array)
        
    # plt.plot(x_range, deriv_array, label="Derivative Value")
    # plt.plot(x_range, fin_diff_array, label="Finite Difference Value")
    label_string = "Delta = " + str(delta)
    plt.plot(x_range, deriv_array - fin_diff_array, label=label_string)
#plt.xscale("log")
#plt.yscale("log")
plt.title("Accuracy of Estimated Derivative for Varying Delta")
plt.xlabel("x Value")
plt.ylabel("Difference between Derivative and Finite Difference")
plt.legend()

plt.show()