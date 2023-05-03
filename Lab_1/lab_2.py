import random
import matplotlib.pyplot as plt
import numpy as np
import warnings
from scipy.integrate import quad

warnings.filterwarnings("ignore")

def monte_carlo_integration(f, a, b, n):
    count = 0
    x_in = []
    y_in = []
    x_out = []
    y_out = []
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, f(b))
        if y <= f(x):
            count += 1
            x_in.append(x)
            y_in.append(y)
        else:
            x_out.append(x)
            y_out.append(y)
    return (b - a) * f(b) * count / n, x_in, y_in, x_out, y_out

def test_function(x):
    return np.exp(x)

def main_function(x):
    return np.exp(x**2)

def errors(integral):
    exact_value = quad(test_function, a, b)[0]
    abs_error = abs(integral - exact_value)
    rel_error = abs_error / exact_value
    return exact_value, abs_error, rel_error

a = 0
b = 2
n = 3000

integral_test, x_in_test, y_in_test, x_out_test, y_out_test = monte_carlo_integration(test_function, a, b, n)
integral_main, x_in_main, y_in_main, x_out_main, y_out_main = monte_carlo_integration(main_function, a, b, n)


exact_value_test, abs_error_test, rel_error_test = errors(integral_test)

print(f"Тестовий інтеграл: {integral_test}")
print(f"Точне значення: {exact_value_test}")
print(f"Абсолютна похибка: {abs_error_test}")
print(f"Відносна похибка: {rel_error_test*100}")

x = np.linspace(a,b , 100)
y = test_function(x)
plt.plot(x,y,color="black", linewidth=3)
plt.scatter(x_in_test,y_in_test,color='blue', alpha=0.5)
plt.scatter(x_out_test,y_out_test,color='yellow', alpha=0.5)
plt.title("Тестова функція")
plt.show()

exact_value_main = quad(main_function,a,b)[0]
abs_error_main = abs(integral_main - exact_value_main)
rel_error_main = abs_error_main / exact_value_main

print(f"Головнй інтеграл: {integral_main}")
print(f"Точне значення: {exact_value_main}")
print(f"Абсолютна похибка: {abs_error_main}")
print(f"Відносна похибка: {rel_error_main*100}")

x = np.linspace(a,b , 100)
y = main_function(x)
plt.plot(x,y,color="black", linewidth=3)
plt.scatter(x_in_main,y_in_main,color='blue', alpha=0.5)
plt.scatter(x_out_main,y_out_main,color='yellow', alpha=0.5)
plt.title("Головна функція")
plt.show()