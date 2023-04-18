def add(x, y):
    """Сложение"""
    return x + y

def subtract(x, y):
    """Вычитание"""
    return x - y

def multiply(x, y):
    """Умножение"""
    return x * y

def divide(x, y):
    """Деление"""
    if y == 0:
        raise ValueError("Деление на ноль невозможно!")
    return x / y

if __name__ == '__main__':
    print("Выберите операцию.")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1/2/3/4): ")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        print(f"{num1}
