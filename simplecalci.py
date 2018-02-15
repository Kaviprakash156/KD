x=float(input("enter the number1:"))
y=float(input("enter the number2:"))
K=int(input("chose the option \n 1]addition\n 2]subtraction\n 3]multiplication\n 4]division\n 5]power\n 6]square of x\n 7]square of y\n 8]cube of x\n 9]cube of y\n 10]modulus\n\nyour option is:"))
if (K==1):
  print("\nyour addition is",x+y)
elif (K==2):
  print("\nsubtraction",x-y)
elif (K==3):
  print("\nmultiplication",x*y)
elif(K==4) :
  if (y==0):
    print("\ninfinite")
  else:
    print("\ndivision",x/y)
elif(K==5):
  print("\npower is",x**y)
elif(K==6):
  print("\nsquare of x is",x**2)
elif(K==7):
  print("\nsquare of y is",y**2)
elif(K==8):
  print("\ncube of x is",x**3)
elif(K==9):
  print("\ncube of y is",y**3)
elif(K==10):
  print("\nmodulus is",x%y)
else:
  print("no operation")
