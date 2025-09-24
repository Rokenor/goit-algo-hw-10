import numpy as np
from scipy.integrate import quad

def monte_carlo_integration(func, a, b, n_points):
    '''Обчислює визначений інтеграл функції методом Монте-Карло'''

    # Знаходимо максимальне значення функції на інтервалі [a, b]
    M = f(b)

    points_under_curve = 0

    # Генеруємо точки та підраховуємо ті, що потрапили під криву
    for _ in range(n_points):
        # Генеруємо випадкову точку (x, y) в межах прямокутника
        x_rand = np.random.uniform(a, b)
        y_rand = np.random.uniform(0, M)
        
        # Перевіряємо, чи точка знаходиться під кривою f(x)
        if y_rand <= func(x_rand):
            points_under_curve += 1

    # Обчислюємо площу прямокутника та наближене значення інтеграла.
    box_area = (b - a) * M
    integral_value = (points_under_curve / n_points) * box_area
    
    return integral_value

if __name__ == "__main__":
    # Визначення функції та параметрів
    def f(x):
        return x ** 2

    a = 0      # Нижня межа
    b = 2      # Верхня межа
    N = 100_000 # Кількість точок

    # Виклик функції для обчислення інтеграла методом Монте-Карло
    integral_monte_carlo = monte_carlo_integration(f, a, b, N)

    # Обчислення інтеграла за допомогою точного методу для перевірки
    integral_quad, error = quad(f, a, b)

    # Виведення результатів
    print(f"Метод Монте-Карло (N = {N} точок):")
    print(f"Наближене значення інтеграла: {integral_monte_carlo}")

    print("\nПеревірка:")
    print(f"Значення за допомогою scipy.integrate.quad: {integral_quad}")