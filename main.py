import math
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Complex:
    def __init__(self, re, im):
        self.__re = re
        self.__im = im

    def get_re(self):
        return self.__re

    def get_im(self):
        return self.__im

    def set_re(self, re):
        self.__re = re

    def set_im(self, im):
        self.__im = im

    def sum(self, rhs_complex):
        return Complex(self.__re + rhs_complex.__re, self.__im + rhs_complex.__im)

    def dif(self, rhs_complex):
        return Complex(self.__re - rhs_complex.__re, self.__im - rhs_complex.__im)

    def division(self, rhs_complex):
        re_part = (self.__re*rhs_complex.__re + self.__im*rhs_complex.__im)/(rhs_complex.__re**2 + rhs_complex.__im**2)
        im_part = (rhs_complex.__re*self.__im - self.__re*rhs_complex.__im)/(rhs_complex.__re**2 + rhs_complex.__im**2)
        return Complex(re_part, im_part)

    def multiplication(self, rhs_complex):
        re_part = self.__re*rhs_complex.__re - self.__im*rhs_complex.__im
        im_part = self.__im*rhs_complex.__re + self.__re*rhs_complex.__im
        return Complex(re_part, im_part)

    def module(self):
        return math.sqrt(self.__re**2 + self.__im**2)

    def print_complex(self):
        print(f"Real part: {self.__re}      Imaginary: {self.__im}")


if __name__ == '__main__':
    complex_number = Complex(3, -5)
    real_part = complex_number.get_re()
    imaginary_part = complex_number.get_im()
    print(f"Real part: {real_part}      Imaginary: {imaginary_part}")
    print("Change the real part to -13 and imaginary to 336:")
    complex_number.set_re(-13)
    complex_number.set_im(336)
    complex_number.print_complex()

    print("\ntesting sum:")
    first_summand = Complex(2, 2)
    second_summand = Complex(133, -22)
    first_summand.print_complex()
    second_summand.print_complex()
    print("result:")
    sum_res = first_summand.sum(second_summand)
    sum_res.print_complex()

    print("\ntesting dif:")
    first_dif = Complex(2, 2)
    second_dif = Complex(3, -22)
    first_dif.print_complex()
    second_dif.print_complex()
    print("result:")
    dif_res = first_dif.dif(second_dif)
    dif_res.print_complex()
    print_hi('PyCharm')

    print("\ntesting divsion:")
    first_div = Complex(2, 3)
    second_div = Complex(-5, -3)
    first_div.print_complex()
    second_div.print_complex()
    print("result:")
    div_res = first_div.division(second_div)
    div_res.print_complex()

    print("\ntesting multiplication:")
    first_mul = Complex(2, 3)
    second_mul = Complex(-5, -3)
    first_mul.print_complex()
    second_mul.print_complex()
    print("result:")
    mul_res = first_mul.multiplication(second_mul)
    mul_res.print_complex()

    print("\ntesting module of complex number:")
    complex_number = Complex(3, -33)
    module_of_complex_number = complex_number.module()
    print("result:" + str(module_of_complex_number))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
