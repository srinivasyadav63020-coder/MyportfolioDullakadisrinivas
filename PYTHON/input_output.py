name=input("enter name:")
print(name)
num=input("enter num:")
num2=int(num)
print(type(num2))
#%%
name=input("enter name:")
age=int(input("enter age:"))
print("Hello! "+name+" your",age,"years old")
#%%
a=input("give a value:")
b=input("give b value:")
print(a,b,a,b,sep=",",end=" Ended here.")
#%%
#Example-1
name=input("enter name:")
print("Hello",name,sep=", ",end="!")
#%%
#Example-2
num=int(input("enter num:"))
print("You entered:",num,sep="")
#%%
#Ex-3
num=float(input("enter number:"))
print("Value of Pi:",num,sep="")
#%%
#EX-4 
a=input("enter values:")
x,y,z=a.split(" ")
sum=int(x)+int(y)+int(z)
print("Sum of Inputs:",sum)
#%%
#Ex-5
a=input("enter name and age:")
name,age=a.split(",")
print("Name:",name,",Age:",age,sep='')
#%%
#Ex-6
n=int(input("enter number:"))
for i in range(0,n):
    a=n-i
    #print(a,end=" ")
print(a)
#print("Countdown:",a)
#%%
x,y=input("enter x,y values:").split(",")
a=int(x)
b=int(y)
print("10 > 5:",a>b,"10 < 5",a<b,"10 == 5",a==b,"10 !=5 ",a!=b)
#%%
a,b=input("Enter name and age:").split(",")
print(f"Name:{a},Age:{b} year's")














