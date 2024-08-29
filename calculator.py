def add(values):
    return sum(values)
def sub(values):
    result=values[0]
    for i in values[1:]:
        result-=i
    return result
def mul(values):
    result=values[0]
    for i in values[1:]:
        result*=i
    return result
def div(values):
    result=values[0]
    for i in values[1:]:
        result//=i
    return result
def mod(values):
    result=values[0]
    for i in values[1:]:
        result%=i
    return result
def cal():
    operations={'1':add,'2':sub,'3':mul,'4':div,'5':mod}
    print("1-add")
    print("2-sub")
    print("3-mul")
    print("4-div")
    print("5-mod")
    back=[]
    while True:
        x=input("please enter the operation")
        if x in operations:
            values=list(map(float,input("Enter the values with spacing").split()))
            result=operations[x](values)
            back.append(result)
            print(result)
            continue
        else:
            return "Invalid"
cal()

'''
def cal(a,x,b):
    if x=="+":
        print(a+b)
    elif x=="-":
        print(a-b)
    elif x=="*":
        print(a*b)
    elif x=="//":
        print(a//b)
    elif x=="%":
        print(a%b)
    else:
        print("Invalid")
a=int(input())
x=input()
b=int(input())
cal(a,x,b)
'''