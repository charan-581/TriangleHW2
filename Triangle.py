def classifyTriangle(a = None, b = None, c = None):
    
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    elif a == None or b == None or c == None:
        return 'InvalidInput'
    
    elif a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    elif a <= 0 or b <= 0 or c <= 0:  # Fix the condition for b
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
  
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):  # Fix the conditions
        return 'NotATriangle'

    if a == b and b == c and a == c:  # Fix the condition to check for Equilateral
        return 'Equilateral'
    elif ((a**2) + (b**2)) == (c**2) or ((b**2) + (c**2)) == (a**2) or ((a**2) + (c**2)) == (b**2):
        return 'Right'
    elif a != b and b != c and a != c:  # Fix the condition
        return 'Scalene'
    else:
        return 'Isosceles' 

