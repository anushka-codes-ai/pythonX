#1. Python Output

# Python is a case sensitive language

print("I love my mom !")
print("I love my Dad !")

print('Mom')
print("Dad")
print("it's me ")
print('''Hello miss ? ''')

print(1)
print(99.99)
print(True) #True

print("Hi " , 35, .5 ,"$" , " is a price of moon cake : ",True )
 
print("https:","colab.research.google.com","drive" , sep="/")

print("Hi.")
print("coderX")

print('hello',end='-')
print('world')

###
# || 2. Data Types
###

# Integer
print(8)
# 1*10^308
print(1e309)

# Decimal/Float
print(8.55)
print(1.7e309)

# Text/String
print('Hello World')

# complex
print(5+6j)

# List-> C-> Array
print([1,2,3,4,5])

# Tuple
print((1,2,3,4,5))

# Sets
print({1,2,3,4,5})

# Dictionary
print({'Origin':'Asian','Age':45,'weight':111})

# type
type([1,2,3])
print(type(["name","marks"]))

###
# ||3. Variables
###

# Static Vs Dynamic Typing
# Static Vs Dynamic Binding
# stylish declaration techniques

# C/C++
what = 'Rest room'
print(what)
a = 5
b = 6
print(a + b)

"""
# Dynamic Typing
a = 5
# Static Typing
int a = 5
"""
"""
# Dynamic Binding
a = 5
print(a)
a = 'see ur best not ur X . @gyaniDiDi '
print(a)

# Static Binding
int a = 5
"""

a = 1
b = 2
c = 3
print(a,b,c)

a,b,c = 11,3,4
print(a,b,c)
#check :    a,b,c = 11,03,4     output:print(a,b,c) ?

a=b=c= 111
print(a,b,c)

#comments
# this is a comment
# 109th line time to assign new project !

###
# ||4. Keywords & Identifiers
###

# Keywords
# Identifiers
# You can't start with a digit
name1 = ' Chainsmoker o_o '
print(name1)
# You can use special chars -> _
_ = 'chain'
print(_)
# identiers can not be keyword


#5. User Input
# Static Vs Dynamic
#Static: The value is already fixed in the code.
email = "abc@gmail.com"
print(email)
#Dynamic: The value comes from the user while the program is running.
email = input("Enter Email: ")
print(email)

# take input from users and store them in a variable
fnum = int(input('enter first number'))
snum = int(input('enter second number'))
#print(type(fnum),type(snum))
# add the 2 variables
result = fnum + snum
# print the result
print(result)
print(type(fnum))

#6. Type Conversion
"""     Implicit: Python automatically converts data types, e.g. `5 + 5.6`.

Explicit: The programmer manually converts data types using `int()`, `float()`, or `str()`, e.g. `4 + int('4')`.    """

# Implicit Vs Explicit
print(5+5.6)
print(type(5),type(5.6))

#E:TypeError  > print(4 + '4')
print(4 + int('4'))#explicit

# Explicit
# str -> int
#int(4+5j)

# int to str
print(str(5))

# float
print(float(4))

#7. Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)


x = 3.14j
print(x.imag)

string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"
#r before a string makes it a raw string, so escape sequences like \n are treated as normal text instead of a newline.

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

a = True + 4
b = False + 10

print("a:", a)
print("b:", b)

k = None
a = 5
b = 6
print('Program exe')

#8. Operators

# Arithmetic
# Relational
# Logical
# Bitwise
# Assignment
# Membership








