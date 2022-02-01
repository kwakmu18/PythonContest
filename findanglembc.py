import math
a=int(input())
b=int(input())
angle=round(math.acos(a/(math.sqrt(a**2+b**2)))*180/math.pi)
print(str(90-round(math.acos(a/(math.sqrt(a**2+b**2)))*180/math.pi))+u'\N{DEGREE SIGN}' if angle>45 else str(90-round(math.acos(a/(math.sqrt(a**2+b**2)))*180/math.pi))+u'\N{DEGREE SIGN}')