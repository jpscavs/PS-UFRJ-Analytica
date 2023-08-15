dof = {}

while True:
  ni = input()
  if ni == "f":
    break
  elif ni.isnumeric():
    if ni in dof:
      dof[ni] += 1
    else:
      dof[ni] = 1
for number in dof:
  print("O número", number, "apareceu", dof[number], "vezes" if dof[number]>1 else "vez")
print("Fim...")
