x=int(input("enter the number1:"))
y=int(input("enter the number2:"))
K=int(input("chose the option \n 1]addition\n 2]subtraction\n 3]multiplication\n 4]division\n 5]power\n 6]square of x\n 7]square of y\n 8]cube of x\n 9]cube of y\n 10]modulus\n\nOperation for="))
if (K==1):
  print("your addition is",x+y)
elif (K==2):
  print("subtraction",x-y)
elif (K==3):
  print("multiplication",x*y)
elif(K==4) :
  if (y==0):
    print("infinite")
  else:
    print("division",x/y)
elif(K==5):
  print("power is",x**y)
elif(K==6):
  print("square of x is",x**2)
elif(K==7):
  print("square of y is",y**2)
elif(K==8):
  print("cube of x is",x**3)
elif(K==9):
  print("cube of y is",y**3)
else:
  print("modulus is",x%y)
