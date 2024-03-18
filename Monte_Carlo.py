'''Обчисліть значення інтеграла функції за допомогою методу Монте-Карло,
інакше кажучи, знайдіть площу під цим графіком (сіра зона).
Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло,
шляхом порівняння отриманого результату та аналітичних розрахунків або результату
виконання функції quad. Зробіть висновки.'''

import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import random


def monte_carlo(f, a, b, num_experiments):
    f_max = max(f(x) for x in range(a, b+1))
    area = 0

    for _ in range(num_experiments):
        x = random.uniform (a,b)
        y = random.uniform (0, f_max)

        if y <= f (x):
            area += 1

    average_area = area / num_experiments
    integral = average_area * (b - a) * f_max
    
    return integral

def f(x):
    return x**2

a = 0
b = 2

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

average_area = monte_carlo(f, a, b, 100)
print(f"Average area for 100 experiments: {average_area}")

# check
result, error = spi.quad(f, a, b)

print("Integral:", result)


fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
            
