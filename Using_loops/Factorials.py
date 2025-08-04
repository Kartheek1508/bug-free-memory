#Calculating factorials

n = int(input())
f=1

for i in range(1,n+1):
  f = f*i

print(f)

#alternate solution

n = int(input('number:'))
f = 1
for i in range (0,n):
    f = (n-i)*f
    
print(f)