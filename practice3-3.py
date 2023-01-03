def z() : 
    d = (b**2) - (4*a*c)
    return d

a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
result = z()

if result < 0 :
    print("your function hasn,t root" )
elif result == 0 :
    print("your function has 2 equal roots")
    result = (-b) / (2*a)
    print(result)
else : 
    x = -b + z() ** 0.5 / 2 * a 
    y = -b - z() ** 0.5 / 2 * a 
    print("\nx : " , x , "\ny : " , y )
    z()