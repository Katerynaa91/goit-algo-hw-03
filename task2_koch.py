import turtle


def koch_curve(size, n):
    """Для візуалізації кривої та сніжинки Коха використовуємо модуль turtle.
В циклі повертаємо черепашку вліво на 60 градусів і впарво на 120 (або вліво на -120)
і ділимо вхідний розмір відрізка на 3. Рекурсивно зменшуємо рівень для 
зменшення розміру трикутників. Базовий випадок, коли рівень = 0, тоді малюється
пряма лінія.
"""
    
    if n == 0:
        turtle.forward(size)
    else:
        for angle in (60, -120, 60, 0):
            koch_curve(size / 3, n - 1)
            turtle.left(angle)


def draw_koch_snowflake(size, n):
    """Функція задає параметри для малювання черепашки.
    У циклі ітеруємо функцію кривої Коха 3 рази, повертаючись праворуч на 120 градусів
    в кінці кожної ітерації. Таким чином, отримуємо сніжинку, або три кривих Коха
    відповідно до 3х сторін рівностороннього трикутника"""
    window = turtle.Screen()
    turtle.ht()
    turtle.speed(0)
    turtle.color('purple')
    window.title("Koch's Snowflake")

    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)

    turtle.done()
    window.mainloop()


size = 300
n = 3

draw_koch_snowflake(size, n)






