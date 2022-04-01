#Programm, das in 10° - Schritten zwischen 0° und 180° den jew. Cosinus-Wert berechnet und ausgibt

import math

int_Grad = 0
int_hoechster_Grad = 180

while int_Grad <= int_hoechster_Grad:
    int_Grad_rad = int_Grad * math.pi / 180
    a = math.cos(int_Grad_rad)
    print("cos(",int_Grad,") =", a)
    int_Grad +=10
    