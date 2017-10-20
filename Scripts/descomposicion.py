import sys

if len(sys.argv) == 2:
  numero = int(float(sys.argv[1]))

  if numero < 0:
    print('El argumentos debe ser positivo')

  else:
    digitos = len(str(numero))

    for i in range(digitos):
      unidad = numero % 10
      numero = int(float(numero) / 10)

      print('{unidad:0{digitos}d}'.format(digitos=digitos, unidad=unidad * (10 ** i)))

else:
  print('Debe incluir el argumentos')
  print('Ejemplo: tabla.py numero')

print(sys.argv)
