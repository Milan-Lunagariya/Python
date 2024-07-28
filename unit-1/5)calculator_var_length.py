# sign = int(input("Enter num sign (+, *) : "))

def calc( sign, *args ) :
    if( (sign == '+') or (sign == '*') or (sign == '-') or (sign == '/') ) :
        if( sign == '+' ):
            result = 0
            for num in args: result += num 
            return (result)    
        if( sign == '*' ):
            result = 1
            for num in args: result *= num 
            return (result)    
        if( sign == '-' ):
            result = args[0]
            for num in args[1:]:         
                result -= num 
            return (result)    
        if( sign == '/' ):
            result = args[0]
            for num in args[1:]: result /= num 
            return (result)    
    else :
        return (" ------ Sign is Invalid ! ------ ")
    
     
addition = calc( '+', 1, 2, 3, 4 )
multiplication = calc( '*', 1, 2, 3, 4 )
substraction = calc( '-', 5, 2, 1)
divition = calc( '/', 10, 2, 2 )

print( "Addition : " , addition )     
print( "Multiplication : ", multiplication )
print( "Substraction : ", substraction )
print( "Divition : ", divition )

print( calc( "test", 10, 20 ) )

