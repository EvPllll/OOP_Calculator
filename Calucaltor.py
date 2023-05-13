
class Calculator:
    '''
    Создание класса "Калькулятор"
    '''
    def __init__(self):
        '''
        Инициализация класса.
        История - список проведённых операций.
        Кол-во операций - кол-во операций соответственно.
        '''
        self.history = list()
        self.count_of_operations = 0

    def get_sum(self, first_some_number: float, second_some_number: float) -> float:
        '''
        Получение суммы чисел
        :param first_some_number: первое число
        :param second_some_number: второе число
        :return: сумма первого и второго числа
        '''
        result = first_some_number + second_some_number
        self.history.append(f'Sum of {first_some_number} and {second_some_number} is {result}')
        self.count_of_operations += 1
        return result

    def get_different(self, first_some_number: float, second_some_number: float) -> float:
        '''
        Получение разности чисел
        :param first_some_number: первое число
        :param second_some_number: второе число
        :return: разность первого числа ко второму
        '''
        result = first_some_number - second_some_number
        self.history.append(f'Different of {first_some_number} and {second_some_number} is {result}')
        self.count_of_operations += 1
        return result

    def get_division(self, first_some_number: float, second_some_number: float) -> float:
        '''
        Получение частого чисел
        :param first_some_number: первое число
        :param second_some_number: второе число
        :return: частное первого и второго числа
        '''
        result = first_some_number / second_some_number
        self.history.append(f'Division of {first_some_number} and {second_some_number} is {result}')
        self.count_of_operations += 1
        return result

    def get_multiplication(self, first_some_number: float, second_some_number: float) -> float:
        '''
        Получение произведение чисел
        :param first_some_number: первое число
        :param second_some_number: второе число
        :return: произведение первого и второго чисел
        '''
        result = first_some_number * second_some_number
        self.history.append(f'Multiplication of {first_some_number} and {second_some_number} is {result}')
        self.count_of_operations += 1
        return result

    def get_degree(self, first_some_number: float, second_some_number: float) -> float:
        '''
        Возведение в степень
        :param first_some_number: число
        :param second_some_number: степень числа
        :return: первое число в степени второго числа
        '''
        result = first_some_number ** second_some_number
        self.history.append(f'Degree of {first_some_number} and {second_some_number} is {result}')
        self.count_of_operations += 1
        return result

    def get_square(self, first_some_number: float) -> float:
        '''
        Получение квадратного коря числа
        :param first_some_number: число
        :return: квадратный корень числа
        '''
        result = round((first_some_number ** 0.5), 3)
        self.history.append(f'Square of {first_some_number} is {result}')
        self.count_of_operations += 1
        return result

    def show_history(self):
        '''
        Получение истории операций
        :return: список проведённых операций с числами и кол-во операций
        '''
        print(self.history)
        print(f'Count of operations is {self.count_of_operations}')

# выполнение программы

if __name__ == '__main__':
    my_calc = Calculator()

    a = my_calc.get_sum(15, 20)
    b = my_calc.get_multiplication(a, 5)
    c = my_calc.get_square(b)

    print(a, b, c, sep='\n')
    my_calc.show_history()