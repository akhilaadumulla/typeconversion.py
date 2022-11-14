a=5;b=4.5;c='py';d='5.5';e='6';f='on';g=8
print(a+b) #int+float=9.5
print(a+g) #int+int=13
print(b+c) #typeError
print(c+d) #str+str=py5.5
print(d+e) #str+str=5.56
print(e+d) #str+str=65.5
print(e+f) #str+str=6on
print(a+d) #typeError
print(str(a)+d) #55.5
print(a+int(d)) #valueError
print(int(d)) #valueError
print(int(e)) #6
print(float(e)) #6.0
print(str(g)) #8

