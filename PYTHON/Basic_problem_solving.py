num1=int(input("Enter numbers:"))
num2=int(input("Enter number:"))
print("sum:",num1+num2,sep="")
#%%
#Area of circle
radius=int(input("Enter radius of circle:"))
area=3.14*radius**2
print("Area of the circle:",area)
#%%
#finding roots
a=int(input("give a value:"))
b=int(input("give b value:"))
c=int(input("give c value:"))
d=(b**2)-4*a*c
root1=((-b+(d**0.5))/2*a)
root2=((-b-(d**0.5))/2*a)
print("roots:",root1,root2)
#%%
#swap two variables
a=int(input("give a value:"))
b=int(input("give b value:"))
a=a+b
b=a-b
a=a-b
print("after swapping:",a,b)
#%%
#temperature converter
c=int(input("give celsius:"))
f=(c*(9/5))+32
k=273.15+c
print("fahreinheit is:",f)
print("kelvin is:",k)
#%%
#money converter
usd=int(input("give ude dollar:"))
rupee=eval(input("give indian rupee:"))
print("equivalent in europe is:",usd*rupee)