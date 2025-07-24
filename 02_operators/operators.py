#Operators->These are used to perform operations on variables and values.
#Arthmetic Operators
#Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulus(%), Exponentiation(**), Floor Division(//)
a=30
b=20
print('Addition:',a+b) 
print('Subtraction:',a-b)
print('Multiplication:',a*b)
print('Division:',a/b)
print('Modulus:',a%b)
print('Exponentiation:',a**b)
print('Floor Division:',a//b)

#Assignment/Compound Operators
#Addition Assignment(+=), Subtraction Assignment(-=), Multiplication Assignment(*=), Division Assignment(/=), Modulus Assignment(%=), Exponentiation Assignment(**=), Floor Division Assignment(//=)
x= 10
x+=5
print('Addition Assignment:',x)
x-=3
print('Subtraction Assignment:',x)
x*=2
print('Multiplication Assignment:',x)
x/=4
print('Division Assignment:',x)
x%=3
print('Modulus Assignment:',x)
x**=2
print('Exponentiation Assignment:',x)
x//=1
print('Floor Division Assignment:',x)

#Relational Operators
#Equal(==), Not Equal(!=), Greater Than(>), Less Than(<), Greater Than or Equal To(>=), Less Than or Equal To(<=)
p= 10
q= 20
print('Equal:', p == q)
print('Not Equal:', p != q)
print('Greater Than:', p > q)
print('Less Than:', p < q)
print('Greater than or equal to:', p>=q)
print('Less than or equal to:', p<=q)

#Logical Operators
#and, or, not
r=6
s=4
t=5
print("AND:", r>s and s<t)
print("OR:", r>s or s<t)
print('NOT:', not r>s)

#Membership Operators
#in, not in
u='Python is eazy'
print('z is present in u','z' in u)
print('f is not present in u','f' in u)

#Identity Operators
# is, is not 
g=10
h=10
print(g is h)
print(g is not h)

#Bitwise Operators
#AND(&), OR(|), XOR(^), Left Shift(<<), Right Shift(>>)
i=5
j=7
print('AND(&):',i & j)
print('OR(|):', i|j)
print('XOR(^):',i^j)
print('Left Shift(<<):', i<<3)
print('Right Shift:', j>>2)
