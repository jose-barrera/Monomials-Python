"""Main program."""

from monomial import Monomial


def test_monomial_string_representation():
    """Prints monomials to test __str__ method."""
    print(Monomial(0, 0))
    print(Monomial(0, 1))
    print(Monomial(0, 5))
    print(Monomial(1, 0))
    print(Monomial(1, 1))
    print(Monomial(1, 5))
    print(Monomial(7.5, 0))
    print(Monomial(7.5, 1))
    print(Monomial(7.5, 5))
    print(Monomial(-0, 0))
    print(Monomial(-0, 1))
    print(Monomial(-0, 5))
    print(Monomial(-1, 0))
    print(Monomial(-1, 1))
    print(Monomial(-1, 5))
    print(Monomial(-7.5, 0))
    print(Monomial(-7.5, 1))
    print(Monomial(-7.5, 5))
    print(Monomial(91, 0))
    print(Monomial(91, 1))
    print(Monomial(91, 5))


test_monomial_string_representation()

print('This program allows to perform basic arithmetic with two')
print('monomials, assuming that conditions are complied.')
print('')

print('*** MONOMIAL 1 ***')
print('Write the coefficient 1: ', end='')
c1 = float(input())
print('Write the exponent 1: ', end='')
e1 = int(input())
print('')
M1 = Monomial(c1, e1)

print('*** MONOMIAL 2 ***')
print('Write the coefficient 2: ', end='')
c2 = float(input())
print('Write the exponent 2: ', end='')
e2 = int(input())
print('')
M2 = Monomial(c2, e2)

monomial_sum = None
monomial_difference = None
monomial_product = None
monomial_quotient = None

# Monomial addition: M1 + M2
try:
    monomial_sum = M1.add(M2)
    print('SUM: ' + str(monomial_sum))
except Exception as e:
    print('SUM: Invalid operation.')

# Monomial subtraction: M1 - M2
try:
    monomial_difference = M1.subtract(M2)
    print('DIFFERENCE: ' + str(monomial_difference))
except Exception as e:
    print('DIFFERENCE: Invalid operation.')

# Monomial multiplication: M1 * M2
monomial_product = M1.multiply(M2)
print('PRODUCT: ' + str(monomial_product))

# Monomial division: M1 / M2
try:
    monomial_quotient = M1.divide(M2)
    print('QUOTIENT: ' + str(monomial_quotient))
except Exception as e:
    print('QUOTIENT: Invalid operation.')

print()
print('Write the value to evaluate: ', end='')
value = float(input())
print()

print('Value of M1 is ' + str(M1.evaluate(value)))
print('Value of M2 is ' + str(M2.evaluate(value)))
if monomial_sum is not None:
    print('Value of M1 + M2 is ' + str(monomial_sum.evaluate(value)))
else:
    print('Value of M1 + M2 cannot be computed because \
          is an invalid operation.')
if monomial_difference is not None:
    print('Value of M1 - M2 is ' + str(monomial_difference.evaluate(value)))
else:
    print('Value of M1 - M2 cannot be computed because \
          is an invalid operation.')
print('Value of M1 * M2 is ' + str(monomial_product.evaluate(value)))
if monomial_quotient is not None:
    print('Value of M1 / M2 is ' + str(monomial_quotient.evaluate(value)))
else:
    print('Value of M1 / M2 cannot be computed because \
          is an invalid operation.')

print('')
print('THANK YOU FOR USING THIS PROGRAM!')
