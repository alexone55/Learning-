class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        str_rep = str(self.real)
        if self.imaginary >= 0:
            str_rep += '+'
        str_rep += str(self.imaginary) + 'i'
        return str_rep

    def __add__(self, other):
        new_real = self.real + other.real
        new_im = self.imaginary + other.imaginary
        return Complex(new_real, new_im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            new_re = self.real * other.real - self.imaginary * other.imaginary
            new_im = self.real * other.imaginary + self.imaginary * other.real
        elif isinstance(other, int) or isinstance(other, float):
            new_re = self.real * other
            new_im = self.imaginary * other
        else:
            raise ComplexError(self, other)
        return Complex(new_re, new_im)

    __rmul__ = __mul__

    def div(self, other):
        r = float(other.real ** 2 + other.imaginary ** 2)
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / r,
                       (self.imaginary * other.real - self.real * other.imaginary) / r)

    def neg(self):
        return Complex(-self.real, -self.imaginary)

    def inv(self):
        return Complex((self.real / (self.real ** 2 + self.imaginary ** 2)) -
                       self.imaginary / (self.real ** 2 + self.imaginary ** 2))


def main():
    complex_number_1 = Complex(float(input('Enter real part of first complex number: ')),
                               float(input('Enter imaginary part of first complex number: ')))
    complex_number_2 = Complex(float(input('Enter real part of second complex number: ')),
                               float(input('Enter imaginary part of first complex number: ')))
    print('Add 2 complex number: ', Complex(complex_number_1 + complex_number_2))
    print('Multiplication of 2 complex number: ', Complex(complex_number_1 * complex_number_2))
    print('Division of 2 complex number: ', Complex.div(complex_number_1, complex_number_2))
    print('Negation of complex number: ', Complex.neg(complex_number_1))
    print('Inversion of complex number: ', Complex.inv(complex_number_1))


if __name__ == "__main__":
    main()
