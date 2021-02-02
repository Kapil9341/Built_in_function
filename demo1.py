#Built-in-function
#abs() # Return absalute value(+ve value)
x=-10
print(abs(x))         #10

#all() chcek value itearbal or not
l=[1,2,3,4,5]
print(all(l))         #True

l1=[0,1,2,3,4]
print(all(l1))        #False

l2=['a','b','c','d','e']
print(all(l2))        #True

l3=[1,'2','ab',123,"hjk"]
print(all(l3))        #True

#any() if any one value is iterable print true
l_=[0,1,2,3,4,5,6]
print(any(l_))        #True

l_1=[0,0,0,0,0,0]
print(any(l_1))      #False

l_2=[0,"a",'s','s','ser',1,1.0,2.0]
print(any(l_2))      #True

#ascii() return ascii value of special symbol or word  
x='Ⓕⓞⓝⓣ'
print(ascii(x))     #'\u24bb\u24de\u24dd\u24e3'
x1='ƒσηт gєηєяαтσя'
print(ascii(x1))    #'\u0192\u03c3\u03b7\u0442 g\u0454\u03b7\u0454\u044f\u03b1\u0442\u03c3\u044f'

#chr() return charcter of ascii value
n=65
print(chr(n))       # A

#ord() Return ascii value of Words/Return integer equivalent of a character
s="A"
print(ord(s))       # 65

#bin() return binary number
n=123
print(bin(n))       #0b1111011

#bool() Return boolean value true or false
a=120
b=130
print(bool(a==b))  # False
print(bool(a>b))   # False
print(bool(b>a))   # True
print(bool(a!=b))  # True

#float() Return float value
n=12
n1=(float(n))
print(n1)
print(type(n1))
print(float("inf"))
print(float("nan"))
#print(float("abc")) # ValueError: could not convert string to float: 'abc'

#bytes() Return bytes
print(bytes(5))              #b'\x00\x00\x00\x00\x00'
print(bytes('hey','UTF-8'))  #b'hey'
print(bytes('hey','UTF-16')) #b'\xff\xfeh\x00e\x00y\x00'

#byteasarry
print(bytearray(5))             #bytearray(b'\x00\x00\x00\x00\x00') 
print(bytearray('hey',"UTF-8")) #bytearray(b'hey')
#print(bytearray('hey'))        #TypeError: string argument without an encoding
#print(bytearray('hey',"abc"))  #LookupError: unknown encoding: abc

#callable() Return true or false if class or fun.. are callable return true otherwise false
print(callable("hello"))       # False
print(callable(type("hello"))) # True

#compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

x=5
code=compile('x +5','','eval')
result=eval(code)
print(result)     #10
#single
x=50
y=compile('x','','single')
exec(y)           #50 
x='abc'
y=compile('x','','single')
exec(y)           #abc

#class complex([real[, imag]]) Return complex number
print(complex())       #0j
print(complex(1))      #(1+0j)
print(complex(2+3))    #(5+0j)
#print(complex('abc')) #ValueError: complex() arg is a malformed string
print(complex('nan'))  #(nan+0j)
print(complex('inf'))  #(inf+0j)



