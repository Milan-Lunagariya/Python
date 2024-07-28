

def calc(sign): 
    divition = addition = substraction = 0
    multiplication = 1 
    if sign == '+': 
        num_of_val = int(input( "Enter no of value : " ))
        for i in range(0, num_of_val) : addition += int(input("Enter value "))
        return (addition)
    elif sign == '*' : 
        num_of_val = int(input( "Enter no of value : " ))
        for i in range(0, num_of_val) : multiplication *= int(input("Enter value "))
        return (multiplication)
    elif sign == '/' or sign == '-': 
        for i in range(0, 2) : 
            num1 = int(input("Enter value 1: "))
            num2 = int(input("Enter value 2: "))
            if( sign == '/' ) :
                if num1 != 0 :
                    divition = num1 / num2
                    return (divition)
                else :
                    return ("Using 0 by can\'t divided")
            else :
                substraction = num1 - num2
                return (substraction)
    else :
        return ("Invalid Sign")
    

sign = (input( "Enter sign for perform opration (+,-,*,/):  " ))

awnser = calc(sign)
print( "---------------------- " )    
print( "Awnser: ", awnser )    
print( "---------------------- " )    