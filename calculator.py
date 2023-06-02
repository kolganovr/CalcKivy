from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import math
class MainContainer(GridLayout):
    entry_calc = ObjectProperty()
    x1 = None
    y1 = None
    rounding = None
    def delete(self, value):
        if value:
            self.entry_calc.text = self.entry_calc.text[:len(self.entry_calc.text)-1]

    def square(self, value):
        if value:
            value = self.equal(value)
            self.entry_calc.text = str(float(value)**2)

    def power(self, value):
        if value:
            try:
                self.x1 = self.entry_calc.text
                self.entry_calc.text += '^'
            except Exception:
                self.entry_calc.text += ""

    def sin(self, value):
        if value:
            value = self.equal(value)
            self.entry_calc.text = str(math.sin(math.radians(float(value))))

    def cos(self, value):
        if value:
            value = self.equal(value)
            self.entry_calc.text = str(math.cos(math.radians(float(value))))

    def tan(self, value):
        if value:
            value = self.equal(value)
            self.entry_calc.text = str(math.tan(math.radians(float(value))))

    def ten_power(self, value):
        if value:
            value = self.equal(value)
            # Избегаем переполнения памяти
            if float(value) > 100:
                self.entry_calc.text = "Error"
            else:
                self.entry_calc.text = str(10**float(value))

    def sub(self, value):
        if value:
            try:
                self.x1 = self.equal(value)
                self.entry_calc.text += '÷'
            except Exception:
                self.entry_calc.text += ""

    def Mod(self, value):
        if value:
            try:
                self.x1 = self.equal(value)
                self.entry_calc.text += 'Mod'
            except Exception:
                self.entry_calc.text += ""

    def fact(self, value):
        if value:
            value = self.equal(value)
            self.entry_calc.text = str(math.factorial(int(value)))

    def square_root(self, value):
        if value:
            # Сначала выполняем все операции, а потом извлекаем корень
            value = self.equal(value)
            self.entry_calc.text = str(math.sqrt(float(value)))

    # Округление числа по правилам математики
    def Round(self, value):
        if value:
            value = self.equal(value)
            self.entry_calc.text = str(round(float(value)))

    # Изменение знака числа
    def upsidedown(self, value):
        if value:
            if self.entry_calc.text[0] == '-':
                self.entry_calc.text = self.entry_calc.text[1:]
            else:
                self.entry_calc.text = '-' + self.entry_calc.text

    def log(self, value):
        if value:
            value = self.equal(value)
            self.entry_calc.text = str(math.log10(float(value)))

    def equal(self, value):
        if value:
            try:
                if '^' in self.entry_calc.text:
                    self.y1 = self.entry_calc.text[len(self.x1)+1:]
                    self.entry_calc.text = str(float(self.x1)**float(self.y1))
                elif '÷' in self.entry_calc.text:
                    self.y1 = self.entry_calc.text[len(self.x1)+1:]
                    self.entry_calc.text = str(float(self.x1)/float(self.y1))
                elif 'Mod' in self.entry_calc.text:
                    self.y1 = self.entry_calc.text[len(self.x1)+3:]
                    self.entry_calc.text = str(float(self.x1)%float(self.y1))
                else:
                    self.entry_calc.text = str(eval(self.entry_calc.text))
            except Exception:
                self.entry_calc.text = "Error"
        return self.entry_calc.text

class Calculator(App):
    def build(self):
        return MainContainer()

if __name__ == '__main__':
    Calculator().run()

