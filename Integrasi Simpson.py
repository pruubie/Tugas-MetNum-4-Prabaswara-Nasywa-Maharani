import numpy as np
import matplotlib.pyplot as plt
import time

# Definisi fungsi f(x)
def f(x):
    return 4 / (1 + x**2)

# Fungsi Integrasi Simpson 1/3
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

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Array untuk menyimpan hasil
integral_values = []
rms_errors = []
execution_times = []

# Testing untuk berbagai nilai N
for N in N_values:
    start_time = time.time()  # Mulai waktu eksekusi
    try:
        integral_value = simpson_13_integration(f, a, b, N)
    except ValueError as e:
        print(f"Error untuk N={N}: {e}")
        continue
    end_time = time.time()  # Akhir waktu eksekusi
    
    # Menghitung galat RMS
    rms_error = np.sqrt((integral_value - pi_reference)**2)
    
    # Menyimpan hasil
    integral_values.append(integral_value)
    rms_errors.append(rms_error)
    execution_times.append(end_time - start_time)

    print(f"N = {N}")
    print(f"Nilai Integral: {integral_value}")
    print(f"Galat RMS: {rms_error}")
    print(f"Waktu Eksekusi: {end_time - start_time:.6f} detik")
    print("-" * 40)

# Plot hasil
plt.figure(figsize=(10, 6))

# Plot galat RMS
plt.subplot(2, 1, 1)
plt.plot(N_values, rms_errors, 'o-', label='Galat RMS')
plt.xscale('log')
plt.xlabel('Jumlah Segmen (N)')
plt.ylabel('Galat RMS')
plt.title('Galat RMS vs. Jumlah Segmen (N)')
plt.grid(True)

# Plot waktu eksekusi
plt.subplot(2, 1, 2)
plt.plot(N_values, execution_times, 'o-', label='Waktu Eksekusi')
plt.xscale('log')
plt.xlabel('Jumlah Segmen (N)')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Waktu Eksekusi vs. Jumlah Segmen (N)')
plt.grid(True)

plt.tight_layout()
plt.show()
