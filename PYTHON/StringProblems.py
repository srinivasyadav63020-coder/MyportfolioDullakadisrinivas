s=input("enter word: ")
s2=s.lower()
print(s2)
a=s2.count('a')
e=s2.count('e')
i=s2.count('i')
o=s2.count('o')
u=s2.count('u')
print("Number of vowels: ",a+e+i+o+u)
#%%
#Gradecalculator
m=int(input("enter marks in maths: "))
s=int(input("enter marks in science: "))
e=int(input("enter marks in English: "))
total_marks=m+s+e
Average=total_marks/3
percentage=(total_marks/300)*100
grade=""
if percentage >90:
    grade="A"
elif percentage > 80:
    grade="B"
elif percentage >70:
    grade="C"
elif percentage >60:
    grade="D"
else:
    print("FAIL")
print("Average Marks: ",Average)
print("Grade is:",grade)
#%%
#palindrome
word=input("Enter word: ")
reverse=word[::-1]
if word==reverse:
    print("It is pallindrone")
else:
    print("not pallindrone")
#%%
#largedt of 3 numbers
a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number: "))
if a>b:
    if a > c:
        print("a is largest is: ",a)
    else:
        print("c is largest is: ",c)
elif b > a:
    if b > c:
        print("b is largest is: ",b)
    else:    
        print("c is largest: ",c)
else:
        print("c is largest: ",c)
        #%%
#checkleap year
year=int(input("enter year: "))
if year%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")
    
























    
