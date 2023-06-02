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
            self.entry_calc.text = str(float(self.entry_calc.text)**2)

    def power(self, value):
        if value:
            try:
                self.x1 = self.entry_calc.text
                self.entry_calc.text += '^'
            except Exception:
                self.entry_calc.text += ""

    def sin(self, value):
        if value:
            self.entry_calc.text = str(math.sin(math.degrees(float(self.entry_calc.text))))

    def cos(self, value):
        if value:
            self.entry_calc.text = str(math.cos(math.degrees(float(self.entry_calc.text))))

    def tan(self, value):
        if value:
            self.entry_calc.text = str(math.tan(math.degrees(float(self.entry_calc.text))))

    def ten_power(self, value):
        if value:
            self.entry_calc.text = str(10**float(self.entry_calc.text))

    def sub(self, value):
        if value:
            try:
                self.x1 = self.entry_calc.text
                self.entry_calc.text += '÷'
            except Exception:
                self.entry_calc.text += ""

    def Mod(self, value):
        if value:
            try:
                self.x1 = self.entry_calc.text
                self.entry_calc.text += 'Mod'
            except Exception:
                self.entry_calc.text += ""

    def fact(self, value):
        if value:
            self.entry_calc.text = str(math.factorial(int(self.entry_calc.text)))

    def square_root(self, value):
        if value:
            self.entry_calc.text = str(math.sqrt(float(self.entry_calc.text)))
    def Up(self, value):
        if value:
            try:
                if '.' in self.entry_calc.text:
                    if int(self.entry_calc.text[-1]) >= 5:
                        self.entry_calc.text = self.entry_calc.text[:len(self.entry_calc.text) - 1]
                        self.rounding = int(self.entry_calc.text[-1])
                        self.rounding += 1
                        self.entry_calc.text = self.entry_calc.text[:len(self.entry_calc.text) - 1]
                        self.entry_calc.text += str(self.rounding)
                    else:
                        self.entry_calc.text = self.entry_calc.text[:len(self.entry_calc.text) - 1]
            except Exception:
                pass

    def upsidedown(self, value):
        if value:
            if self.entry_calc.text[0] != '-':
                minus = '-'
                minus += self.entry_calc.text
            # else:
            #     self.entry_calc.text

    def log(self, value):
        if value:
            self.entry_calc.text = str(float(math.log(float(self.entry_calc.text), 10)))

    def equal(self, value):
        if value:
            try:
                if '^' in self.entry_calc.text:
                    self.y1 = self.entry_calc.text[len(self.x1)+1:]
                    self.entry_calc.text = str(float(self.x1)**float(self.y1))
                elif '÷' in self.entry_calc.text:
                    self.y1 = self.entry_calc.text[len(self.x1)+1:]
                    self.entry_calc.text = str(float(self.x1)//float(self.y1))
                elif 'Mod' in self.entry_calc.text:
                    self.y1 = self.entry_calc.text[len(self.x1)+3:]
                    self.entry_calc.text = str(float(self.x1)%float(self.y1))
                else:
                    self.entry_calc.text = str(eval(self.entry_calc.text))
            except Exception:
                self.entry_calc.text = "Error"

class Calculator(App):
    def build(self):
        return MainContainer()

if __name__ == '__main__':
    Calculator().run()

