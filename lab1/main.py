import sys
import math

def get_coefficient(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

def get_coefficient_from_args_or_input(arg_index, prompt):
    try:
        return float(sys.argv[arg_index])
    except (IndexError, ValueError):
        return get_coefficient(prompt)

def solve_quadratic_for_t(a, b, c):
    discriminant = b**2 - 4 * a * c
    print(f"Дискриминант: {discriminant}")

    if discriminant > 0:
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return t1, t2
    elif discriminant == 0:
        t = -b / (2 * a)
        return t, None
    else:
        return None, None

def solve_biquadratic_equation(a, b, c):
    if a == 0:
        print("Это не биквадратное уравнение, так как A = 0.")
        return
    
    t1, t2 = solve_quadratic_for_t(a, b, c)

    roots = []
    if t1 is not None and t1 >= 0:
        x1 = math.sqrt(t1)
        x2 = -math.sqrt(t1)
        roots.extend([x1, x2])

    if t2 is not None and t2 >= 0:
        x3 = math.sqrt(t2)
        x4 = -math.sqrt(t2)
        roots.extend([x3, x4])

    if roots:
        print("Действительные корни уравнения: ", sorted(set(roots)))
    else:
        print("Действительных корней нет.")

def main():
    a = get_coefficient_from_args_or_input(1, "Введите коэффициент A: ")
    b = get_coefficient_from_args_or_input(2, "Введите коэффициент B: ")
    c = get_coefficient_from_args_or_input(3, "Введите коэффициент C: ")

    solve_biquadratic_equation(a, b, c)

if __name__ == "__main__":
    main()
