def f(x):
  return x**4 + 2*x**3 - x**2 + 9*x

def integral_definida(a, b, n):
  h = (b-a)/n
  sum = 0
  for i in range(1, n):
    sum += f(a + i*h)
  return h/2 * (f(a) + f(b) + 2*sum)

result = integral_definida(0, 1, 1000)
print('Integral de x^4 + 2x^3 - x^2 + 9x limitado entre 0 e 1 =',round(result, 5))

def g(x):
  return x**2

def integral_definida(a, b, n):
  h = (b-a)/n
  sum = 0
  for i in range(1, n):
    sum += f(a + i*h)
  return h/2 * (f(a) + f(b) + 2*sum)

result = integral_definida(0, 1, 1000)
print('Integral de x^2 limitado entre 0 e 1 =',round(result, 5))
  
  
