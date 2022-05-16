import math
co = float(input("Comprimento do cateto oposto"))
ca = float(input("Comprimento do cateto adjacente "))
hi = math.hypot(co, ca)
print("a hipotenusa vai medir {:.2f}".format(hi))