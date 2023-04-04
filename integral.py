def f(x):
  return x**4 + 2*x**3 - x**2 + 9*x

def integral_definida(a, b, n):
  h = (b-a)/n
  sum = 0
  for i in range(1, n):
    sum += f(a + i*h)
  return h/2 * (f(a) + f(b) + 2*sum)

result = integral_definida(0, 1, 1000)
print(round(result, 5))
  
