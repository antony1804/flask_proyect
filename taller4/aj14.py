with open("nombres.txt", "w") as f:
 f.write("Ana\nLuis\n")
with open("nombres.txt") as f:
 for linea in f:
  print(linea.strip())
