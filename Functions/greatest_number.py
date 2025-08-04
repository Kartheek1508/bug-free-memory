def highest_number(a,b,c):
    
    if a>b and a>c:
        return a

    if b>a and b>c:
        return b

    if c>a and c>b:
        return c

print(highest_number(11,2,3))
