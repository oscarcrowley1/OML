import sympy
import matplotlib.pyplot as plt
import numpy as np
#x0, x1 = sympy.symbols("x0, x1", real=True)
x0 = sympy.symbols("x0", real=True)
#x=sympy.Array([x0,x1])
f=x0**4
#f=0.5*(x[0]**2+10*x[1]**2)
dfdx = sympy.diff(f,x0)
print(f,dfdx)

#x_range = [0.01, 0.1, 1, 10, 100, 1000]
half_width = 0.1
x_range = np.linspace(-half_width, half_width)
delta = 0.01

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
    
plt.plot(x_range, deriv_array, label="Derivative Value")
plt.plot(x_range, fin_diff_array, label="Finite Difference Value")
#plt.plot(x_range, deriv_array - fin_diff_array)
#plt.xscale("log")
#plt.yscale("log")
plt.title("Comparing Derivative and Finite Difference at delta=0.01")
plt.xlabel("x Value")
plt.ylabel("Slope of f(x)")
plt.legend()

plt.show()