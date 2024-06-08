import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4 / (1 + x**2)

def simpson_13_integration(func, a, b, n=100):
    # n harus genap
    if n % 2 != 0:
        raise ValueError("n harus genap")

    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    integral = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))
    return integral

# Batas integral
a = 0
b = 1

# Hitung nilai integral menggunakan metode Integrasi Simpson 1/3
integral_value = simpson_13_integration(f, a, b)

# Plot fungsi f(x) dan area di bawah kurva
x_values = np.linspace(a, b, 100)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'r', label='f(x) = 4 / (1 + x^2)')
plt.fill_between(x_values, y_values, color='lightblue', alpha=0.5)
plt.title('Integrasi Simpson 1/3 untuk f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print(f"Nilai integral menggunakan metode Simpson 1/3: {integral_value}")
