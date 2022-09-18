import math
r=3
m=4

#Gömb térfogata: V=4/3*πr^3
#Gömb felszine: A=4*π*r^2
print(f"A gomb terfogata: V={4/3*(math.pi*r**3)}")
print(f"A gömb felszine: A={4*(math.pi*r**2)}")

#A henger térfogata: V=r^2*π*m
#A henger felszine: A=2*r^2*π+2*r*π*m
print(f"A henger térfogata: V={r**2*math.pi*m}")
print(f"A henger felszine: A={2*(r**2*math.pi)+2*(r*math.pi*m)}")

#út-idő sebesség s=50km t=30min v=?
s=50000
t=1800
v=s/t
print(f"A sebesség: {v}m/s") #{v:.2f} vagy {round(v)}