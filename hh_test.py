class Geometry:
    @staticmethod
    def circle_area(radius):
        """
        Вычисляем площадь круга по радиусу.
        
        :param radius: Радиус круга
        :return: Площадь круга
        """
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        
        pi = 3.141592653589793
        return pi * radius ** 2

    @staticmethod
    def triangle_area(a, b, c):
        """
        Вычисляем площадь треугольника по трем сторонам с использованием формулы Герона.
        
        :param a: Первая сторона треугольника
        :param b: Вторая сторона треугольника
        :param c: Третья сторона треугольника
        :return: Площадь треугольника
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сумма любых двух сторон треугольника должна быть больше третьей стороны")

        # Полупериметр
        s = (a + b + c) / 2
        # Площадь по формуле Герона
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

    @staticmethod
    def is_right_triangle(a, b, c):
        """
        Проверяем, является ли треугольник прямоугольным.
        
        :param a: Первая сторона треугольника
        :param b: Вторая сторона треугольника
        :param c: Третья сторона треугольника
        :return: True, если треугольник прямоугольный, иначе False
        """
        # Сортируем стороны так, чтобы 'c' была наибольшей стороной
        sides = sorted([a, b, c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9

def main():
    while True:
        choice = input("Выберите фигуру (1 - круг, 2 - треугольник, 0 - выход): ")
        if choice == '1':
            radius = float(input("Введите радиус круга: "))
            try:
                area = Geometry.circle_area(radius)
                print("Площадь круга:", area)
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == '2':
            a = float(input("Введите сторону a треугольника: "))
            b = float(input("Введите сторону b треугольника: "))
            c = float(input("Введите сторону c треугольника: "))
            try:
                area = Geometry.triangle_area(a, b, c)
                is_right = Geometry.is_right_triangle(a, b, c)
                print("Площадь треугольника:", area)
                print("Треугольник является прямоугольным:" if is_right else "Треугольник не является прямоугольным")
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
