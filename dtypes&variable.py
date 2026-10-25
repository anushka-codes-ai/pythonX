#Integer (+ve and -ve both )        or call number

print(8)
#long and large int they can handle.
#1*10^308
print(1e309)#inf : infinite 
print(1e308)#$maximum value they can handles

#Decimal/Float
print(3.55)
print(1.7e309)#inf
print(1.7e308)#maximum 1.7*10^308 they can handle

#Boolean
print(True)
print(False)
#print("True") : its just a string 

#String / text 
print('HELLO WORLD ')

#COMPLEX NUMBER
print(5+6j)#reason of ur pain 
#use very less 

#view these
#list(array of c)
print([1,23,4,5])
#Tuple
print((1,2,32,54,2))
#sets
print({1,2,46,7})
#Dictionary
print({"Name": "Anushka",'Gender':'Female','weight':65})
#interpreted only because python is a interpreter language .
# imp. function 
print(type(3))
print(type(3.3))
print(type("hello"))
print(type(5+5j))
print(type([1,2,4]))

#variables : container .
#u can store anything on it .
#what user enter we don't knows. ..so how we know that.
#what happens in future 
#container for future use

#c/c++
#int name = "Anushka"
#in python
name ="Anushka " 
#Python is intelligent enough so they knows what's the datatype
#here we can't declare the datatype
print(name)#prints whats inside the name .
a=4
b=6
print(a+b)
#here we take text inside and store that inside the variable before equal to
#when we need we directly create the variable 

#dynamic typing :
#in c++
#int a =5;
# in python
# a=5 
#here we don't tell the datatype of the variable .
#interpreter automatically understand if value is 5 so that is definately integer.
#if value is 5.5 means float 
#if value is anushka so that's the string
#static typing in c
#intialise the datatype at the time of declaration of a variable
#int a = 5 #c+\java\c use static typing 

#dynamic binding
#in python if we are created a variable.but  they can be changable anytime(they don't have fixed value .)
#python : in same program they can store different datatype
#even list also storeable .
a =6
print(a)
a="Anushka"
#in static binding if we create a variable we can't change there datatype
#int a =5
#they can store different value but can't storeble different datatype.

#stylist way of creating variables
#lets create 3 variable together .
a=1
b=2
c=3
print(a,b,c)
a,c,c=1,2,3
print(a,b,c)
#wrong syntax
#Error : a,b,c =5 : cannot unpack non - iterable int object 
a=b=c=5
print(a,b,c)





