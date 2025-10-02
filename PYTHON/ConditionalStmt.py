w=input()
if w=="sunny":
    print("play Cricket")
    print("good")
print("code ended here !!!")
#%%
#if else condition
w=input("give input: ")
if w=="sunny":
    print("play Cricket")
else:
    print("play with toy")
print("code ended here !!!")
#%%
#If elif-else condition
w=input("give input: ")
if w=="sunny":
    print("play Cricket")
elif w=="rainy":
    print("play indoor games")
else:
    print("play with toy")
print("code ended here !!!")
#%%
#if elif-else condition
weather="snowy"
time_of_day="night"
if weather=="sunny":
    print("you can play with your car toy.")
elif weather=="rainy":
    print("you can play with your boat toy")
elif weather=="snowy" and time_of_day=="night":
    print("you can play with your teddybear toy")
else:
    print("you can play with your snowman toy")
print("Stay warm and have a great day!!")
#%%
weather="snowy"
time_of_day="night"
if weather=="sunny":
    if time_of_day=="day":
        print("you can play with your car toy.")
    else:
        print("It's night. time to sleep")
elif weather=="rainy":
    print("you can play with your boat toy")
elif weather=="snowy":
    if time_of_day=="night":
        print("you can play with your teddybear toy")
else:
    print("you can play with your snowman toy")
print("Stay warm and have a great day!!")