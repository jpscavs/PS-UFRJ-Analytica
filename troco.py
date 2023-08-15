class InvalidInputError(Exception):
    pass

s = input()

if not s[:-3].isnumeric() or s[-3]!="." or not s[-2:].isnumeric() or len(s[-2:])>2:
  raise InvalidInputError("Input Inválido")
else:
  val = float(s)
  divs = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, .5, .25, .1, .05, .01]
  mons = [0 for _ in divs]

  for i,div in enumerate(divs):
    q,r = (int(val/div), val%div)
    mons[i] = q
    val = r
  
  print("NOTAS:")
  for i in range(6):
    print(mons[i], "nota(s) de R$", str(divs[i])+"0")
  print()
  print("MOEDAS:")
  for i in range(6,12):
    print(mons[i], "moeda(s) de R$", str(divs[i])+"0" if len(str(divs[i]))==3 else str(divs[i]))