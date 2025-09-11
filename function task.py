import math
print("-----CALCULATOR-------")
previous_ele=None
history=[]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Number not divide by zero!")
        return None 
    return a/b
def power(a,b):
    return a**b

while True:
    print("\n----MAIN MENU------")
    print("1. Simple Calculator")
    print("2. Scientific Calculator")
    print("3. Show History")
    print("4. Exit")
    choice=int(input("Enter your choice(1/2/3/4): "))
    if choice==4:
        print("---------Thank You---------")
        break
    if choice==3:
        if not history:
            print("Empty History")
        else:
            print("Calculation History: ")
            for item in history:
                print(item)
        continue
    
        
        
    
    if previous_ele is not None:
        use_prev = input("Do you want to use Previous Element as first number? (Y/N): ").upper()
        if use_prev == "Y":
            a = previous_ele
            print("First number (using previous result):", a)
        else:
            a=float(input("Enter your First Number: "))
    else:
        a=float(input("Enter your First Number: "))
    expr=None
    res=None
    #simple Calculator
    if choice==1:
        
        
        print("1.Add (+) ")
        print("2.Subtraction (-)")
        print("3.Multiplication (*)")
        print("4.Division (/)")
        print("5.Reminder (%)")
        operation=int(input("enter your operation(1/2/3/4)"))
        b=float(input("enter your second number: "))

        if operation==1:
            res=add(a,b)
            expr = f"{a} + {b} = {res}"
            print("The addition is:",res)
        elif operation==2:
            res=sub(a,b)
            expr = f"{a} - {b} = {res}"
            print("Subtraction is: ",res)

        elif operation==3:
            res=mul(a,b)
            expr = f"{a} * {b} = {res}"
            print("Multiplication is: ",res)
        elif operation==4:
            if b==0:
                print("Division by Zero is not allowed!")
                continue
            res=div(a,b)
            expr = f"{a} / {b} = {res}"
            print("Division is: ",res)
        elif operation==5:
            res=a%b
            expr=f"{a}%{b}={res}"
            print("Remainder is:",res)
            
        else:
            print("Invalid choice")
            continue


        
    elif choice==2:
        print("----- Scientific Calculator -----")
        print("1 power")
        print("2. Square Root")
        print("3. Sine (in degrees)")
        print("4. Cosine (in degrees)")
        print("5. Tangent (in degrees)")
        print("6. Logarithm (base 10)")
        op = int(input("Enter operation (1-6): "))
        if op==1:
            b = float(input("Enter the exponent (b): "))
            res=power(a,b)
            expr=str(a)+" ** "+str(b)+" = "+str(res)
            print("Power is:",res)
        elif op==2:
            if a<0:
                print("cannot take square root of negative number!")
                continue
            res=math.sqrt(a)
            expr = f"√{a} = {res}"
        elif op==3:
            res = math.sin(math.radians(a))
            expr = f"sin({a}) = {res}"
        elif op==4:
            res=math.cos(math.radians(a))
            expr = f"cos({a}) = {res}"
        elif op==5:
            res=math.tan(math.radians(a))
            expr = f"tan({a}) = {res}"
        elif op == 6:
            if a <= 0:
                print("Log undefined for non-positive numbers!")
                continue
            res = math.log10(a)
            expr = f"log10({a})={res}"

        else:
            print("Invalid option")
            continue
    if res is not None:
        previous_ele = res
        history.append(expr)
        print(" Result:", res)
        print("Previous Result Stored:", previous_ele)
            



































        
        

    
