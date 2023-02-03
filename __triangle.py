#Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating is given in the
#comments of the code. Also you will have to print the following after validation in respective functions:-
#1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)
#2.Valid Triangle:If the triangle sum property of sides is valid.
#3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b
#4.Invalid Rectangle: If Not Valid rectangle as stated above.
base=int(input('Enter base for triangle  :'))
length=int(input('Enter length for triangle  :'))
hypotenous=int(input('Enter hypotenous for triangle  :'))
if base**2+length**2==hypotenous**2:
    print("valid Triangle")
else:
    print('invalid Triangle')   



# Rectangle
len1=int(input('Enter Length1 for rectangle  :'))     
len2=int(input('Enter Length2 for rectangle  :'))    
base1=int(input('Enter Base1 for rectangle  :'))    
base2=int(input('Enter Base2 for rectangle  :'))    
if len1==len2 and base1==base2:
    print('valid Rectangle')
else:
    print('invalid Rectangle')    