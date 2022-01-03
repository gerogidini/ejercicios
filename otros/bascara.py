import math
def find_roots(a, b, c):
    
    x1 = (-b + (math.sqrt((b**2)-(4*a*c))))/(2*a)
    x2 = (-b - (math.sqrt((b**2)-(4*a*c))))/(2*a)
    result = (x1, x2)
    
    return result

print(find_roots(2, 10, 8));