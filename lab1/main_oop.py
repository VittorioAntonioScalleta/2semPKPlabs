import sys
import math

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve_quadratic_for_t(self):
        discriminant = self.b**2 - 4 * self.a * self.c
        print(f"Дискриминант: {discriminant}")
        
        if discriminant > 0:
            t1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            t2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return t1, t2
        elif discriminant == 0:
            t = -self.b / (2 * self.a)
            return t, None
        else:
            return None, None 

    def solve_biquadratic(self):
        if self.a == 0:
            print("Это не биквадратное уравнение, так как A = 0.")
            return

        t1, t2 = self.solve_quadratic_for_t()

        roots = []
        if t1 is not None and t1 >= 0:
            roots.append(math.sqrt(t1))
            roots.append(-math.sqrt(t1))

        if t2 is not None and t2 >= 0:
            roots.append(math.sqrt(t2))
            roots.append(-math.sqrt(t2))

        if roots:
            print("Действительные корни уравнения: ", sorted(set(roots)))
        else:
            print("Действительных корней нет.")

class InputHandler:
    @staticmethod 
    def get_coefficient(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")
    @staticmethod 
    def get_coefficient_from_args_or_input(arg_index, prompt):
        try:
            return float(sys.argv[arg_index])
        except (IndexError, ValueError):
            return InputHandler.get_coefficient(prompt)

def main():
    a = InputHandler.get_coefficient_from_args_or_input(1, "Введите коэффициент A: ")
    b = InputHandler.get_coefficient_from_args_or_input(2, "Введите коэффициент B: ")
    c = InputHandler.get_coefficient_from_args_or_input(3, "Введите коэффициент C: ")

    equation = BiquadraticEquation(a, b, c)

    equation.solve_biquadratic()

if __name__ == "__main__":
    main()
