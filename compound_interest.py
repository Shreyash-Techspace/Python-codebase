"""
Amount = P(1+r/100)**T
ci = Amount-P
"""
principal = float(input("Enter principal amount"))
rate = float(input("Enter rate of interest"))
time = float(input("Enter time duration"))
amount1 = principal * (1+ rate/100) ** time
#amount2 = principal * pow((1 + rate/100), time)
print(round(amount1,2))
ci = amount1-principal
print("Compound Interest",ci)
