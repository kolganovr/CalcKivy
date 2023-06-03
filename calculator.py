# Импортируем необходимые модули
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import math

# Создаем класс MainContainer, который является подклассом GridLayout
class MainContainer(GridLayout):
    # Определяем свойство entry_calc
    entry_calc = ObjectProperty()
    # Инициализируем поля x1, y1 и rounding значением None
    x1 = None
    y1 = None
    rounding = None
    
    # Метод delete удаляет последний символ в поле ввода при нажатии на кнопку «DEL».
    def delete(self, value):
        if value:
            self.entry_calc.text = self.entry_calc.text[:len(self.entry_calc.text)-1]
    
    # Метод square возводит число, записанное в поле ввода, в квадрат при нажатии на кнопку «x²».
    def square(self, value):
        if value:
            # Вычисляем значение в поле ввода и возводим его в квадрат
            value = self.equal(value)
            self.entry_calc.text = str(float(value)**2)
    
    # Метод power сохраняет значение в поле ввода и добавляет знак возведения в степень при нажатии на кнопку «^».
    def power(self, value):
        if value:
            try:
                # Сохраняем значение в поле ввода и добавляем знак возведения в степень
                self.x1 = self.entry_calc.text
                self.entry_calc.text += '^'
            except Exception:
                self.entry_calc.text += ""
    
    # Метод sin вычисляет синус угла в градусах, записанного в поле ввода, при нажатии на кнопку «sin».
    def sin(self, value):
        if value:
            # Вычисляем значение синуса
            value = self.equal(value)
            self.entry_calc.text = str(math.sin(math.radians(float(value))))
    
    # Метод cos вычисляет косинус угла в градусах, записанного в поле ввода, при нажатии на кнопку «cos».
    def cos(self, value):
        if value:
            # Вычисляем значение косинуса
            value = self.equal(value)
            self.entry_calc.text = str(math.cos(math.radians(float(value))))
    
    # Метод tan вычисляет тангенс угла в градусах, записанного в поле ввода, при нажатии на кнопку «tan».
    def tan(self, value):
        if value:
            # Вычисляем значение тангенса
            value = self.equal(value)
            self.entry_calc.text = str(math.tan(math.radians(float(value))))
    
    # Метод ten_power вычисляет 10 в степени, записанной в поле ввода, при нажатии на кнопку «10^x».
    def ten_power(self, value):
        if value:
            # Вычисляем значение 10 в степени и избегаем переполнения памяти
            value = self.equal(value)
            if float(value) > 100:
                self.entry_calc.text = "Error"
            else:
                self.entry_calc.text = str(10**float(value))
    
    # Метод sub сохраняет значение в поле ввода и добавляет знак деления при нажатии на кнопку «÷».
    def sub(self, value):
        if value:
            try:
                # Сохраняем значение в поле ввода и добавляем знак деления
                self.x1 = self.equal(value)
                self.entry_calc.text += '÷'
            except Exception:
                self.entry_calc.text += ""
    
    # Метод Mod сохраняет значение в поле ввода и добавляет знак остатка от деления при нажатии на кнопку «Mod».
    def Mod(self, value):
        if value:
            try:
                # Сохраняем значение в поле ввода и добавляем знак остатка от деления
                self.x1 = self.equal(value)
                self.entry_calc.text += 'Mod'
            except Exception:
                self.entry_calc.text += ""

    # Метод fact вычисляет факториал числа, записанного в поле ввода, при нажатии на кнопку «x!».
    def fact(self, value):
        if value:
            # Вычисляем значение факториала
            value = self.equal(value)
            self.entry_calc.text = str(math.factorial(int(value)))

    # Метод square_root извлекает квадратный корень из числа, записанного в поле ввода, при нажатии на кнопку «√x».
    def square_root(self, value):
        if value:
            # Вычисляем значение квадратного корня
            value = self.equal(value)
            self.entry_calc.text = str(math.sqrt(float(value)))

    # Метод Round округляет число, записанное в поле ввода, по правилам математики при нажатии на кнопку «Round».
    def Round(self, value):
        if value:
            # Округляем число по правилам математики
            value = self.equal(value)
            self.entry_calc.text = str(round(float(value)))

    # Метод upsidedown меняет знак числа, записанного в поле ввода, при нажатии на кнопку «±».
    def upsidedown(self, value):
        if value:
            # Изменяем знак числа
            if self.entry_calc.text[0] == '-':
                self.entry_calc.text = self.entry_calc.text[1:]
            else:
                self.entry_calc.text = '-' + self.entry_calc.text

    # Метод log вычисляет логарифм числа, записанного в поле ввода, по основанию 10 при нажатии на кнопку «log».
    def log(self, value):
        if value:
            # Вычисляем значение логарифма
            value = self.equal(value)
            self.entry_calc.text = str(math.log10(float(value)))

    # Метод equal вызывается при нажатии на кнопку «=». Он выполняет арифметические операции, записанные пользователем в поле ввода, и выводит результат в поле вывода.
    def equal(self, value):
        if value:
            try:
                if '^' in self.entry_calc.text:
                    # Если в поле ввода есть знак возведения в степень, то вычисляем степень
                    self.y1 = self.entry_calc.text[len(self.x1)+1:]
                    self.entry_calc.text = str(float(self.x1)**float(self.y1))
                elif '÷' in self.entry_calc.text:
                    # Если в поле ввода есть знак деления, то выполняем деление
                    self.y1 = self.entry_calc.text[len(self.x1)+1:]
                    self.entry_calc.text = str(float(self.x1)/float(self.y1))
                elif 'Mod' in self.entry_calc.text:
                    # Если в поле ввода есть знак остатка от деления, то вычисляем остаток
                    self.y1 = self.entry_calc.text[len(self.x1)+3:]
                    self.entry_calc.text = str(float(self.x1)%float(self.y1))
                else:
                    # Иначе выполняем арифметическое выражение
                    self.entry_calc.text = str(eval(self.entry_calc.text))
            except Exception:
                # Если во время вычислений возникает ошибка, то выводим сообщение "Error"
                self.entry_calc.text = "Error"
        
        # Возвращаем значение поля вывода
        return self.entry_calc.text

# Класс Calculator является главным классом приложения. 
# Он наследуется от класса App и содержит метод build, 
# который возвращает экземпляр класса MainContainer.
class Calculator(App):
    def build(self):
        return MainContainer()

# Если файл запускается напрямую, то создается экземпляр класса Calculator и вызывается метод run.
if __name__ == '__main__':
    Calculator().run()

