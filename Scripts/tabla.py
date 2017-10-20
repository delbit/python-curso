import sys
print(sys.argv)

if len(sys.argv) == 3:
  fila = int(sys.argv[1])
  columna = int(sys.argv[2])
  if_fila = (fila >= 1) and (fila <= 9)
  if_columna = (columna >= 1) and (columna <= 9)

  if if_fila and if_columna:
    for i in range(fila):
      print('\n')
      for j in range(columna):
         print(" * ", end='')

  else:
    print('Debe ingresar 2 valores enteros y positivos comprendidos ente 1 y 9')

else:
  print('Debe incluir los dos argumentos')
  print('Ejemplo: tabla.py numero numero')
