#Design a calculator which will give all the correct values for calculations except
# 55*8=333, 22/3=12
'''Take operator and operand from user input'''
print("Enter a and b")
a=int(input())
b=int(input())
print("Enter the op")
op=input()
if (a==55 and b==8 and op=='*'):
    print(333)
elif(a==22 and b==3 and op=='/'):
    print(12 "lol")
else:
    if op=='+':
        print(a-b)
    elif op=='-':
        print(a-b)
    elif op=='*':
        print(a*b)
    else:
        print(a/b)
